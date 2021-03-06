import modifiers
import jobs


class Building(object):
    def __init__(self):
        self.name = "Building"
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
            "physics": 0,
            "society": 0,
            "engineering": 0,
            "motes": 0,
            "gases": 0,
            "crystals": 0,
            "admin": 0,
            "naval": 0,
            "storage": 0,
        }
        self.upkeep = {
            "housing": 0,
            "amenities": 0,
            "energy": 0,
            "minerals": 0,
            "food": 0,
            "trade": 0,
            "goods": 0,
            "alloys": 0,
            "unity": 0,
            "physics": 0,
            "society": 0,
            "engineering": 0,
            "motes": 0,
            "gases": 0,
            "crystals": 0,
            "admin": 0,
            "naval": 0,
            "storage": 0,
        }
        self.jobs_slots = []

    def aggregate_resources(self):
        return {
            "housing": self.production["housing"]+ self.upkeep["housing"]
            + sum(
                (j.production["housing"] * j.production_coefficients["housing"])
                + j.production_constants["housing"]
                + (j.upkeep["housing"] * j.upkeep_coefficients["housing"])
                + j.upkeep_constants["housing"]
                for j in self.jobs_slots
            ),
            "amenities": self.production["amenities"]+ self.upkeep["amenities"]
            + sum(
                (j.production["amenities"] * j.production_coefficients["amenities"])
                + j.production_constants["amenities"]
                + (j.upkeep["amenities"] * j.upkeep_coefficients["amenities"])
                + j.upkeep_constants["amenities"]
                for j in self.jobs_slots
            ),
            "energy": self.production["energy"]+ self.upkeep["energy"]
            + sum(
                (j.production["energy"] * j.production_coefficients["energy"])
                + j.production_constants["energy"]
                + (j.upkeep["energy"] * j.upkeep_coefficients["energy"])
                + j.upkeep_constants["energy"]
                for j in self.jobs_slots
            ),
            "minerals": self.production["minerals"]+ self.upkeep["minerals"]
            + sum(
                (j.production["minerals"] * j.production_coefficients["minerals"])
                + j.production_constants["minerals"]
                + (j.upkeep["minerals"] * j.upkeep_coefficients["minerals"])
                + j.upkeep_constants["minerals"]
                for j in self.jobs_slots
            ),
            "food": self.production["food"]+ self.upkeep["food"]
            + sum(
                (j.production["food"] * j.production_coefficients["food"])
                + j.production_constants["food"]
                + (j.upkeep["food"] * j.upkeep_coefficients["food"])
                + j.upkeep_constants["food"]
                for j in self.jobs_slots
            ),
            "trade": self.production["trade"]+ self.upkeep["trade"]
            + sum(
                (j.production["trade"] * j.production_coefficients["trade"])
                + j.production_constants["trade"]
                + (j.upkeep["trade"] * j.upkeep_coefficients["trade"])
                + j.upkeep_constants["trade"]
                for j in self.jobs_slots
            ),
            "goods": self.production["goods"]+ self.upkeep["goods"]
            + sum(
                (j.production["goods"] * j.production_coefficients["goods"])
                + j.production_constants["goods"]
                + (j.upkeep["goods"] * j.upkeep_coefficients["goods"])
                + j.upkeep_constants["goods"]
                for j in self.jobs_slots
            ),
            "alloys": self.production["alloys"]+ self.upkeep["alloys"]
            + sum(
                (j.production["alloys"] * j.production_coefficients["alloys"])
                + j.production_constants["alloys"]
                + (j.upkeep["alloys"] * j.upkeep_coefficients["alloys"])
                + j.upkeep_constants["alloys"]
                for j in self.jobs_slots
            ),
            "unity": self.production["unity"]+ self.upkeep["unity"]
            + sum(
                (j.production["unity"] * j.production_coefficients["unity"])
                + j.production_constants["unity"]
                + (j.upkeep["unity"] * j.upkeep_coefficients["unity"])
                + j.upkeep_constants["unity"]
                for j in self.jobs_slots
            ),
            "research": (
                self.production["physics"]+ self.upkeep["physics"]
                + sum(
                    (j.production["physics"] * j.production_coefficients["physics"])
                    + j.production_constants["physics"]
                    + (j.upkeep["physics"] * j.upkeep_coefficients["physics"])
                    + j.upkeep_constants["physics"]
                    for j in self.jobs_slots
                )
                + self.production["society"]+ self.upkeep["society"]
                + sum(
                    (j.production["society"] * j.production_coefficients["society"])
                    + j.production_constants["society"]
                    + (j.upkeep["society"] * j.upkeep_coefficients["society"])
                    + j.upkeep_constants["society"]
                    for j in self.jobs_slots
                )
                + self.production["engineering"]+ self.upkeep["engineering"]
                + sum(
                    (
                        j.production["engineering"]
                        * j.production_coefficients["engineering"]
                    )
                    + j.production_constants["engineering"]
                    + (j.upkeep["engineering"] * j.upkeep_coefficients["engineering"])
                    + j.upkeep_constants["engineering"]
                    for j in self.jobs_slots
                )
            )
            / 3,
            "motes": self.production["motes"]+ self.upkeep["motes"]
            + sum(
                (j.production["motes"] * j.production_coefficients["motes"])
                + j.production_constants["motes"]
                + (j.upkeep["motes"] * j.upkeep_coefficients["motes"])
                + j.upkeep_constants["motes"]
                for j in self.jobs_slots
            ),
            "gases": self.production["gases"]+ self.upkeep["gases"]
            + sum(
                (j.production["gases"] * j.production_coefficients["gases"])
                + j.production_constants["gases"]
                + (j.upkeep["gases"] * j.upkeep_coefficients["gases"])
                + j.upkeep_constants["gases"]
                for j in self.jobs_slots
            ),
            "crystals": self.production["crystals"]+ self.upkeep["crystals"]
            + sum(
                (j.production["crystals"] * j.production_coefficients["crystals"])
                + j.production_constants["crystals"]
                + (j.upkeep["crystals"] * j.upkeep_coefficients["crystals"])
                + j.upkeep_constants["crystals"]
                for j in self.jobs_slots
            ),
            "admin": self.production["admin"]+ self.upkeep["admin"]
            + sum(
                (j.production["admin"] * j.production_coefficients["admin"])
                + j.production_constants["admin"]
                + (j.upkeep["admin"] * j.upkeep_coefficients["admin"])
                + j.upkeep_constants["admin"]
                for j in self.jobs_slots
            ),
            "naval": self.production["naval"]+ self.upkeep["naval"]
            + sum(
                (j.production["naval"] * j.production_coefficients["naval"])
                + j.production_constants["naval"]
                + (j.upkeep["naval"] * j.upkeep_coefficients["naval"])
                + j.upkeep_constants["naval"]
                for j in self.jobs_slots
            ),
            "storage": self.production["storage"]+ self.upkeep["storage"]
            + sum(
                (j.production["storage"] * j.production_coefficients["storage"])
                + j.production_constants["storage"]
                + (j.upkeep["storage"] * j.upkeep_coefficients["storage"])
                + j.upkeep_constants["storage"]
                for j in self.jobs_slots
            ),
            "jobs": len(self.jobs_slots),
        }

    def aggregate_production(self):
        return {
            "housing": self.production["housing"]
            + sum(
                (j.production["housing"] * j.production_coefficients["housing"])
                + j.production_constants["housing"]
                for j in self.jobs_slots
            ),
            "amenities": self.production["amenities"]
            + sum(
                (j.production["amenities"] * j.production_coefficients["amenities"])
                + j.production_constants["amenities"]
                for j in self.jobs_slots
            ),
            "energy": self.production["energy"]
            + sum(
                (j.production["energy"] * j.production_coefficients["energy"])
                + j.production_constants["energy"]
                for j in self.jobs_slots
            ),
            "minerals": self.production["minerals"]
            + sum(
                (j.production["minerals"] * j.production_coefficients["minerals"])
                + j.production_constants["minerals"]
                for j in self.jobs_slots
            ),
            "food": self.production["food"]
            + sum(
                (j.production["food"] * j.production_coefficients["food"])
                + j.production_constants["food"]
                for j in self.jobs_slots
            ),
            "trade": self.production["trade"]
            + sum(
                (j.production["trade"] * j.production_coefficients["trade"])
                + j.production_constants["trade"]
                for j in self.jobs_slots
            ),
            "goods": self.production["goods"]
            + sum(
                (j.production["goods"] * j.production_coefficients["goods"])
                + j.production_constants["goods"]
                for j in self.jobs_slots
            ),
            "alloys": self.production["alloys"]
            + sum(
                (j.production["alloys"] * j.production_coefficients["alloys"])
                + j.production_constants["alloys"]
                for j in self.jobs_slots
            ),
            "unity": self.production["unity"]
            + sum(
                (j.production["unity"] * j.production_coefficients["unity"])
                + j.production_constants["unity"]
                for j in self.jobs_slots
            ),
            "research": (
                self.production["physics"]
                + sum(
                    (j.production["physics"] * j.production_coefficients["physics"])
                    + j.production_constants["physics"]
                    for j in self.jobs_slots
                )
                + self.production["society"]
                + sum(
                    (j.production["society"] * j.production_coefficients["society"])
                    + j.production_constants["society"]
                    for j in self.jobs_slots
                )
                + self.production["engineering"]
                + sum(
                    (
                        j.production["engineering"]
                        * j.production_coefficients["engineering"]
                    )
                    + j.production_constants["engineering"]
                    for j in self.jobs_slots
                )
            )
            / 3,
            "motes": self.production["motes"]
            + sum(
                (j.production["motes"] * j.production_coefficients["motes"])
                + j.production_constants["motes"]
                for j in self.jobs_slots
            ),
            "gases": self.production["gases"]
            + sum(
                (j.production["gases"] * j.production_coefficients["gases"])
                + j.production_constants["gases"]
                for j in self.jobs_slots
            ),
            "crystals": self.production["crystals"]
            + sum(
                (j.production["crystals"] * j.production_coefficients["crystals"])
                + j.production_constants["crystals"]
                for j in self.jobs_slots
            ),
            "admin": self.production["admin"]
            + sum(
                (j.production["admin"] * j.production_coefficients["admin"])
                + j.production_constants["admin"]
                for j in self.jobs_slots
            ),
            "naval": self.production["naval"]
            + sum(
                (j.production["naval"] * j.production_coefficients["naval"])
                + j.production_constants["naval"]
                for j in self.jobs_slots
            ),
            "storage": self.production["storage"]
            + sum(
                (j.production["storage"] * j.production_coefficients["storage"])
                + j.production_constants["storage"]
                for j in self.jobs_slots
            ),
            "jobs": len(self.jobs_slots),
        }
    def aggregate_upkeep(self):
        return {
            "housing": self.upkeep["housing"]
            + sum(
                (j.upkeep["housing"] * j.upkeep_coefficients["housing"])
                + j.upkeep_constants["housing"]
                for j in self.jobs_slots
            ),
            "amenities": self.upkeep["amenities"]
            + sum(
                (j.upkeep["amenities"] * j.upkeep_coefficients["amenities"])
                + j.upkeep_constants["amenities"]
                for j in self.jobs_slots
            ),
            "energy": self.upkeep["energy"]
            + sum(
                (j.upkeep["energy"] * j.upkeep_coefficients["energy"])
                + j.upkeep_constants["energy"]
                for j in self.jobs_slots
            ),
            "minerals": self.upkeep["minerals"]
            + sum(
                (j.upkeep["minerals"] * j.upkeep_coefficients["minerals"])
                + j.upkeep_constants["minerals"]
                for j in self.jobs_slots
            ),
            "food": self.upkeep["food"]
            + sum(
                (j.upkeep["food"] * j.upkeep_coefficients["food"])
                + j.upkeep_constants["food"]
                for j in self.jobs_slots
            ),
            "trade": self.upkeep["trade"]
            + sum(
                (j.upkeep["trade"] * j.upkeep_coefficients["trade"])
                + j.upkeep_constants["trade"]
                for j in self.jobs_slots
            ),
            "goods": self.upkeep["goods"]
            + sum(
                (j.upkeep["goods"] * j.upkeep_coefficients["goods"])
                + j.upkeep_constants["goods"]
                for j in self.jobs_slots
            ),
            "alloys": self.upkeep["alloys"]
            + sum(
                (j.upkeep["alloys"] * j.upkeep_coefficients["alloys"])
                + j.upkeep_constants["alloys"]
                for j in self.jobs_slots
            ),
            "unity": self.upkeep["unity"]
            + sum(
                (j.upkeep["unity"] * j.upkeep_coefficients["unity"])
                + j.upkeep_constants["unity"]
                for j in self.jobs_slots
            ),
            "research": (
                self.upkeep["physics"]
                + sum(
                    (j.upkeep["physics"] * j.upkeep_coefficients["physics"])
                    + j.upkeep_constants["physics"]
                    for j in self.jobs_slots
                )
                + self.upkeep["society"]
                + sum(
                    (j.upkeep["society"] * j.upkeep_coefficients["society"])
                    + j.upkeep_constants["society"]
                    for j in self.jobs_slots
                )
                + self.upkeep["engineering"]
                + sum(
                    (
                        j.upkeep["engineering"]
                        * j.upkeep_coefficients["engineering"]
                    )
                    + j.upkeep_constants["engineering"]
                    for j in self.jobs_slots
                )
            )
            / 3,
            "motes": self.upkeep["motes"]
            + sum(
                (j.upkeep["motes"] * j.upkeep_coefficients["motes"])
                + j.upkeep_constants["motes"]
                for j in self.jobs_slots
            ),
            "gases": self.upkeep["gases"]
            + sum(
                (j.upkeep["gases"] * j.upkeep_coefficients["gases"])
                + j.upkeep_constants["gases"]
                for j in self.jobs_slots
            ),
            "crystals": self.upkeep["crystals"]
            + sum(
                (j.upkeep["crystals"] * j.upkeep_coefficients["crystals"])
                + j.upkeep_constants["crystals"]
                for j in self.jobs_slots
            ),
            "admin": self.upkeep["admin"]
            + sum(
                (j.upkeep["admin"] * j.upkeep_coefficients["admin"])
                + j.upkeep_constants["admin"]
                for j in self.jobs_slots
            ),
            "naval": self.upkeep["naval"]
            + sum(
                (j.upkeep["naval"] * j.upkeep_coefficients["naval"])
                + j.upkeep_constants["naval"]
                for j in self.jobs_slots
            ),
            "storage": self.upkeep["storage"]
            + sum(
                (j.upkeep["storage"] * j.upkeep_coefficients["storage"])
                + j.upkeep_constants["storage"]
                for j in self.jobs_slots
            ),
            "jobs": len(self.jobs_slots),
        }

