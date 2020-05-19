import modifiers
import jobs


class Building(object):
    def __init__(self):
        self.name = "Building"
        self.housing = 0
        self.amenities = 0
        self.energy = 0
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.admin = 0
        self.naval = 0
        self.jobs_slots = []

    def aggregate_resources(self):
        return {
            "housing": self.housing + sum(j.housing for j in self.jobs_slots),
            "amenities": self.amenities + sum(j.amenities for j in self.jobs_slots),
            "energy": self.energy + sum(j.energy for j in self.jobs_slots),
            "minerals": self.minerals + sum(j.minerals for j in self.jobs_slots),
            "food": self.food + sum(j.food for j in self.jobs_slots),
            "trade": self.trade + sum(j.trade for j in self.jobs_slots),
            "goods": self.goods + sum(j.goods for j in self.jobs_slots),
            "alloys": self.alloys + sum(j.alloys for j in self.jobs_slots),
            "unity": self.unity + sum(j.unity for j in self.jobs_slots),
            "research": (
                self.physics
                + sum(j.physics for j in self.jobs_slots)
                + self.society
                + sum(j.society for j in self.jobs_slots)
                + self.engineering
                + sum(j.engineering for j in self.jobs_slots)
            )
            / 3,
            "motes": self.motes + sum(j.motes for j in self.jobs_slots),
            "gases": self.gases + sum(j.gases for j in self.jobs_slots),
            "crystals": self.crystals + sum(j.crystals for j in self.jobs_slots),
            "admin": self.admin + sum(j.admin for j in self.jobs_slots),
            "naval": self.naval + sum(j.naval for j in self.jobs_slots),
            "jobs": len(self.jobs_slots),
        }


class SystemCapitalComplex(Building):
    def __init__(self):
        super().__init__()
        self.name = "SystemCapitalComplex"

        self.housing = 10
        self.amenities = 10
        self.energy = -10

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

        self.energy = -8
        self.motes = -2

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

        self.energy = -8
        self.gases = -2

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
        self.energy = -8
        self.crystals = -2

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
        self.energy = -8
        self.crystals = -2

        self.culture_workers = 8

        for c in range(self.culture_workers):
            self.jobs_slots.append(jobs.CultureWorker())


class SacredNexus(Building):
    def __init__(self):
        super().__init__()
        self.name = "SacredNexus"
        self.energy = -8
        self.crystals = -2

        self.priests = 8

        for c in range(self.priests):
            self.jobs_slots.append(jobs.Priest())


class SynergyForum(Building):
    def __init__(self):
        super().__init__()
        self.name = "SynergyForum"
        self.energy = -8
        self.crystals = -2

        self.managers = 8

        for c in range(self.managers):
            self.jobs_slots.append(jobs.Manager())


class ConfluenceOfThought(Building):
    def __init__(self):
        super().__init__()
        self.name = "ConfluenceOfThought"
        self.energy = -8
        self.gases = -2

        self.synapse_drones = 8

        for c in range(self.synapse_drones):
            self.jobs_slots.append(jobs.SynapseDrone())


class SimulationComplex(Building):
    def __init__(self):
        super().__init__()
        self.name = "SimulationComplex"
        self.energy = -8
        self.crystals = -2

        self.evaluators = 8

        for c in range(self.evaluators):
            self.jobs_slots.append(jobs.Evaluator())


class HyperEntertainmentForums(Building):
    def __init__(self):
        super().__init__()
        self.name = "HyperEntertainmentForums"
        self.energy = -5
        self.gases = -1

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
        self.energy = -5
        self.crystals = -1

        self.bureaucrats = 5

        for c in range(self.bureaucrats):
            self.jobs_slots.append(jobs.Bureaucrat())


class SystemConflux(Building):
    def __init__(self):
        super().__init__()
        self.name = "SystemConflux"
        self.energy = -8
        self.crystals = -2

        self.coordinators = 8

        for c in range(self.coordinators):
            self.jobs_slots.append(jobs.Coordinator())


class HallOfJudgement(Building):
    def __init__(self):
        super().__init__()
        self.name = "HallOfJudgement"
        self.energy = -5
        self.gases = -1

        self.enforcers = 5

        for c in range(self.enforcers):
            self.jobs_slots.append(jobs.Enforcer())


class SentinelPosts(Building):
    def __init__(self):
        super().__init__()
        self.name = "SentinelPosts"
        self.energy = -2

        self.hunter_seeker_drones = 2

        for c in range(self.hunter_seeker_drones):
            self.jobs_slots.append(jobs.HunterSeekerDrone())


class HydroponicsFarms(Building):
    def __init__(self):
        super().__init__()
        self.name = "HydroponicsFarms"
        self.energy = -2

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
        self.energy = -5
        self.crystals = -1

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
        self.energy = -3

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
        self.energy = -3

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
        self.energy = -3

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
        self.housing = 6
        self.amenities = 10
        self.energy = -3
        self.crystals = -1


