import jobs


class Building(object):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = 0
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []


class SystemCapitalComplex(Building):
    def __init__(self):
        self.housing = 10
        self.amenities = 10
        self.energy = -10
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

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
        if "synthetic_evolution" in modifiers.ascension_perks:
            self.roboticists += 3

        for c in range(self.administrators):
            self.jobs.append(jobs.Administrator)
        for c in range(self.enforcers):
            self.jobs.append(jobs.Enforcer)
        for c in range(self.nobles):
            self.jobs.append(jobs.Noble)
        for c in range(self.high_priests):
            self.jobs.append(jobs.HighPriests)
        for c in range(self.merchants):
            self.jobs.append(jobs.Merchant)
        for c in range(self.science_directors):
            self.jobs.append(jobs.ScienceDirector)
        for c in range(self.executives):
            self.jobs.append(jobs.Executive)
        for c in range(self.roboticists):
            self.jobs.append(jobs.Roboticist)


class AlloyNanoPlants(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = -2
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

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
            self.jobs.append(jobs.Metallurgist)
        for c in range(self.foundry_drone):
            self.jobs.append(jobs.FoundryDrone)
        for c in range(self.fabricator):
            self.jobs.append(jobs.Fabricator)


class AdvancedResearchComplexes(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -2
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

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
            self.jobs.append(jobs.Researcher)
        for c in range(self.brain_drone):
            self.jobs.append(jobs.BrainDrone)
        for c in range(self.calculators):
            self.jobs.append(jobs.Calculator)


class CivilianRepliComplexes(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.artisans = 8
        self.artisan_drones = 0

        if "rogue_servitor" in modifiers.civics:
            self.artisans = 0
            self.artisan_drones = 8

        for c in range(self.artisans):
            self.jobs.append(jobs.Artisan)
        for c in range(self.artisan_drones):
            self.jobs.append(jobs.ArtisanDrone)


class HypercommsForum(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.culture_workers = 8

        for c in range(self.culture_workers):
            self.jobs.append(jobs.CultureWorker)


class SacredNexus(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.priests = 8

        for c in range(self.priests):
            self.jobs.append(jobs.Priest)


class SynergyForum(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.managers = 8

        for c in range(self.managers):
            self.jobs.append(jobs.Manager)


class ConfluenceOfThought(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -2
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.synapse_drones = 8

        for c in range(self.synapse_drones):
            self.jobs.append(jobs.SynapseDrone)


class SimulationComplex(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.evaluators = 8

        for c in range(self.evaluators):
            self.jobs.append(jobs.Evaluator)


class HyperEntertainmentForums(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -1
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.entertainers = 5
        self.duelists = 0

        if "warrior_culture" in modifiers.ethics:
            self.entertainers = 0
            self.duelists = 5

        for c in range(self.entertainers):
            self.jobs.append(jobs.Entertainer)
        for c in range(self.duelists):
            self.jobs.append(jobs.Duelists)


class AdministrativePark(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.bureaucrats = 5

        for c in range(self.bureaucrats):
            self.jobs.append(jobs.Bureaucrat)


class SystemConflux(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.coordinators = 8

        for c in range(self.coordinators):
            self.jobs.append(jobs.Coordinator)


class HallOfJudgement(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -1
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.enforcers = 5

        for c in range(self.enforcers):
            self.jobs.append(jobs.Enforcer)


class SentinelPosts(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.hunter_seeker_drones = 2

        for c in range(self.hunter_seeker_drones):
            self.jobs.append(jobs.HunterSeekerDrone)
class HydroponicsFarms(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.farmers = 2
        self.agri_drones = 0

        if "hive_mind" in modifiers.authority:
            self.farmers = 0
            self.agri_drones = 2

        for c in range(self.farmers):
            self.jobs.append(jobs.Farmer)
        for c in range(self.agri_drones):
            self.jobs.append(jobs.AgriDrone)
class CommerceMegaplexes(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.clerks = 10
        self.merchants = 1

        for c in range(self.clerks):
            self.jobs.append(jobs.Clerk)
        for c in range(self.merchants):
            self.jobs.append(jobs.Merchant)
class ChemicalPlants(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -3
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.chemists = 1
        self.chem_drones = 0

        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.chemists = 0
            self.chem_drones = 1

        for j in range(self.chemists):
            self.jobs.append(jobs.Chemist)
        for j in range(self.chem_drones):
            self.jobs.append(jobs.ChemDrone)
class ExoticGasRefineries(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -3
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.gas_refiners = 1
        self.refinery_drones = 0

        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.gas_refiners = 0
            self.refinery_drones = 1

        for j in range(self.gas_refiners):
            self.jobs.append(jobs.GasRefiner)
        for j in range(self.refinery_drones):
            self.jobs.append(jobs.RefineryDrone)
class SyntheticCrystalPlants(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -3
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.translucers  = 1
        self.lensing_drones = 0

        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.translucers = 0
            self.lensing_drones = 1

        for j in range(self.translucers):
            self.jobs.append(jobs.Translucer)
        for j in range(self.lensing_drones):
            self.jobs.append(jobs.LensingDrone)
class ParadiseDome(Building):
    def __init__(self):
        self.housing = 6
        self.amenities = 10
        self.energy = -3
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class UtopianCommunalHousing(Building):
    def __init__(self):
        self.housing = 10
        self.amenities = 6
        self.energy = -3
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class ExpandedWarren(Building):
    def __init__(self):
        self.housing = 6
        self.amenities = 10
        self.energy = -3
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class UpgradedDroneStorage(Building):
    def __init__(self):
        self.housing = 8
        self.amenities = 6
        self.energy = -3
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class OrganicParadise(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -1
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.bio_trophies = 1
        self.maintenance_drones = 0

        for j in range(self.bio_trophies):
            self.jobs.append(jobs.BioTrophy)
        for j in range(self.maintenance_drones):
            self.jobs.append(jobs.MaintenanceDrone)
class Fortress(Building):
    def __init__(self):
        self.housing = 3
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = -1
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.soldiers = 3
        self.warrior_drones = 0
        
        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.soldiers = 0
            self.warrior_drones = 3

        for j in range(self.soldiers):
            self.jobs.append(jobs.Soldier)
        for j in range(self.warrior_drones):
            self.jobs.append(jobs.WarriorDrone)
class BetharianPowerPlant(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = 10
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.technicians = 4
        self.tech_drones = 0
        
        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.technicians = 0
            self.tech_drones = 4

        for j in range(self.technicians):
            self.jobs.append(jobs.Technician)
        for j in range(self.tech_drones):
            self.jobs.append(jobs.TechDrone)
class AlienZoo(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.culture_workers = 2
        self.entertainers = 1
        self.duelists = 0
        
        if "warrior_culture" in modifiers.civics:
            self.culture_workers = 2
            self.entertainers -=1
            self.duelists = 1

        for j in range(self.culture_workers):
            self.jobs.append(jobs.CultureWorker)
        for j in range(self.entertainers):
            self.jobs.append(jobs.Entertainer)
        for j in range(self.duelists):
            self.jobs.append(jobs.Duelist)
class CrystalMines(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.crystal_miners = 1
        self.crystal_mining_drones = 0
        
        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.crystal_miners = 0
            self.crystal_mining_drones = 1

        for j in range(self.crystal_miners):
            self.jobs.append(jobs.CrystalMiner)
        for j in range(self.crystal_mining_drones):
            self.jobs.append(jobs.CrystalMiningDrone)
class GasExtractionWells(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.gas_extractors = 1
        self.gas_extraction_drones = 0
        
        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.gas_extractors = 0
            self.gas_extraction_drones = 1

        for j in range(self.gas_extractors):
            self.jobs.append(jobs.GasExtractor)
        for j in range(self.gas_extraction_drones):
            self.jobs.append(jobs.GasExtractionDrone)
class MoteHarvestingTraps(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.mote_harvesters = 1
        self.mote_harvesting_drones = 0
        
        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.mote_harvesters = 0
            self.mote_harvesting_drones = 1

        for j in range(self.mote_harvesters):
            self.jobs.append(jobs.MoteHarvester)
        for j in range(self.mote_harvesting_drones):
            self.jobs.append(jobs.MoteHarvestingDrone)
class ResourceSilos(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
        
        self.clerks = 2
        self.maintenance_drones = 0
        
        if "gestalt_consciousness" in modifiers.ethics:
            self.clerks = 0
            self.maintenance_drones = 1

        for j in range(self.clerks):
            self.jobs.append(jobs.Clerk)
        for j in range(self.maintenance_drones):
            self.jobs.append(jobs.MaintenanceDrone)
class BioReactor(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = 20
        self.minerals = 0
        self.food = -25
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class NaniteTransmuter(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food =0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =2
        self.gases = 2
        self.crystals = 2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = -1
        self.admin = 0
        self.naval = 0
        self.jobs = []
class SlaveHuts(Building):
    def __init__(self):
        self.housing = 8
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food =0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class OverseerResidences(Building):
    def __init__(self):
        self.housing = 2
        self.amenities = 0
        self.energy = -1
        self.minerals = 0
        self.food =0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes =0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.slave_overseers = 2

        for j in range(self.slave_overseers):
            self.jobs.append(jobs.SlaveOverseer)
class UniqueBuilding(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = 0
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class PlanetaryShieldGenerator(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class MilitaryAcademy(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.soldiers = 1
        self.warrior_drones = 0

        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.soldiers = 0
            self.warrior_drones = 1

        for c in range(self.soldiers):
            self.jobs.append(jobs.Soldier )
        for c in range(self.warrior_drones):
            self.jobs.append(jobs.WarriorDrones)
class EnergyNexus(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -1
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.technicians = 2
        self.tech_drones = 0

        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.technicians = 0
            self.tech_drones = 2

        for j in range(self.technicians):
            self.jobs.append(jobs.Technician)
        for j in range(self.warrior_drones):
            self.jobs.append(jobs.TechDrone)
class MineralPurificationHubs(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = -1
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.miners = 2
        self.mining_drones = 0

        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.miners = 0
            self.mining_drones = 2

        for j in range(self.miners):
            self.jobs.append(jobs.Miner)
        for j in range(self.warrior_drones):
            self.jobs.append(jobs.WarriorDrone)
class FoodProcessingCenters(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = -1
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.farmers = 2
        self.agri_drones = 0

        if "hive_mind" in modifiers.authority or "machine_intelligence" in modifiers.authority:
            self.farmers = 0
            self.agri_drones = 2

        for j in range(self.farmers):
            self.jobs.append(jobs.Farmer)
        for j in range(self.agri_drones):
            self.jobs.append(jobs.AgriDrone)
class AutoCuratingVault(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class CitadelOfFaith(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.priests = 5
        self.high_priests = 1

        for j in range(self.priests):
            self.jobs.append(jobs.Priest)
        for j in range(self.high_priests):
            self.jobs.append(jobs.HighPriest)
class VaultOfAcquisitions(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class AlphaHub(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class ResearchInstitute(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -1
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.science_directors = 1

        for j in range(self.science_directors):
            self.jobs.append(jobs.ScienceDirector)
class PlanetarySupercomputer(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -1
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

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
            self.jobs.append(jobs.ScienceDirector)
        for j in range(self.brain_drones):
            self.jobs.append(jobs.BrainDrone)
        for j in range(self.calculators):
            self.jobs.append(jobs.Calculator)
class MinistryOfProduction(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = -1
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.administrators = 1

        for j in range(self.administrators):
            self.jobs.append(jobs.Administrator)
class ResourceProcessingCenter(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = -1
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.foundry_drones = 2
        self.fabricators = 0

        if "hive_mind" in modifiers.authority:
            self.foundry_drones = 2
            self.fabricators = 0
        if "machine_intelligence" in modifiers.authority:
            self.foundry_drones = 0
            self.fabricators = 1

        for j in range(self.foundry_drones):
            self.jobs.append(jobs.FoundryDrone)
        for j in range(self.fabricators):
            self.jobs.append(jobs.Fabricator)
class CytoRevitalizationCenter(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = -1
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.medical_workers = 5

        for j in range(self.medical_workers):
            self.jobs.append(jobs.MedicalWorker)
class SpawningPools(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.spawning_drones = 1

        for j in range(self.spawning_drones):
            self.jobs.append(jobs.SpawningDrone)
class RobotAssemblyPlants(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.roboticists = 1

        for j in range(self.roboticists):
            self.jobs.append(jobs.Roboticist)
class MachineAssemblyComplex(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.replicators = 3

        for j in range(self.replicators):
            self.jobs.append(jobs.Replicator)
class GalacticStockExchange(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -1
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.merchants = 2

        for j in range(self.merchants):
            self.jobs.append(jobs.Merchant)
class NobleEstates(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.nobles = 1

        for j in range(self.nobles):
            self.jobs.append(jobs.Noble)
class SlaveProcessingFacility(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class CloneVats(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -2
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class PsiCorps(UniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -5
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []

        self.telepaths = 2

        for j in range(self.telepaths):
            self.jobs.append(jobs.Telepath)
class EmpireUniqueBuilding(Building):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = 0
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class GrandEmbassyComplex(EmpireUniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = -2
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []
class OmegaAlignment(EmpireUniqueBuilding):
    def __init__(self):
        self.housing = 0
        self.amenities = 0
        self.energy = -8
        self.minerals = 0
        self.food = 0
        self.trade = 0
        self.goods = 0
        self.alloys = 0
        self.influence = 0
        self.unity = 0
        self.physics = 16
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.metals = 0
        self.zro = 0
        self.matter = 0
        self.nanites = 0
        self.admin = 0
        self.naval = 0
        self.jobs = []