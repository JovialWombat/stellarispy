import modifiers


class Job(object):
    def __init__(self):
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
            "jobs": 0,
        }
        self.upkeep = {
            "housing": -1,
            "amenities": -1,


            "energy": 0,
            # machines
            # "energy": -1,
            
            "minerals": 0,
            # lithoids
            "minerals": -1,

            # humanoids  
            # "food": -1,
            # lithoids & machines
            "food": 0,

            "trade": 0,

            "goods": -1,
            # gestalt consciousness
            # "goods": 0,

            "alloys": 0,
            "unity": 0,
            "physics": 0,
            "society": 0,
            "engineering": 0,
            "motes": 0,
            "gases": 0,
            "crystals": 0,
            "admin": -0.5,
            "naval": 0,
            "storage": 0,
            "jobs": 0,
        }

        self.production_coefficients = {
            "housing": 1.0,
            "amenities": 1.0,
            "energy": 1.0,
            "minerals": 1.0,
            "food": 1.0,
            "trade": 1.0,
            "goods": 1.0,
            "alloys": 1.0,
            "unity": 1.0,
            "physics": 1.0,
            "society": 1.0,
            "engineering": 1.0,
            "motes": 1.0,
            "gases": 1.0,
            "crystals": 1.0,
            "admin": 1.0,
            "naval": 1.0,
            "storage": 1.0,
            "jobs": 1.0,
        }
        self.production_constants = {
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
            "jobs": 0,
        }
        self.upkeep_coefficients = {
            "housing": 1.0,
            "amenities": 1.0,
            "energy": 1.0,
            "minerals": 1.0,
            "food": 1.0,
            "trade": 1.0,
            "goods": 1.0,
            "alloys": 1.0,
            "unity": 1.0,
            "physics": 1.0,
            "society": 1.0,
            "engineering": 1.0,
            "motes": 1.0,
            "gases": 1.0,
            "crystals": 1.0,
            "admin": 1.0,
            "naval": 1.0,
            "storage": 1.0,
            "jobs": 1.0,
        }
        self.upkeep_constants = {
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
            "jobs": 0,
        }


class Ruler(Job):
    def __init__(self):
        super().__init__()
        self.production["trade"] = 0.4
        self.upkeep["goods"] = -1


class Specialist(Job):
    def __init__(self):
        super().__init__()
        self.production["trade"] = 0.25
        self.upkeep["goods"] = -0.5


class Worker(Job):
    def __init__(self):
        super().__init__()
        self.production["trade"] = 0.15
        self.upkeep["goods"] = -0.25


class Administrator(Ruler):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 3
        self.production["amenities"] += 8


class Executive(Ruler):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 2
        self.production["amenities"] += 5
        self.production["trade"] += 4


class HighPriest(Ruler):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 5
        self.production["amenities"] += 5
        self.production["society"] += 2
        if "exalted_priesthood" in modifiers.civics:
            self.production["unity"] += 1


class Merchant(Ruler):
    def __init__(self):
        super().__init__()
        self.production["amenities"] += 5
        self.production["trade"] += 8
        if "merchant_guilds" in modifiers.civics:
            self.production["unity"] += 2


class Noble(Ruler):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 3


class ScienceDirector(Ruler):
    def __init__(self):
        super().__init__()
        self.production["amenities"] += 5
        self.production["physics"] += 5
        self.production["society"] += 5
        self.production["engineering"] += 5


class Metallurgist(Specialist):
    def __init__(self):
        super().__init__()
        self.production["alloys"] += 3
        self.upkeep["minerals"] -= 6


class Artisan(Specialist):
    def __init__(self):
        super().__init__()
        self.production["goods"] += 6
        self.upkeep["minerals"] -= 6


class Chemist(Specialist):
    def __init__(self):
        super().__init__()
        self.production["motes"] += 2
        self.upkeep["minerals"] -= 10


class GasRefiner(Specialist):
    def __init__(self):
        super().__init__()
        self.production["gases"] += 2
        self.upkeep["minerals"] -= 10


class Translucer(Specialist):
    def __init__(self):
        super().__init__()
        self.production["crystals"] += 2
        self.upkeep["minerals"] -= 10


class Researcher(Specialist):
    def __init__(self):
        super().__init__()
        self.production["physics"] += 4
        self.production["society"] += 4
        self.production["engineering"] += 4
        self.upkeep["goods"] -= 2
        if "technocracy" in modifiers.civics:
            self.production["unity"] += 1


class CultureWorker(Specialist):
    def __init__(self):
        super().__init__()
        self.production["society"] += 3
        self.production["unity"] += 3
        self.upkeep["goods"] -= 2


class Priest(Specialist):
    def __init__(self):
        super().__init__()
        self.production["society"] += 2
        self.production["unity"] += 3
        self.production["amenities"] += 5
        self.upkeep["goods"] -= 2
        if "exalted_priesthood" in modifiers.civics:
            self.production["unity"] += 1


class Manager(Specialist):
    def __init__(self):
        super().__init__()
        self.production["society"] += 2
        self.production["unity"] += 3
        self.production["trade"] += 2
        self.upkeep["goods"] -= 2


class Enforcer(Specialist):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 1
        if "police_state" in modifiers.civics:
            self.production["unity"] += 1


class Telepath(Specialist):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 3
        self.upkeep["energy"] -= 1
        if "police_state" in modifiers.civics:
            self.production["unity"] += 1


