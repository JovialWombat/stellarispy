import modifiers
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
        self.unity = 0
        self.physics = 0
        self.society = 0
        self.engineering = 0
        self.motes = 0
        self.gases = 0
        self.crystals = 0
        self.admin = -1
        self.naval = 0
        self.storage = 0
        self.jobs_slots = []

    def aggregate_resources(self):
        return {
            "housing": self.housing
            + sum(
                (j.production["housing"] * j.production_coefficients["housing"])
                + j.production_constants["housing"]
                + (j.upkeep["housing"] * j.upkeep_coefficients["housing"])
                + j.upkeep_constants["housing"]
                for j in self.jobs_slots
            ),
            "amenities": self.amenities
            + sum(
                (j.production["amenities"] * j.production_coefficients["amenities"])
                + j.production_constants["amenities"]
                + (j.upkeep["amenities"] * j.upkeep_coefficients["amenities"])
                + j.upkeep_constants["amenities"]
                for j in self.jobs_slots
            ),
            "energy": self.energy
            + sum(
                (j.production["energy"] * j.production_coefficients["energy"])
                + j.production_constants["energy"]
                + (j.upkeep["energy"] * j.upkeep_coefficients["energy"])
                + j.upkeep_constants["energy"]
                for j in self.jobs_slots
            ),
            "minerals": self.minerals
            + sum(
                (j.production["minerals"] * j.production_coefficients["minerals"])
                + j.production_constants["minerals"]
                + (j.upkeep["minerals"] * j.upkeep_coefficients["minerals"])
                + j.upkeep_constants["minerals"]
                for j in self.jobs_slots
            ),
            "food": self.food
            + sum(
                (j.production["food"] * j.production_coefficients["food"])
                + j.production_constants["food"]
                + (j.upkeep["food"] * j.upkeep_coefficients["food"])
                + j.upkeep_constants["food"]
                for j in self.jobs_slots
            ),
            "trade": self.trade
            + sum(
                (j.production["trade"] * j.production_coefficients["trade"])
                + j.production_constants["trade"]
                + (j.upkeep["trade"] * j.upkeep_coefficients["trade"])
                + j.upkeep_constants["trade"]
                for j in self.jobs_slots
            ),
            "goods": self.goods
            + sum(
                (j.production["goods"] * j.production_coefficients["goods"])
                + j.production_constants["goods"]
                + (j.upkeep["goods"] * j.upkeep_coefficients["goods"])
                + j.upkeep_constants["goods"]
                for j in self.jobs_slots
            ),
            "alloys": self.alloys
            + sum(
                (j.production["alloys"] * j.production_coefficients["alloys"])
                + j.production_constants["alloys"]
                + (j.upkeep["alloys"] * j.upkeep_coefficients["alloys"])
                + j.upkeep_constants["alloys"]
                for j in self.jobs_slots
            ),
            "unity": self.unity
            + sum(
                (j.production["unity"] * j.production_coefficients["unity"])
                + j.production_constants["unity"]
                + (j.upkeep["unity"] * j.upkeep_coefficients["unity"])
                + j.upkeep_constants["unity"]
                for j in self.jobs_slots
            ),
            "research": (
                self.physics
                + sum(
                    (j.production["physics"] * j.production_coefficients["physics"])
                    + j.production_constants["physics"]
                    + (j.upkeep["physics"] * j.upkeep_coefficients["physics"])
                    + j.upkeep_constants["physics"]
                    for j in self.jobs_slots
                )+
                self.society
                + sum(
                    (j.production["society"] * j.production_coefficients["society"])
                    + j.production_constants["society"]
                    + (j.upkeep["society"] * j.upkeep_coefficients["society"])
                    + j.upkeep_constants["society"]
                    for j in self.jobs_slots
                )+
                self.engineering
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
            "motes": self.motes
            + sum(
                (j.production["motes"] * j.production_coefficients["motes"])
                + j.production_constants["motes"]
                + (j.upkeep["motes"] * j.upkeep_coefficients["motes"])
                + j.upkeep_constants["motes"]
                for j in self.jobs_slots
            ),
            "gases": self.gases
            + sum(
                (j.production["gases"] * j.production_coefficients["gases"])
                + j.production_constants["gases"]
                + (j.upkeep["gases"] * j.upkeep_coefficients["gases"])
                + j.upkeep_constants["gases"]
                for j in self.jobs_slots
            ),
            "crystals": self.crystals
            + sum(
                (j.production["crystals"] * j.production_coefficients["crystals"])
                + j.production_constants["crystals"]
                + (j.upkeep["crystals"] * j.upkeep_coefficients["crystals"])
                + j.upkeep_constants["crystals"]
                for j in self.jobs_slots
            ),
            "admin": self.admin
            + sum(
                (j.production["admin"] * j.production_coefficients["admin"])
                + j.production_constants["admin"]
                + (j.upkeep["admin"] * j.upkeep_coefficients["admin"])
                + j.upkeep_constants["admin"]
                for j in self.jobs_slots
            ),
            "naval": self.naval
            + sum(
                (j.production["naval"] * j.production_coefficients["naval"])
                + j.production_constants["naval"]
                + (j.upkeep["naval"] * j.upkeep_coefficients["naval"])
                + j.upkeep_constants["naval"]
                for j in self.jobs_slots
            ),
            "storage": self.storage
            + sum(
                (j.production["storage"] * j.production_coefficients["storage"])
                + j.production_constants["storage"]
                + (j.upkeep["storage"] * j.upkeep_coefficients["storage"])
                + j.upkeep_constants["storage"]
                for j in self.jobs_slots
            ),
            "jobs": len(self.jobs_slots),
        }


class CityDistrict(District):
    def __init__(self):
        super().__init__()
        self.housing = 5
        self.energy = -2

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
            self.jobs_slots.append(jobs.Clerk())


class HiveDistrict(District):
    def __init__(self):
        super().__init__()
        self.housing = 6
        self.energy = -2

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
            self.jobs_slots.append(jobs.MaintenanceDrone())


class NexusDistrict(District):
    def __init__(self):
        super().__init__()
        self.housing = 5
        self.energy = -2

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
            self.jobs_slots.append(jobs.MaintenanceDrone())


class GeneratorDistrict(District):
    def __init__(self):
        super().__init__()
        self.housing = 2

        self.energy = -1

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
            self.jobs_slots.append(jobs.Technician())
        for c in range(self.tech_drones):
            self.jobs_slots.append(jobs.TechDrone())


class MiningDistrict(District):
    def __init__(self):
        super().__init__()
        self.housing = 2

        self.energy = -1

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
            self.jobs_slots.append(jobs.Miner())
        for c in range(self.mining_drones):
            self.jobs_slots.append(jobs.MiningDrone())


class AgricultureDistrict(District):
    def __init__(self):
        super().__init__()
        self.housing = 2

        self.energy = -1

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
            self.jobs_slots.append(jobs.Farmer())
        for c in range(self.agri_drones):
            self.jobs_slots.append(jobs.AgriDrone())
