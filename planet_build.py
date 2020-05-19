import math
import helpers
import districts
import buildings as bs
from collections import Counter


class PlanetBuild(object):
    def __init__(self, planet):
        self._name = planet.name

        self._designation = None

        self.maximum_districts = planet.maximum_districts
        self.maximum_generator_districts = planet.maximum_generator_districts
        self.maximum_mining_districts = planet.maximum_mining_districts
        self.maximum_agriculture_districts = planet.maximum_agriculture_districts

        self._city_districts = None
        self._generator_districts = None
        self._mining_districts = None
        self._agriculture_districts = None
        self._buildings = None

        self.city_districts = []
        self.generator_districts = []
        self.mining_districts = []
        self.agriculture_districts = []
        self.buildings = [bs.SystemCapitalComplex()]
        self.production = {
            "housing": 0,
            "amenities": 0,
            "energy": 0,
            "minerals": 0,
            "food": 0,
            "trade": 0,
            "goods": 0,
            "alloys": 0,
            "unity": 0,
            "research": 0,
            "motes": 0,
            "gases": 0,
            "crystals": 0,
            "admin": 0,
            "naval": 0,
            "jobs": 0,
        }
        self.modifiers = {
            "housing": 1.0,
            "amenities": 1.0,
            "energy": 1.0,
            "minerals": 1.0,
            "food": 1.0,
            "trade": 1.0,
            "goods": 1.0,
            "alloys": 1.0,
            "unity": 1.0,
            "research": 1.0,
            "motes": 1.0,
            "gases": 1.0,
            "crystals": 1.0,
            "admin": 1.0,
            "naval": 1.0,
            "jobs": 1.0,
        }
        self.offsets = {
            "housing": 0,
            "amenities": 0,
            "energy": 0,
            "minerals": 0,
            "food": 0,
            "trade": 0,
            "goods": 0,
            "alloys": 0,
            "unity": 0,
            "research": 0,
            "motes": 0,
            "gases": 0,
            "crystals": 0,
            "admin": 0,
            "naval": 0,
            "jobs": 0,
        }

        self.build_planet()

    def prepare_for_export(self):
        self._city_districts = len(self.city_districts)
        self._generator_districts = len(self.generator_districts)
        self._mining_districts = len(self.mining_districts)
        self._agriculture_districts = len(self.agriculture_districts)
        self._buildings = [b.name for b in self.buildings]

    # TODO: empire capital designation fixed on one planet
    def build_planet(self):
        self.update_planet_build()
        while (
            len(self.city_districts)
            + len(self.generator_districts)
            + len(self.mining_districts)
            + len(self.agriculture_districts)
        ) < self.maximum_districts or len(self.buildings) < 16:
            self.build()

    def build(self):
        if self.production["housing"] <= 0:
            self.build_housing()
        elif self.production["amenities"] <= 0:
            self.build_amenities()
        else:
            self.build_in_priority_order()
        self.update_planet_build()
        return

    def build_housing(self):
        pass

    def build_amenities(self):
        pass

    def build_in_priority_order(self):
        pass

    def update_planet_build(self):
        for key in self.production.keys():
            if key == "admin":
                self.production[key] = -5
            else:
                self.production[key] = 0
        for d in (
            self.city_districts
            + self.generator_districts
            + self.mining_districts
            + self.agriculture_districts
            + self.buildings
        ):
            for key, value in d.aggregate_resources().items():
                self.production[key] += (value * self.modifiers[key]) + self.offsets[
                    key
                ]

    def balance_buildings(self):
        production = helpers.aggregate_production(helpers.complete_planet_builds, self)
        errors = helpers.calculate_aggregate_error(
            helpers.resource_relative_values,
            helpers.target_production_proportions,
            production,
        )
        building_errors = {
            key: value
            for (key, value) in errors.items()
            if key in ["food", "trade", "goods","alloys","unity","research","motes","gases","crystals","admin","naval"]
            # if key
            # in [
            #     "trade",
            #     "goods",
            #     "alloys",
            #     "unity",
            #     "research",
            #     "motes",
            #     "gases",
            #     "crystals",
            #     "admin",
            #     "naval",
            # ]
        }
        lowest = min(building_errors, key=building_errors.get)
        if lowest == "food":
            return bs.HydroponicsFarms()
        if lowest == "trade":
            return bs.CommerceMegaplexes()
        if lowest == "goods":
            return bs.CivilianRepliComplexes()
        if lowest == "alloys":
            return bs.AlloyNanoPlants()
        if lowest == "unity":
            return bs.HypercommsForum()
        if lowest == "research":
            return bs.AdvancedResearchComplexes()
        if lowest == "motes":
            return bs.ChemicalPlants()
        if lowest == "gases":
            return bs.ExoticGasRefineries()
        if lowest == "crystals":
            return bs.SyntheticCrystalPlants()
        if lowest == "admin":
            return bs.AdministrativePark()
        if lowest == "naval":
            return bs.Fortress()

    def balance_refineries(self):
        production = helpers.aggregate_production(helpers.complete_planet_builds, self)
        errors = helpers.calculate_aggregate_error(
            helpers.resource_relative_values,
            helpers.target_production_proportions,
            production,
        )
        refinery_errors = {
            key: value
            for (key, value) in errors.items()
            if key in ["motes", "gases", "crystals",]
        }
        lowest = min(refinery_errors, key=refinery_errors.get)

        if lowest == "motes":
            return bs.ChemicalPlants()
        if lowest == "gases":
            return bs.ExoticGasRefineries()
        if lowest == "crystals":
            return bs.SyntheticCrystalPlants()

    def balance_districts(self):
        production = helpers.aggregate_production(helpers.complete_planet_builds, self)
        errors = helpers.calculate_aggregate_error(
            helpers.resource_relative_values,
            helpers.target_production_proportions,
            production,
        )
        district_errors = {
            key: value
            for (key, value) in errors.items()
            if key in ["energy", "minerals", "food",]
            # if key in ["energy", "minerals",]
        }
        lowest = min(district_errors, key=district_errors.get)

        count_available = []
        if self.generator_districts_available():
            count_available.append(len(self.generator_districts))
        if self.mining_districts_available():
            count_available.append(len(self.mining_districts))
        if self.agriculture_districts_available():
            count_available.append(len(self.agriculture_districts))

        if len(count_available) != 0:
            if self.generator_districts_available() and lowest == "energy":
                self.generator_districts.append(districts.GeneratorDistrict())
                return
            if self.mining_districts_available() and lowest == "minerals":
                self.mining_districts.append(districts.MiningDistrict())
                return
            if self.agriculture_districts_available() and lowest == "food":
                self.agriculture_districts.append(districts.AgricultureDistrict())
                return
        self.city_districts.append(districts.CityDistrict())
        return

    def districts_available(self):
        return (
            len(self.city_districts)
            + len(self.generator_districts)
            + len(self.mining_districts)
            + len(self.agriculture_districts)
        ) < self.maximum_districts

    def generator_districts_available(self):
        return (
            self.districts_available()
            and len(self.generator_districts) < self.maximum_generator_districts
        )

    def mining_districts_available(self):
        return (
            self.districts_available()
            and len(self.mining_districts) < self.maximum_mining_districts
        )

    def agriculture_districts_available(self):
        return (
            self.districts_available()
            and len(self.agriculture_districts) < self.maximum_agriculture_districts
        )

    def buildings_available(self):
        if self.districts_available():
            building_slots = math.floor(self.production["jobs"] / 5) + 1
            if building_slots >= 16:
                building_slots = 16
        else:
            building_slots = 16
        return len(self.buildings) < building_slots


class MiningWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "MiningWorld"
        self.modifiers = {
            "minerals": 1.0,
        }

    def build_housing(self):
        if self.mining_districts_available():
            self.mining_districts.append(districts.MiningDistrict())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.mining_districts_available():
            self.mining_districts.append(districts.MiningDistrict())
        elif self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(
                isinstance(b, bs.MineralPurificationHubs) for b in self.buildings
            ):
                self.buildings.append(bs.MineralPurificationHubs())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(self.balance_buildings())
        if self.districts_available():
            self.balance_districts()


class AgriWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "AgriWorld"
        self.modifiers = {
            "food": 1.0,
        }

    def build_housing(self):
        if self.agriculture_districts_available():
            self.agriculture_districts.append(districts.AgricultureDistrict())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.agriculture_districts_available():
            self.agriculture_districts.append(districts.AgricultureDistrict())
        elif self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.FoodProcessingCenters) for b in self.buildings):
                self.buildings.append(bs.FoodProcessingCenters())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(self.balance_buildings())
        if self.districts_available():
            self.balance_districts()


class GeneratorWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "GeneratorWorld"
        self.modifiers = {
            "energy": 1.0,
        }

    def build_housing(self):
        if self.generator_districts_available():
            self.generator_districts.append(districts.GeneratorDistrict())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.generator_districts_available():
            self.generator_districts.append(districts.GeneratorDistrict())
        elif self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.EnergyNexus) for b in self.buildings):
                self.buildings.append(bs.EnergyNexus())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(self.balance_buildings())
        if self.districts_available():
            self.balance_districts()


class ForgeWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "ForgeWorld"

    def build_housing(self):
        if self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.MinistryOfProduction) for b in self.buildings):
                self.buildings.append(bs.MinistryOfProduction())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(bs.AlloyNanoPlants())
        if self.districts_available():
            self.balance_districts()


class IndustrialWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "IndustrialWorld"

    def build_housing(self):
        if self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.MinistryOfProduction) for b in self.buildings):
                self.buildings.append(bs.MinistryOfProduction())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(bs.CivilianRepliComplexes())
        if self.districts_available():
            self.balance_districts()


class RefineryWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "RefineryWorld"

    def build_housing(self):
        if self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(self.balance_refineries())
        if self.districts_available():
            self.balance_districts()


class TechWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "TechWorld"

    def build_housing(self):
        if self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.ResearchInstitute) for b in self.buildings):
                self.buildings.append(bs.ResearchInstitute())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(bs.AdvancedResearchComplexes())
        if self.districts_available():
            self.balance_districts()


class FortressWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "FortressWorld"

    def build_housing(self):
        if self.buildings_available():
            self.buildings.append(bs.Fortress())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(bs.Fortress())
        if self.districts_available():
            self.balance_districts()


class BureaucraticWorld(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "BureaucraticWorld"
        self.offsets["admin"] = 0

    def build_housing(self):
        if self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            self.buildings.append(bs.AdministrativePark())
        if self.districts_available():
            self.balance_districts()


class EmpireCapital(PlanetBuild):
    def __init__(self, planet):
        super().__init__(planet)
        self._designation = "EmpireCapital"

    def build_housing(self):
        if self.districts_available():
            self.city_districts.append(districts.CityDistrict())
        elif self.buildings_available():
            self.buildings.append(bs.ParadiseDome())

    def build_amenities(self):
        if self.buildings_available():
            self.buildings.append(bs.HyperEntertainmentForums())
        elif self.districts_available():
            self.city_districts.append(districts.CityDistrict())

    def build_in_priority_order(self):
        if self.buildings_available():
            if not any(isinstance(b, bs.RobotAssemblyPlants) for b in self.buildings):
                self.buildings.append(bs.RobotAssemblyPlants())

            if not any(
                isinstance(b, bs.CytoRevitalizationCenter) for b in self.buildings
            ):
                self.buildings.append(bs.CytoRevitalizationCenter())

            if not any(isinstance(b, bs.AutoCuratingVault) for b in self.buildings):
                self.buildings.append(bs.AutoCuratingVault())

            if not any(isinstance(b, bs.MilitaryAcademy) for b in self.buildings):
                self.buildings.append(bs.MilitaryAcademy())

            if not any(isinstance(b, bs.GrandEmbassyComplex) for b in self.buildings):
                self.buildings.append(bs.GrandEmbassyComplex())

            self.buildings.append(self.balance_buildings())
        if self.districts_available():
            self.balance_districts()
