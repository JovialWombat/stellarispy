import modifiers


class Job(object):
    def __init__(self):
        self.housing = -1
        self.amenities = -1
        self.energy = 0
        self.minerals = 0
        self.food = -1
        self.trade = 1
        self.goods = -1
        self.alloys = 0
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0  
        self.crystals = 0
        self.admin = -0.5
        self.naval = 0

class Ruler(Job):
    def __init__(self):
        super().__init__()
        self.trade = 0.4
        self.goods = -1

class Specialist(Job):
    def __init__(self):
        super().__init__()
        self.trade = 0.25
        self.goods = -0.5

class Worker(Job):
    def __init__(self):
        super().__init__()
        self.trade = 0.15
        self.goods = -0.25

class Administrator(Ruler):
    def __init__(self):
        super().__init__()
        self.unity += 3
        self.amenities += 8


class Executive(Ruler):
    def __init__(self):
        super().__init__()
        self.unity += 2
        self.amenities += 5
        self.trade += 4


class HighPriest(Ruler):
    def __init__(self):
        super().__init__()
        self.unity += 5
        self.amenities += 5
        self.society += 2
        if "exalted_priesthood" in modifiers.civics:
            self.unity += 1


class Merchant(Ruler):
    def __init__(self):
        super().__init__()
        self.amenities += 5
        self.trade += 8
        if "merchant_guilds" in modifiers.civics:
            self.unity += 2


class Noble(Ruler):
    def __init__(self):
        super().__init__()
        self.unity += 3


class ScienceDirector(Ruler):
    def __init__(self):
        super().__init__()
        self.amenities += 5
        self.physics += 5
        self.society += 5
        self.engineering += 5


class Metallurgist(Specialist):
    def __init__(self):
        super().__init__()
        self.alloys += 3
        self.minerals -= 6


class Artisan(Specialist):
    def __init__(self):
        super().__init__()
        self.goods += 6
        self.minerals -= 6


class Chemist(Specialist):
    def __init__(self):
        super().__init__()
        self.motes += 2
        self.minerals -= 10


class GasRefiner(Specialist):
    def __init__(self):
        super().__init__()
        self.gases += 2
        self.minerals -= 10


class Translucer(Specialist):
    def __init__(self):
        super().__init__()
        self.crystals += 2
        self.minerals -= 10


class Researcher(Specialist):
    def __init__(self):
        super().__init__()
        self.physics += 4
        self.society += 4
        self.engineering += 4
        self.goods -= 2
        if "technocracy" in modifiers.civics:
            self.unity += 1


class CultureWorker(Specialist):
    def __init__(self):
        super().__init__()
        self.society += 3
        self.unity += 3
        self.goods -= 2


class Priest(Specialist):
    def __init__(self):
        super().__init__()
        self.society += 2
        self.unity += 3
        self.amenities += 5
        self.goods -= 2
        if "exalted_priesthood" in modifiers.civics:
            self.unity += 1


class Manager(Specialist):
    def __init__(self):
        super().__init__()
        self.society += 2
        self.unity += 3
        self.trade += 2
        self.goods -= 2


class Enforcer(Specialist):
    def __init__(self):
        super().__init__()
        self.unity += 1
        if "police_state" in modifiers.civics:
            self.unity += 1


class Telepath(Specialist):
    def __init__(self):
        super().__init__()
        self.unity += 3
        self.energy -= 1
        if "police_state" in modifiers.civics:
            self.unity += 1


class Entertainer(Specialist):
    def __init__(self):
        super().__init__()
        self.unity += 2
        self.amenities += 10
        self.goods -= 1


class Duelist(Specialist):
    def __init__(self):
        super().__init__()
        self.unity += 3
        self.amenities += 12
        self.naval += 2
        self.alloys -= 1


class MedicalWorker(Specialist):
    def __init__(self):
        super().__init__()
        self.amenities += 5
        self.goods -= 1


class Roboticist(Specialist):
    def __init__(self):
        super().__init__()
        self.alloys -= 2