class SystemCapitalComplex(Building):
    def __init__(self):
        super().__init__()
        self.name = "SystemCapitalComplex"

        self.production["housing"] = 10
        self.production["amenities"] = 10
        self.upkeep["energy"] = -10

        self.administrators = 4
        self.enforcers = 3
        self.nobles = 0
        self.high_priests = 0
        self.merchants = 0
        self.science_directors = 0
        self.executives = 0
        self.roboticists = 0

        if "aristocratic_elite" in modifiers.civics:
            self.administrators -= 2
            self.nobles += 2
        if "exalted_priesthood" in modifiers.civics:
            self.administrators -= 2
            self.high_priests += 2
        if "merchant_guilds" in modifiers.civics:
            self.administrators -= 2
            self.merchants += 2
        if "technocracy" in modifiers.civics:
            self.administrators -= 2
            self.science_directors += 2
        if "corporate" in modifiers.authority:
            self.administrators -= 4
            self.executives += 4
        if "synthetic_evolution" in modifiers.perks:
            self.roboticists += 3

        for c in range(self.administrators):
            self.jobs_slots.append(jobs.Administrator())
        for c in range(self.enforcers):
            self.jobs_slots.append(jobs.Enforcer())
        for c in range(self.nobles):
            self.jobs_slots.append(jobs.Noble())
        for c in range(self.high_priests):
            self.jobs_slots.append(jobs.HighPriest())
        for c in range(self.merchants):
            self.jobs_slots.append(jobs.Merchant())
        for c in range(self.science_directors):
            self.jobs_slots.append(jobs.ScienceDirector())
        for c in range(self.executives):
            self.jobs_slots.append(jobs.Executive())
        for c in range(self.roboticists):
            self.jobs_slots.append(jobs.Roboticist())


