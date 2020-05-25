import modifiers
import jobs


class District(object):
    def __init__(self):
        self.name = "District"
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
            "housing": self.production["housing"]
            + sum(
                (j.production["housing"] * j.production_coefficients["housing"])
                + j.production_constants["housing"]
                + (j.upkeep["housing"] * j.upkeep_coefficients["housing"])
                + j.upkeep_constants["housing"]
                for j in self.jobs_slots
            ),
            "amenities": self.production["amenities"]
            + sum(
                (j.production["amenities"] * j.production_coefficients["amenities"])
                + j.production_constants["amenities"]
                + (j.upkeep["amenities"] * j.upkeep_coefficients["amenities"])
                + j.upkeep_constants["amenities"]
                for j in self.jobs_slots
            ),
            "energy": self.production["energy"]
            + sum(
                (j.production["energy"] * j.production_coefficients["energy"])
                + j.production_constants["energy"]
                + (j.upkeep["energy"] * j.upkeep_coefficients["energy"])
                + j.upkeep_constants["energy"]
                for j in self.jobs_slots
            ),
            "minerals": self.production["minerals"]
            + sum(
                (j.production["minerals"] * j.production_coefficients["minerals"])
                + j.production_constants["minerals"]
                + (j.upkeep["minerals"] * j.upkeep_coefficients["minerals"])
                + j.upkeep_constants["minerals"]
                for j in self.jobs_slots
            ),
            "food": self.production["food"]
            + sum(
                (j.production["food"] * j.production_coefficients["food"])
                + j.production_constants["food"]
                + (j.upkeep["food"] * j.upkeep_coefficients["food"])
                + j.upkeep_constants["food"]
                for j in self.jobs_slots
            ),
            "trade": self.production["trade"]
            + sum(
                (j.production["trade"] * j.production_coefficients["trade"])
                + j.production_constants["trade"]
                + (j.upkeep["trade"] * j.upkeep_coefficients["trade"])
                + j.upkeep_constants["trade"]
                for j in self.jobs_slots
            ),
            "goods": self.production["goods"]
            + sum(
                (j.production["goods"] * j.production_coefficients["goods"])
                + j.production_constants["goods"]
                + (j.upkeep["goods"] * j.upkeep_coefficients["goods"])
                + j.upkeep_constants["goods"]
                for j in self.jobs_slots
            ),
            "alloys": self.production["alloys"]
            + sum(
                (j.production["alloys"] * j.production_coefficients["alloys"])
                + j.production_constants["alloys"]
                + (j.upkeep["alloys"] * j.upkeep_coefficients["alloys"])
                + j.upkeep_constants["alloys"]
                for j in self.jobs_slots
            ),
            "unity": self.production["unity"]
            + sum(
                (j.production["unity"] * j.production_coefficients["unity"])
                + j.production_constants["unity"]
                + (j.upkeep["unity"] * j.upkeep_coefficients["unity"])
                + j.upkeep_constants["unity"]
                for j in self.jobs_slots
            ),
            "research": (
                self.production["physics"]
                + sum(
                    (j.production["physics"] * j.production_coefficients["physics"])
                    + j.production_constants["physics"]
                    + (j.upkeep["physics"] * j.upkeep_coefficients["physics"])
                    + j.upkeep_constants["physics"]
                    for j in self.jobs_slots
                )
                + self.production["society"]
                + sum(
                    (j.production["society"] * j.production_coefficients["society"])
                    + j.production_constants["society"]
                    + (j.upkeep["society"] * j.upkeep_coefficients["society"])
                    + j.upkeep_constants["society"]
                    for j in self.jobs_slots
                )
                + self.production["engineering"]
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
            "motes": self.production["motes"]
            + sum(
                (j.production["motes"] * j.production_coefficients["motes"])
                + j.production_constants["motes"]
                + (j.upkeep["motes"] * j.upkeep_coefficients["motes"])
                + j.upkeep_constants["motes"]
                for j in self.jobs_slots
            ),
            "gases": self.production["gases"]
            + sum(
                (j.production["gases"] * j.production_coefficients["gases"])
                + j.production_constants["gases"]
                + (j.upkeep["gases"] * j.upkeep_coefficients["gases"])
                + j.upkeep_constants["gases"]
                for j in self.jobs_slots
            ),
            "crystals": self.production["crystals"]
            + sum(
                (j.production["crystals"] * j.production_coefficients["crystals"])
                + j.production_constants["crystals"]
                + (j.upkeep["crystals"] * j.upkeep_coefficients["crystals"])
                + j.upkeep_constants["crystals"]
                for j in self.jobs_slots
            ),
            "admin": self.production["admin"]
            + sum(
                (j.production["admin"] * j.production_coefficients["admin"])
                + j.production_constants["admin"]
                + (j.upkeep["admin"] * j.upkeep_coefficients["admin"])
                + j.upkeep_constants["admin"]
                for j in self.jobs_slots
            ),
            "naval": self.production["naval"]
            + sum(
                (j.production["naval"] * j.production_coefficients["naval"])
                + j.production_constants["naval"]
                + (j.upkeep["naval"] * j.upkeep_coefficients["naval"])
                + j.upkeep_constants["naval"]
                for j in self.jobs_slots
            ),
            "storage": self.production["storage"]
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

class CityDistrict(District):
    def __init__(self):
        super().__init__()
        self.name = "CityDistrict"
        self.production["housing"] = 5
        self.upkeep["energy"] = -2

        self.clerks = 1

        if "agrarian_idyll" in modifiers.civics:
            self.production["housing"] -= 1
        if "public_works" in modifiers.traditions:
            self.production["housing"] += 1
        if "trans_stellar_corporations" in modifiers.traditions:
            self.clerks += 1
        if "weather_control_systems" in modifiers.research:
            self.production["housing"] += 1
        if "anti_gravity_engineering" in modifiers.research:
            self.production["housing"] += 1

        for j in range(self.clerks):
            self.jobs_slots.append(jobs.Clerk())


class HiveDistrict(District):
    def __init__(self):
        super().__init__()
        self.name = "HiveDistrict"
        self.production["housing"] = 6
        self.upkeep["energy"] = -2

        self.maintenance_drones = 3

        if "hive_world" in modifiers.planet_type:
            self.production["housing"] = 12
            self.maintenance_drones = 6

        if "agrarian_idyll" in modifiers.civics:
            self.production["housing"] -= 1
        if "public_works" in modifiers.traditions:
            self.production["housing"] += 1
        # if "trans_stellar_corporations" in modifiers.traditions:
        #     self.clerks += 1
        if "weather_control_systems" in modifiers.research:
            self.production["housing"] += 1
        if "anti_gravity_engineering" in modifiers.research:
            self.production["housing"] += 1
            self.maintenance_drones += 1

        for j in range(self.maintenance_drones):
            self.jobs_slots.append(jobs.MaintenanceDrone())


class NexusDistrict(District):
    def __init__(self):
        super().__init__()
        self.name = "NexusDistrict"

        self.production["housing"] = 5
        self.upkeep["energy"] = -2

        self.maintenance_drones = 3

        if "agrarian_idyll" in modifiers.civics:
            self.production["housing"] -= 1
        if "public_works" in modifiers.traditions:
            self.production["housing"] += 1
        # if "trans_stellar_corporations" in modifiers.traditions:
        #     self.clerks += 1
        if "weather_control_systems" in modifiers.research:
            self.production["housing"] += 1
        if "anti_gravity_engineering" in modifiers.research:
            self.production["housing"] += 1
            self.maintenance_drones += 1

        for j in range(self.maintenance_drones):
            self.jobs_slots.append(jobs.MaintenanceDrone())


class GeneratorDistrict(District):
    def __init__(self):
        super().__init__()
        self.name = "GeneratorDistrict"

        self.production["housing"] = 2

        self.upkeep["energy"] = -1

        self.technicians = 2
        self.tech_drones = 0

        if "machine_intelligence" in modifiers.authority:
            self.production["housing"] = 3
            self.technicians = 0
            self.tech_drones = 2
        if "hive_mind" in modifiers.authority:
            self.technicians = 0
            self.tech_drones = 3
        if "agrarian_idyll" in modifiers.civics:
            self.production["housing"] = 3

        for c in range(self.technicians):
            self.jobs_slots.append(jobs.Technician())
        for c in range(self.tech_drones):
            self.jobs_slots.append(jobs.TechDrone())


class MiningDistrict(District):
    def __init__(self):
        super().__init__()
        self.name = "MiningDistrict"
        self.production["housing"] = 2

        self.upkeep["energy"] = -1

        self.miners = 2
        self.mining_drones = 0

        if "machine_intelligence" in modifiers.authority:
            self.production["housing"] = 3
            self.miners = 0
            self.mining_drones = 2
        if "hive_mind" in modifiers.authority:
            self.miners = 0
            self.mining_drones = 3
        if "agrarian_idyll" in modifiers.civics:
            self.production["housing"] = 3

        for c in range(self.miners):
            self.jobs_slots.append(jobs.Miner())
        for c in range(self.mining_drones):
            self.jobs_slots.append(jobs.MiningDrone())


class AgricultureDistrict(District):
    def __init__(self):
        super().__init__()
        self.name = "AgricultureDistrict"
        self.production["housing"] = 2

        self.upkeep["energy"] = -1

        self.farmers = 2
        self.agri_drones = 0

        if "machine_intelligence" in modifiers.authority:
            self.production["housing"] = 3
            self.farmers = 0
            self.agri_drones = 2
        if "hive_mind" in modifiers.authority:
            self.farmers = 0
            self.agri_drones = 3
        if "agrarian_idyll" in modifiers.civics:
            self.production["housing"] = 3
            if "agrarian_utopias" in modifiers.research:
                self.production["housing"] = 4

        for c in range(self.farmers):
            self.jobs_slots.append(jobs.Farmer())
        for c in range(self.agri_drones):
            self.jobs_slots.append(jobs.AgriDrone())
