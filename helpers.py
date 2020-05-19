import numpy as np
import districts, buildings

resource_relative_values = None
target_production_proportions = None
complete_planet_builds = []


def solve_resource_equations(planets):
    district_list = [
        districts.CityDistrict(),
        districts.GeneratorDistrict(),
        districts.MiningDistrict(),
        districts.AgricultureDistrict(),
    ]
    max_district_production = []
    for d in district_list:
        max_district_production.append(d.aggregate_resources())
    buildings_list = [
        buildings.HyperEntertainmentForums(),
        buildings.ResourceSilos(),
        buildings.CivilianRepliComplexes(),
        buildings.AlloyNanoPlants(),
        buildings.HypercommsForum(),
        buildings.AdvancedResearchComplexes(),
        buildings.ChemicalPlants(),
        buildings.ExoticGasRefineries(),
        buildings.SyntheticCrystalPlants(),
        buildings.AdministrativePark(),
        buildings.Fortress(),
    ]
    max_building_production = []
    for b in buildings_list:
        max_building_production.append(b.aggregate_resources())
    districts_and_building_production = (
        max_district_production + max_building_production
    )

    array = []
    jobs = []
    for p in districts_and_building_production:
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
    ]
    resource_relative_values = {}
    for index, name in enumerate(resource_names):
        resource_relative_values[name] = in_terms_of_energy[index]
    return resource_relative_values


def aggregate_production(complete_planet_builds, planet_build):
    production = {}
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
    resource_relative_values, target_production_proportions, production
):
    produced_value = {
        key: production[key] * value
        for (key, value) in resource_relative_values.items()
    }
    total_produced_value = sum(produced_value.values())
    total_target_proportions = sum(target_production_proportions.values())
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