class AlloyNanoPlants(Building):
    def __init__(self):
        super().__init__()
        self.name = "AlloyNanoPlants"

        self.upkeep["energy"] = -8
        self.upkeep["motes"] = -2

        self.metallurgists = 8
        self.foundry_drone = 0
        self.fabricator = 0

        if "hive_mind" in modifiers.authority:
            self.metallurgists = 0
            self.foundry_drone = 8
            self.fabricator = 0
        if "machine_intelligence" in modifiers.authority:
            self.metallurgists = 0
            self.foundry_drone = 0
            self.fabricator = 8

        for c in range(self.metallurgists):
            self.jobs_slots.append(jobs.Metallurgist())
        for c in range(self.foundry_drone):
            self.jobs_slots.append(jobs.FoundryDrone())
        for c in range(self.fabricator):
            self.jobs_slots.append(jobs.Fabricator())


class AdvancedResearchComplexes(Building):
    def __init__(self):
        super().__init__()
        self.name = "AdvancedResearchComplexes"

        self.upkeep["energy"] = -8
        self.upkeep["gases"] = -2

        self.researchers = 8
        self.brain_drone = 0
        self.calculators = 0

        if "hive_mind" in modifiers.authority:
            self.researchers = 0
            self.brain_drone = 8
            self.calculators = 0
        if "machine_intelligence" in modifiers.authority:
            self.researchers = 0
            self.brain_drone = 0
            self.calculators = 8

        for c in range(self.researchers):
            self.jobs_slots.append(jobs.Researcher())
        for c in range(self.brain_drone):
            self.jobs_slots.append(jobs.BrainDrone())
        for c in range(self.calculators):
            self.jobs_slots.append(jobs.Calculator())


