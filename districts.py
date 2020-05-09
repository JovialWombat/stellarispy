import jobs


class District(object):
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


class CityDistrict(District):
    def __init__(self):
        self.housing = 5
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

        self.clerks = 1

        if "agrarian_idyll" in modifiers.civics:
            self.housing -= 1
        if "public_works" in modifiers.traditions:
            self.housing += 1
        if "trans_stellar_corporations" in modifiers.traditions:
            self.clerks += 1
        if "weather_control_systems" in modifiers.research:
            self.housing += 1
        if "anti_gravity_engineering" in modifiers.research:
            self.housing += 1

        for j in range(self.clerks):
            self.jobs.append(jobs.Clerk)


class HiveDistrict(District):
    def __init__(self):
        self.housing = 6
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

        self.maintenance_drones = 3

        if "hive_world" in modifiers.planet_type:
            self.housing = 12
            self.maintenance_drones = 6

        if "agrarian_idyll" in modifiers.civics:
            self.housing -= 1
        if "public_works" in modifiers.traditions:
            self.housing += 1
        # if "trans_stellar_corporations" in modifiers.traditions:
        #     self.clerks += 1
        if "weather_control_systems" in modifiers.research:
            self.housing += 1
        if "anti_gravity_engineering" in modifiers.research:
            self.housing += 1
            self.maintenance_drones += 1

        for j in range(self.maintenance_drones):
            self.jobs.append(jobs.MaintenanceDrones)


class NexusDistrict(District):
    def __init__(self):
        self.housing = 5
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

        self.maintenance_drones = 3

        if "agrarian_idyll" in modifiers.civics:
            self.housing -= 1
        if "public_works" in modifiers.traditions:
            self.housing += 1
        # if "trans_stellar_corporations" in modifiers.traditions:
        #     self.clerks += 1
        if "weather_control_systems" in modifiers.research:
            self.housing += 1
        if "anti_gravity_engineering" in modifiers.research:
            self.housing += 1
            self.maintenance_drones += 1

        for j in range(self.maintenance_drones):
            self.jobs.append(jobs.MaintenanceDrones)


class GeneratorDistrict(District):
    def __init__(self):
        self.housing = 2
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

        self.technicians = 2
        self.tech_drones = 0

        if "machine_intelligence" in modifiers.authority:
            self.housing = 3
            self.technicians = 0
            self.tech_drones = 2
        if "hive_mind" in modifiers.authority:
            self.technicians = 0
            self.tech_drones = 3
        if "agrarian_idyll" in modifiers.civics:
            self.housing = 3

        for c in range(self.technicians):
            self.jobs.append(jobs.Technician)
        for c in range(self.tech_drones):
            self.jobs.append(jobs.TechDrone)


class MiningDistrict(District):
    def __init__(self):
        self.housing = 2
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

        self.miners = 2
        self.mining_drones = 0

        if "machine_intelligence" in modifiers.authority:
            self.housing = 3
            self.miners = 0
            self.mining_drones = 2
        if "hive_mind" in modifiers.authority:
            self.miners = 0
            self.mining_drones = 3
        if "agrarian_idyll" in modifiers.civics:
            self.housing = 3

        for c in range(self.miners):
            self.jobs.append(jobs.Miner)
        for c in range(self.mining_drones):
            self.jobs.append(jobs.MiningDrone)


class AgricultureDistrict(District):
    def __init__(self):
        self.housing = 2
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

        if "machine_intelligence" in modifiers.authority:
            self.housing = 3
            self.farmers = 0
            self.agri_drones = 2
        if "hive_mind" in modifiers.authority:
            self.farmers = 0
            self.agri_drones = 3
        if "agrarian_idyll" in modifiers.civics:
            self.housing = 3
            if "agrarian_utopias" in modifiers.research:
                self.housing = 4

        for c in range(self.farmers):
            self.jobs.append(jobs.Farmer)
        for c in range(self.agri_drones):
            self.jobs.append(jobs.AgriDrones)