class UtopianCommunalHousing(Building):
    def __init__(self):
        super().__init__()
        self.name = "UtopianCommunalHousing"
        self.housing = 10
        self.amenities = 6
        self.energy = -3
        self.crystals = -1


class ExpandedWarren(Building):
    def __init__(self):
        super().__init__()
        self.name = "ExpandedWarren"
        self.housing = 6
        self.amenities = 10
        self.energy = -3
        self.crystals = -1


class UpgradedDroneStorage(Building):
    def __init__(self):
        super().__init__()
        self.name = "UpgradedDroneStorage"
        self.housing = 8
        self.amenities = 6
        self.energy = -3
        self.crystals = -1


class OrganicParadise(Building):
    def __init__(self):
        super().__init__()
        self.name = "OrganicParadise"
        self.energy = -5
        self.gases = -1

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
        self.housing = 3
        self.energy = -1
        self.motes = -1

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
        self.energy = 10

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
        self.energy = -1

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
        self.energy = -1

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
        self.energy = -1

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
        self.energy = -1

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
        self.energy = -1

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
        self.energy = 20
        self.food = -25


# class NaniteTransmuter(Building):
#     def __init__(self):
#         super().__init__()
# self.name = "NaniteTransmuter"
#         self.energy = -5
#         self.food = 0
#         self.motes = 2
#         self.gases = 2
#         self.crystals = 2
#         self.nanites = -1


class SlaveHuts(Building):
    def __init__(self):
        super().__init__()
        self.name = "SlaveHuts"
        self.housing = 8
        self.energy = -1
        self.food = 0


class OverseerResidences(Building):
    def __init__(self):
        super().__init__()
        self.name = "OverseerResidences"
        self.housing = 2
        self.energy = -1
        self.food = 0

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
        self.energy = -5


class MilitaryAcademy(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "MilitaryAcademy"
        self.energy = -2

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
        self.energy = -2
        self.gases = -1

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
        self.energy = -2
        self.motes = -1

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
        self.energy = -2
        self.motes = -1

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
        self.energy = -5
        self.crystals = -1


class CitadelOfFaith(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "CitadelOfFaith"
        self.energy = -5
        self.crystals = -1

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
        self.energy = -5
        self.crystals = -1


class AlphaHub(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "AlphaHub"
        self.energy = -5
        self.crystals = -1


class ResearchInstitute(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "ResearchInstitute"
        self.energy = -5
        self.gases = -1

        self.science_directors = 1
        for j in range(self.science_directors):
            self.jobs_slots.append(jobs.ScienceDirector())


class PlanetarySupercomputer(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "PlanetarySupercomputer"
        self.energy = -5
        self.gases = -1

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
        self.energy = -5
        self.motes = -1

        self.administrators = 1
        for j in range(self.administrators):
            self.jobs_slots.append(jobs.Administrator())


class ResourceProcessingCenter(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "ResourceProcessingCenter"
        self.energy = -5
        self.motes = -1

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
        self.energy = -5
        self.gases = -1

        self.medical_workers = 5
        for j in range(self.medical_workers):
            self.jobs_slots.append(jobs.MedicalWorker())


class SpawningPools(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "SpawningPools"
        self.energy = -2

        self.spawning_drones = 1
        for j in range(self.spawning_drones):
            self.jobs_slots.append(jobs.SpawningDrone())


class RobotAssemblyPlants(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "RobotAssemblyPlants"
        self.energy = -5

        self.roboticists = 1
        for j in range(self.roboticists):
            self.jobs_slots.append(jobs.Roboticist())


class MachineAssemblyComplex(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "MachineAssemblyComplex"
        self.energy = -8
        self.crystals = -2

        self.replicators = 3
        for j in range(self.replicators):
            self.jobs_slots.append(jobs.Replicator())


class GalacticStockExchange(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "GalacticStockExchange"
        self.energy = -5
        self.crystals = -1

        self.merchants = 2
        for j in range(self.merchants):
            self.jobs_slots.append(jobs.Merchant())


class NobleEstates(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "NobleEstates"
        self.energy = -2

        self.nobles = 1
        for j in range(self.nobles):
            self.jobs_slots.append(jobs.Noble())


class SlaveProcessingFacility(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "SlaveProcessingFacility"
        self.energy = -2


class CloneVats(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "CloneVats"
        self.energy = -2


class PsiCorps(UniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "PsiCorps"
        self.energy = -5

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
        self.energy = -8
        self.crystals = -2


class OmegaAlignment(EmpireUniqueBuilding):
    def __init__(self):
        super().__init__()
        self.name = "OmegaAlignment"
        self.energy = -8
        self.physics = 16