class CivilianRepliComplexes(Building):
    def __init__(self):
        super().__init__()
        self.name = "CivilianRepliComplexes"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2

        self.artisans = 8
        self.artisan_drones = 0

        if "rogue_servitor" in modifiers.civics:
            self.artisans = 0
            self.artisan_drones = 8

        for c in range(self.artisans):
            self.jobs_slots.append(jobs.Artisan())
        for c in range(self.artisan_drones):
            self.jobs_slots.append(jobs.ArtisanDrone())


class HypercommsForum(Building):
    def __init__(self):
        super().__init__()
        self.name = "HypercommsForum"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2

        self.culture_workers = 8

        for c in range(self.culture_workers):
            self.jobs_slots.append(jobs.CultureWorker())


class SacredNexus(Building):
    def __init__(self):
        super().__init__()
        self.name = "SacredNexus"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2

        self.priests = 8

        for c in range(self.priests):
            self.jobs_slots.append(jobs.Priest())


class SynergyForum(Building):
    def __init__(self):
        super().__init__()
        self.name = "SynergyForum"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2

        self.managers = 8

        for c in range(self.managers):
            self.jobs_slots.append(jobs.Manager())


class ConfluenceOfThought(Building):
    def __init__(self):
        super().__init__()
        self.name = "ConfluenceOfThought"
        self.upkeep["energy"] = -8
        self.upkeep["gases"] = -2

        self.synapse_drones = 8

        for c in range(self.synapse_drones):
            self.jobs_slots.append(jobs.SynapseDrone())