class Entertainer(Specialist):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 2
        self.production["amenities"] += 10
        self.upkeep["goods"] -= 1


class Duelist(Specialist):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 3
        self.production["amenities"] += 12
        self.production["naval"] += 2
        self.upkeep["alloys"] -= 1


class MedicalWorker(Specialist):
    def __init__(self):
        super().__init__()
        self.production["amenities"] += 5
        self.upkeep["goods"] -= 1


class Roboticist(Specialist):
    def __init__(self):
        super().__init__()
        self.upkeep["alloys"] -= 2


class Bureaucrat(Specialist):
    def __init__(self):
        super().__init__()
        self.production["admin"] += 10
        if "byzantine_bureaucracy" in modifiers.civics:
            self.production["unity"] += 1


class Technician(Worker):
    def __init__(self):
        super().__init__()
        self.production["energy"] += 4
        if "synthetic_evolution" in modifiers.perks:
            self.production["energy"] += 2


class Miner(Worker):
    def __init__(self):
        super().__init__()
        self.production["minerals"] += 4
        if "mining_guilds" in modifiers.civics:
            self.production["minerals"] += 1


class Farmer(Worker):
    def __init__(self):
        super().__init__()
        self.production["food"] += 6
        if "synthetic_evolution" in modifiers.perks:
            self.upkeep["food"] -= 1
        if "agrarian_idyll" in modifiers.civics:
            self.production["amenities"] += 2


class CrystalMiner(Worker):
    def __init__(self):
        super().__init__()
        self.production["crystals"] += 2


class MoteHarvester(Worker):
    def __init__(self):
        super().__init__()
        self.production["motes"] += 2


class GasExtractor(Worker):
    def __init__(self):
        super().__init__()
        self.production["gases"] += 2


class Clerk(Worker):
    def __init__(self):
        super().__init__()
        self.production["trade"] += 2
        self.production["amenities"] += 2


class ProsperityPreacher(Worker):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 1
        self.production["trade"] += 3
        self.production["amenities"] += 3


class Soldier(Worker):
    def __init__(self):
        super().__init__()
        self.production["naval"] += 4
        if "citizen_service" in modifiers.civics:
            self.production["unity"] += 2


class FoundryDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["alloys"] += 3
        self.upkeep["minerals"] -= 6


class Fabricator(Specialist):
    def __init__(self):
        super().__init__()
        self.production["alloys"] += 4
        self.upkeep["minerals"] -= 8


class ArtisanDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["goods"] += 8
        self.upkeep["minerals"] -= 8


class ChemDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["motes"] += 2
        self.upkeep["minerals"] -= 10


class RefineryDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["gases"] += 2
        self.upkeep["minerals"] -= 10


class LensingDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["crystals"] += 2
        self.upkeep["minerals"] -= 10


class CrystalMiningDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["crystals"] += 2
        self.upkeep["energy"] -= 1


class GasExtractionDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["gases"] += 2
        self.upkeep["energy"] -= 1


class MoteHarvestingDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["motes"] += 2
        self.upkeep["energy"] -= 1


class BrainDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["physics"] += 4
        self.production["society"] += 4
        self.production["engineering"] += 4
        self.upkeep["minerals"] -= 6


class Calculator(Specialist):
    def __init__(self):
        super().__init__()
        self.production["physics"] += 4
        self.production["society"] += 4
        self.production["engineering"] += 4
        self.upkeep["energy"] -= 4


class Evaluator(Specialist):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 4
        self.upkeep["energy"] -= 1


class SynapseDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 3
        self.production["admin"] += 5
        if "instinctive_synchronisation" in modifiers.traditions:
            self.production["amenities"] += 2


class HunterSeekerDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 1


class SpawningDrone(Specialist):
    def __init__(self):
        super().__init__()
        self.production["amenities"] += 5
        self.upkeep["food"] -= 5


class Replicator(Specialist):
    def __init__(self):
        super().__init__()
        self.upkeep["alloys"] -= 1


class Coordinator(Specialist):
    def __init__(self):
        super().__init__()
        self.production["admin"] += 15
        self.upkeep["energy"] -= 4
        if "integrated_preservation" in modifiers.traditions:
            self.production["admin"] += 3


class TechDrone(Worker):
    def __init__(self):
        super().__init__()
        self.production["energy"] += 4
        if "machine_intelligence" in modifiers.civics:
            self.production["energy"] += 2


class MiningDrone(Worker):
    def __init__(self):
        super().__init__()
        self.production["minerals"] += 4
        if "rockbreakers" in modifiers.civics:
            self.production["energy"] += 1


class AgriDrone(Worker):
    def __init__(self):
        super().__init__()
        self.production["food"] += 6
        if "machine_intelligence" in modifiers.civics:
            self.upkeep["food"] -= 1


class MaintenanceDrone(Worker):
    def __init__(self):
        super().__init__()
        self.production["amenities"] += 4
        if "maintenance_protocols" in modifiers.civics:
            self.production["unity"] += 1


class WarriorDrone(Worker):
    def __init__(self):
        super().__init__()
        self.production["naval"] += 4


class BioTrophy(Worker):
    def __init__(self):
        super().__init__()
        self.production["unity"] += 2
        self.production["housing"] += 1


class SlaveOverseer(Worker):
    def __init__(self):
        super().__init__()
