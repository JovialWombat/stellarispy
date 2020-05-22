import numpy as np
import districts, buildings

resource_relative_values = None
target_production_proportions = None
complete_planet_builds = []


def solve_resource_equations(planets):
    producers_list = [
        districts.CityDistrict(),
        buildings.HyperEntertainmentForums(),
        districts.GeneratorDistrict(),
        districts.MiningDistrict(),
        districts.AgricultureDistrict(),
        buildings.CommerceMegaplexes(),
        buildings.CivilianRepliComplexes(),
        buildings.AlloyNanoPlants(),
        buildings.HypercommsForum(),
        buildings.AdvancedResearchComplexes(),
        buildings.ChemicalPlants(),
        buildings.ExoticGasRefineries(),
        buildings.SyntheticCrystalPlants(),
        buildings.AdministrativePark(),
        buildings.Fortress(),
        buildings.ResourceSilos(),
    ]
    production = []
    for p in producers_list:
        production.append(p.aggregate_resources())
    array = []
    jobs = []
    for p in production:
        values = [v for k, v in p.items() if k != "jobs"]
        j = [v for k, v in p.items() if k == "jobs"]
        array.append(values)
        jobs.append(j)
    a = np.array(array)
    b = np.array(jobs)
    solution = np.linalg.solve(a, b).tolist()

    # energy is element 2...
    energy_value = solution[2]
    in_terms_of_energy = [s[0] / energy_value[0] for s in solution]
    resource_names = [
        "housing",
        "amenities",
        "energy",
        "minerals",
        "food",
        "trade",
        "goods",
        "alloys",
        "unity",
        "research",
        "motes",
        "gases",
        "crystals",
        "admin",
        "naval",
        "storage",
    ]
    resource_relative_values = {}
    for index, name in enumerate(resource_names):
        resource_relative_values[name] = in_terms_of_energy[index]
    return resource_relative_values


def aggregate_production(complete_planet_builds, planet_build):
    production = {}
    if complete_planet_builds != None:
        for p in complete_planet_builds:
            for key, value in p.production.items():
                if key not in production:
                    production[key] = value
                else:
                    production[key] += value
    if planet_build != None:
        for key, value in planet_build.production.items():
            if key not in production:
                production[key] = value
            else:
                production[key] += value
    return production


def calculate_aggregate_error(
    resource_relative_values, target_production_proportions, production, resource_mask
):
    # mask off resources
    production = {
        key: value
        for (key, value) in production.items() if key in resource_mask
    }
    target_production_proportions = {
        key: value
        for (key, value) in target_production_proportions.items() if key in resource_mask
    }

    produced_value = {
        key: resource_relative_values[key] * value
        for (key, value) in production.items()
    }
    total_produced_value = abs(sum(produced_value.values()))
    total_target_proportions = sum(target_production_proportions.values())
    if np.isclose(total_target_proportions,0):
        total_target_proportions = 1.0
    errors = {
        key: value
        - (
            target_production_proportions[key]
            * total_produced_value
            / total_target_proportions
        )
        for (key, value) in produced_value.items()
    }
    return errors

def calculate_total_value(
    resource_relative_values, production
):
    produced_value = {
        key: production[key] * value
        for (key, value) in resource_relative_values.items()
    }
    total_produced_value = sum(produced_value.values())
    return total_produced_value


possible_colony_designations = [
    {
        "name": "Empire Capital",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Urban World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Mining World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.2,
        "food_multiplier": 1.0,
    },
    {
        "name": "Agri World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.2,
    },
    {
        "name": "Generator World",
        "energy_multiplier": 1.2,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Forge World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Industrial World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Refinery World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Tech World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Fortress World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Rural World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
    {
        "name": "Bureaucratic World",
        "energy_multiplier": 1.0,
        "mineral_multiplier": 1.0,
        "food_multiplier": 1.0,
    },
]