class SimulationComplex(Building):
    def __init__(self):
        super().__init__()
        self.name = "SimulationComplex"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2

        self.evaluators = 8

        for c in range(self.evaluators):
            self.jobs_slots.append(jobs.Evaluator())


class HyperEntertainmentForums(Building):
    def __init__(self):
        super().__init__()
        self.name = "HyperEntertainmentForums"
        self.upkeep["energy"] = -5
        self.upkeep["gases"] = -1

        self.entertainers = 5
        self.duelists = 0

        if "warrior_culture" in modifiers.ethics:
            self.entertainers = 0
            self.duelists = 5

        for c in range(self.entertainers):
            self.jobs_slots.append(jobs.Entertainer())
        for c in range(self.duelists):
            self.jobs_slots.append(jobs.Duelist())


class AdministrativePark(Building):
    def __init__(self):
        super().__init__()
        self.name = "AdministrativePark"
        self.upkeep["energy"] = -5
        self.upkeep["crystals"] = -1

        self.bureaucrats = 5

        for c in range(self.bureaucrats):
            self.jobs_slots.append(jobs.Bureaucrat())


class SystemConflux(Building):
    def __init__(self):
        super().__init__()
        self.name = "SystemConflux"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2

        self.coordinators = 8

        for c in range(self.coordinators):
            self.jobs_slots.append(jobs.Coordinator())


class HallOfJudgement(Building):
    def __init__(self):
        super().__init__()
        self.name = "HallOfJudgement"
        self.upkeep["energy"] = -5
        self.upkeep["gases"] = -1

        self.enforcers = 5

        for c in range(self.enforcers):
            self.jobs_slots.append(jobs.Enforcer())


class SentinelPosts(Building):
    def __init__(self):
        super().__init__()
        self.name = "SentinelPosts"
        self.upkeep["energy"] = -2

        self.hunter_seeker_drones = 2

        for c in range(self.hunter_seeker_drones):
            self.jobs_slots.append(jobs.HunterSeekerDrone())


class HydroponicsFarms(Building):
    def __init__(self):
        super().__init__()
        self.name = "HydroponicsFarms"
        self.upkeep["energy"] = -2

        self.farmers = 2
        self.agri_drones = 0

        if "hive_mind" in modifiers.authority:
            self.farmers = 0
            self.agri_drones = 2

        for c in range(self.farmers):
            self.jobs_slots.append(jobs.Farmer())
        for c in range(self.agri_drones):
            self.jobs_slots.append(jobs.AgriDrone())


class CommerceMegaplexes(Building):
    def __init__(self):
        super().__init__()
        self.name = "CommerceMegaplexes"
        self.upkeep["energy"] = -5
        self.upkeep["crystals"] = -1

        self.clerks = 10
        self.merchants = 1

        for c in range(self.clerks):
            self.jobs_slots.append(jobs.Clerk())
        for c in range(self.merchants):
            self.jobs_slots.append(jobs.Merchant())


class ChemicalPlants(Building):
    def __init__(self):
        super().__init__()
        self.name = "ChemicalPlants"
        self.upkeep["energy"] = -3

        self.chemists = 1
        self.chem_drones = 0

        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.chemists = 0
            self.chem_drones = 1

        for j in range(self.chemists):
            self.jobs_slots.append(jobs.Chemist())
        for j in range(self.chem_drones):
            self.jobs_slots.append(jobs.ChemDrone())