class Bureaucrat(Specialist):
    def __init__(self):
        super().__init__()
        self.admin += 10
        if "byzantine_bureaucracy" in modifiers.civics:
            self.unity += 1


class Technician(Worker):
    def __init__(self):
        super().__init__()
        self.energy += 4
        if "synthetic_evolution" in modifiers.perks:
            self.energy += 2


class Miner(Worker):
    def __init__(self):
        super().__init__()
        self.minerals += 4
        if "mining_guilds" in modifiers.civics:
            self.minerals += 1


class Farmer(Worker):
    def __init__(self):
        super().__init__()
        self.food += 6
        if "synthetic_evolution" in modifiers.perks:
            self.food -= 1
        if "agrarian_idyll" in modifiers.civics:
            self.amenities += 2


class CrystalMiner(Worker):
    def __init__(self):
        super().__init__()
        self.crystals += 2


class MoteHarvester(Worker):
    def __init__(self):
        super().__init__()
        self.motes += 2


class GasExtractor(Worker):
    def __init__(self):
        super().__init__()
        self.gases += 2


class Clerk(Worker):
    def __init__(self):
        super().__init__()
        self.trade += 2
        self.amenities += 2


class ProsperityPreacher(Worker):
    def __init__(self):
        super().__init__()
        self.unity += 1
        self.trade += 3
        self.amenities += 3


class Soldier(Worker):
    def __init__(self):
        super().__init__()
        self.naval += 4
        if "citizen_service" in modifiers.civics:
            self.unity += 2


class FoundryDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.alloys += 3
        self.minerals -= 6


class Fabricator(Specialist):
    def __init__(self):
        super().__init__()
        self.alloys += 4
        self.minerals -= 8


class ArtisanDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.goods += 8
        self.minerals -= 8


class ChemDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.motes += 2
        self.minerals -= 10


class RefineryDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.gases += 2
        self.minerals -= 10


class LensingDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.crystals += 2
        self.minerals -= 10


class CrystalMiningDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.crystals += 2
        self.energy -= 1


class GasExtractionDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.gases += 2
        self.energy -= 1


class MoteHarvestingDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.motes += 2
        self.energy -= 1


class BrainDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.physics += 4
        self.society += 4
        self.engineering += 4
        self.minerals -= 6


class Calculator(Specialist):
    def __init__(self):
        super().__init__()
        self.physics += 4
        self.society += 4
        self.engineering += 4
        self.energy -= 4


class Evaluator(Specialist):
    def __init__(self):
        super().__init__()
        self.unity += 4
        self.energy -= 1


class SynapseDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.unity += 3
        self.admin += 5
        if "instinctive_synchronisation" in modifiers.traditions:
            self.amenities += 2


class HunterSeekerDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.unity += 1


class SpawningDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.amenities += 5
        self.food -= 5


class Replicator(Specialist):
    def __init__(self):
        super().__init__()
        self.alloys -= 1


class Coordinator(Specialist):
    def __init__(self):
        super().__init__()
        self.admin += 15
        self.energy -= 4
        if "integrated_preservation" in modifiers.traditions:
            self.admin += 3


class TechDrone(Worker):
    def __init__(self):
        super().__init__()
        self.energy += 4
        if "machine_intelligence" in modifiers.civics:
            self.energy += 2


class MiningDrone(Worker):
    def __init__(self):
        super().__init__()
        self.minerals += 4
        if "rockbreakers" in modifiers.civics:
            self.energy += 1


class AgriDrone(Worker):
    def __init__(self):
        super().__init__()
        self.food += 6
        if "machine_intelligence" in modifiers.civics:
            self.food -= 1


class MaintenanceDrone(Worker):
    def __init__(self):
        super().__init__()
        self.amenities += 4
        if "maintenance_protocols" in modifiers.civics:
            self.unity += 1


class WarriorDrone(Worker):
    def __init__(self):
        super().__init__()
        self.naval += 4


class BioTrophy(Worker):
    def __init__(self):
        super().__init__()
        self.unity += 2
        self.housing += 1


class SlaveOverseer(Worker):
    def __init__(self):
        super().__init__()