class ExoticGasRefineries(Building):
    def __init__(self):
        super().__init__()
        self.name = "ExoticGasRefineries"
        self.upkeep["energy"] = -3

        self.gas_refiners = 1
        self.refinery_drones = 0

        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.gas_refiners = 0
            self.refinery_drones = 1

        for j in range(self.gas_refiners):
            self.jobs_slots.append(jobs.GasRefiner())
        for j in range(self.refinery_drones):
            self.jobs_slots.append(jobs.RefineryDrone())


class SyntheticCrystalPlants(Building):
    def __init__(self):
        super().__init__()
        self.name = "SyntheticCrystalPlants"
        self.upkeep["energy"] = -3

        self.translucers = 1
        self.lensing_drones = 0

        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.translucers = 0
            self.lensing_drones = 1

        for j in range(self.translucers):
            self.jobs_slots.append(jobs.Translucer())
        for j in range(self.lensing_drones):
            self.jobs_slots.append(jobs.LensingDrone())


class ParadiseDome(Building):
    def __init__(self):
        super().__init__()
        self.name = "ParadiseDome"
        self.production["housing"] = 6
        self.production["amenities"] = 10
        self.upkeep["energy"] = -3
        self.upkeep["crystals"] = -1


class UtopianCommunalHousing(Building):
    def __init__(self):
        super().__init__()
        self.name = "UtopianCommunalHousing"
        self.production["housing"] = 10
        self.production["amenities"] = 6
        self.upkeep["energy"] = -3
        self.upkeep["crystals"] = -1


class ExpandedWarren(Building):
    def __init__(self):
        super().__init__()
        self.name = "ExpandedWarren"
        self.production["housing"] = 6
        self.production["amenities"] = 10
        self.upkeep["energy"] = -3
        self.upkeep["crystals"] = -1


class UpgradedDroneStorage(Building):
    def __init__(self):
        super().__init__()
        self.name = "UpgradedDroneStorage"
        self.production["housing"] = 8
        self.production["amenities"] = 6
        self.upkeep["energy"] = -3
        self.upkeep["crystals"] = -1


class OrganicParadise(Building):
    def __init__(self):
        super().__init__()
        self.name = "OrganicParadise"
        self.upkeep["energy"] = -5
        self.upkeep["gases"] = -1

        self.bio_trophies = 1
        self.maintenance_drones = 0

        for j in range(self.bio_trophies):
            self.jobs_slots.append(jobs.BioTrophy())
        for j in range(self.maintenance_drones):
            self.jobs_slots.append(jobs.MaintenanceDrone())


class Fortress(Building):
    def __init__(self):
        super().__init__()
        self.name = "Fortress"
        self.production["housing"] = 3
        self.upkeep["energy"] = -1
        self.upkeep["motes"] = -1

        self.soldiers = 3
        self.warrior_drones = 0

        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.soldiers = 0
            self.warrior_drones = 3

        for j in range(self.soldiers):
            self.jobs_slots.append(jobs.Soldier())
        for j in range(self.warrior_drones):
            self.jobs_slots.append(jobs.WarriorDrone())


class BetharianPowerPlant(Building):
    def __init__(self):
        super().__init__()
        self.name = "BetharianPowerPlant"
        self.production["energy"] = 10

        self.technicians = 4
        self.tech_drones = 0

        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.technicians = 0
            self.tech_drones = 4

        for j in range(self.technicians):
            self.jobs_slots.append(jobs.Technician())
        for j in range(self.tech_drones):
            self.jobs_slots.append(jobs.TechDrone())


class AlienZoo(Building):
    def __init__(self):
        super().__init__()
        self.name = "AlienZoo"
        self.upkeep["energy"] = -1

        self.culture_workers = 2
        self.entertainers = 1
        self.duelists = 0

        if "warrior_culture" in modifiers.civics:
            self.culture_workers = 2
            self.entertainers -= 1
            self.duelists = 1

        for j in range(self.culture_workers):
            self.jobs_slots.append(jobs.CultureWorker())
        for j in range(self.entertainers):
            self.jobs_slots.append(jobs.Entertainer())
        for j in range(self.duelists):
            self.jobs_slots.append(jobs.Duelist())


class CrystalMines(Building):
    def __init__(self):
        super().__init__()
        self.name = "CrystalMines"
        self.upkeep["energy"] = -1

        self.crystal_miners = 1
        self.crystal_mining_drones = 0

        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.crystal_miners = 0
            self.crystal_mining_drones = 1

        for j in range(self.crystal_miners):
            self.jobs_slots.append(jobs.CrystalMiner())
        for j in range(self.crystal_mining_drones):
            self.jobs_slots.append(jobs.CrystalMiningDrone())


class GasExtractionWells(Building):
    def __init__(self):
        super().__init__()
        self.name = "GasExtractionWells"
        self.upkeep["energy"] = -1

        self.gas_extractors = 1
        self.gas_extraction_drones = 0

        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.gas_extractors = 0
            self.gas_extraction_drones = 1

        for j in range(self.gas_extractors):
            self.jobs_slots.append(jobs.GasExtractor())
        for j in range(self.gas_extraction_drones):
            self.jobs_slots.append(jobs.GasExtractionDrone())


class MoteHarvestingTraps(Building):
    def __init__(self):
        super().__init__()
        self.name = "MoteHarvestingTraps"
        self.upkeep["energy"] = -1

        self.mote_harvesters = 1
        self.mote_harvesting_drones = 0
        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.mote_harvesters = 0
            self.mote_harvesting_drones = 1

        for j in range(self.mote_harvesters):
            self.jobs_slots.append(jobs.MoteHarvester())
        for j in range(self.mote_harvesting_drones):
            self.jobs_slots.append(jobs.MoteHarvestingDrone())


class ResourceSilos(Building):
    def __init__(self):
        super().__init__()
        self.name = "ResourceSilos"
        self.upkeep["energy"] = -1
        self.production["storage"] = 2000

        self.clerks = 2
        self.maintenance_drones = 0

        if "gestalt_consciousness" in modifiers.ethics:
            self.clerks = 0
            self.maintenance_drones = 1

        for j in range(self.clerks):
            self.jobs_slots.append(jobs.Clerk())
        for j in range(self.maintenance_drones):
            self.jobs_slots.append(jobs.MaintenanceDrone())


class BioReactor(Building):
    def __init__(self):
        super().__init__()
        self.name = "BioReactor"
        self.production["energy"] = 20
        self.upkeep["food"] = -25


# class NaniteTransmuter(Building):
#     def __init__(self):
#         super().__init__()
# self.name = "NaniteTransmuter"
#         self.upkeep["energy"] = -5
#         self.production["food"] = 0
#         self.production["motes"] = 2
#         self.production["gases"] = 2
#         self.production["crystals"] = 2
#         self.nanites = -1


class SlaveHuts(Building):
    def __init__(self):
        super().__init__()
        self.name = "SlaveHuts"
        self.production["housing"] = 8
        self.upkeep["energy"] = -1
        self.production["food"] = 0


class OverseerResidences(Building):
    def __init__(self):
        super().__init__()
        self.name = "OverseerResidences"
        self.production["housing"] = 2
        self.upkeep["energy"] = -1
        self.production["food"] = 0

        self.slave_overseers = 2
        for j in range(self.slave_overseers):
            self.jobs_slots.append(jobs.SlaveOverseer())


class UniqueBuilding(Building):
    def __init__(self):
        super().__init__()


class PlanetaryShieldGenerator(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "PlanetaryShieldGenerator"
        self.upkeep["energy"] = -5


class MilitaryAcademy(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "MilitaryAcademy"
        self.upkeep["energy"] = -2

        self.soldiers = 1
        self.warrior_drones = 0
        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.soldiers = 0
            self.warrior_drones = 1

        for c in range(self.soldiers):
            self.jobs_slots.append(jobs.Soldier())
        for c in range(self.warrior_drones):
            self.jobs_slots.append(jobs.WarriorDrone())


class EnergyNexus(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "EnergyNexus"
        self.upkeep["energy"] = -2
        self.upkeep["gases"] = -1

        self.technicians = 2
        self.tech_drones = 0
        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.technicians = 0
            self.tech_drones = 2

        for j in range(self.technicians):
            self.jobs_slots.append(jobs.Technician())
        for j in range(self.tech_drones):
            self.jobs_slots.append(jobs.TechDrone())


class MineralPurificationHubs(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "MineralPurificationHubs"
        self.upkeep["energy"] = -2
        self.upkeep["motes"] = -1

        self.miners = 2
        self.mining_drones = 0
        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.miners = 0
            self.mining_drones = 2

        for j in range(self.miners):
            self.jobs_slots.append(jobs.Miner())
        for j in range(self.mining_drones):
            self.jobs_slots.append(jobs.MiningDrone())


class FoodProcessingCenters(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "FoodProcessingCenters"
        self.upkeep["energy"] = -2
        self.upkeep["motes"] = -1

        self.farmers = 2
        self.agri_drones = 0
        if (
            "hive_mind" in modifiers.authority
            or "machine_intelligence" in modifiers.authority
        ):
            self.farmers = 0
            self.agri_drones = 2

        for j in range(self.farmers):
            self.jobs_slots.append(jobs.Farmer())
        for j in range(self.agri_drones):
            self.jobs_slots.append(jobs.AgriDrone())


class AutoCuratingVault(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "AutoCuratingVault"
        self.upkeep["energy"] = -5
        self.upkeep["crystals"] = -1


class CitadelOfFaith(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "CitadelOfFaith"
        self.upkeep["energy"] = -5
        self.upkeep["crystals"] = -1

        self.priests = 5
        self.high_priests = 1
        for j in range(self.priests):
            self.jobs_slots.append(jobs.Priest())
        for j in range(self.high_priests):
            self.jobs_slots.append(jobs.HighPriest())


class VaultOfAcquisitions(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "VaultOfAcquisitions"
        self.upkeep["energy"] = -5
        self.upkeep["crystals"] = -1


class AlphaHub(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "AlphaHub"
        self.upkeep["energy"] = -5
        self.upkeep["crystals"] = -1


class ResearchInstitute(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "ResearchInstitute"
        self.upkeep["energy"] = -5
        self.upkeep["gases"] = -1

        self.science_directors = 1
        for j in range(self.science_directors):
            self.jobs_slots.append(jobs.ScienceDirector())


class PlanetarySupercomputer(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "PlanetarySupercomputer"
        self.upkeep["energy"] = -5
        self.upkeep["gases"] = -1

        self.science_directors = 1
        self.brain_drones = 0
        self.calculators = 0
        if "hive_mind" in modifiers.authority:
            self.science_directors = 0
            self.brain_drones = 1
            self.calculators = 0
        if "machine_intelligence" in modifiers.authority:
            self.science_directors = 0
            self.brain_drones = 0
            self.calculators = 1

        for j in range(self.science_directors):
            self.jobs_slots.append(jobs.ScienceDirector())
        for j in range(self.brain_drones):
            self.jobs_slots.append(jobs.BrainDrone())
        for j in range(self.calculators):
            self.jobs_slots.append(jobs.Calculator())


class MinistryOfProduction(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "MinistryOfProduction"
        self.upkeep["energy"] = -5
        self.upkeep["motes"] = -1

        self.administrators = 1
        for j in range(self.administrators):
            self.jobs_slots.append(jobs.Administrator())


class ResourceProcessingCenter(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "ResourceProcessingCenter"
        self.upkeep["energy"] = -5
        self.upkeep["motes"] = -1

        self.foundry_drones = 2
        self.fabricators = 0
        if "hive_mind" in modifiers.authority:
            self.foundry_drones = 2
            self.fabricators = 0
        if "machine_intelligence" in modifiers.authority:
            self.foundry_drones = 0
            self.fabricators = 1

        for j in range(self.foundry_drones):
            self.jobs_slots.append(jobs.FoundryDrone())
        for j in range(self.fabricators):
            self.jobs_slots.append(jobs.Fabricator())


class CytoRevitalizationCenter(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "CytoRevitalizationCenter"
        self.upkeep["energy"] = -5
        self.upkeep["gases"] = -1

        self.medical_workers = 5
        for j in range(self.medical_workers):
            self.jobs_slots.append(jobs.MedicalWorker())


class SpawningPools(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "SpawningPools"
        self.upkeep["energy"] = -2

        self.spawning_drones = 1
        for j in range(self.spawning_drones):
            self.jobs_slots.append(jobs.SpawningDrone())


class RobotAssemblyPlants(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "RobotAssemblyPlants"
        self.upkeep["energy"] = -5

        self.roboticists = 1
        for j in range(self.roboticists):
            self.jobs_slots.append(jobs.Roboticist())


class MachineAssemblyComplex(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "MachineAssemblyComplex"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2

        self.replicators = 3
        for j in range(self.replicators):
            self.jobs_slots.append(jobs.Replicator())


class GalacticStockExchange(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "GalacticStockExchange"
        self.upkeep["energy"] = -5
        self.upkeep["crystals"] = -1

        self.merchants = 2
        for j in range(self.merchants):
            self.jobs_slots.append(jobs.Merchant())


class NobleEstates(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "NobleEstates"
        self.upkeep["energy"] = -2

        self.nobles = 1
        for j in range(self.nobles):
            self.jobs_slots.append(jobs.Noble())


class SlaveProcessingFacility(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "SlaveProcessingFacility"
        self.upkeep["energy"] = -2


class CloneVats(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "CloneVats"
        self.upkeep["energy"] = -2


class PsiCorps(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "PsiCorps"
        self.upkeep["energy"] = -5

        self.telepaths = 2
        for j in range(self.telepaths):
            self.jobs_slots.append(jobs.Telepath())


class EmpireUniqueBuilding(Building):
    def __init__(self):
        super().__init__()
        self.jobs_slots = []


class GrandEmbassyComplex(EmpireUniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "GrandEmbassyComplex"
        self.upkeep["energy"] = -8
        self.upkeep["crystals"] = -2


class OmegaAlignment(EmpireUniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "OmegaAlignment"
        self.upkeep["energy"] = -8
        self.production["physics"] = 16
