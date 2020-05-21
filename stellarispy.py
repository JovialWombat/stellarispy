import re
from pathlib import Path
import json
import helpers
import jsonpickle
from colorama import init
from colorama import Fore, Back, Style
import numpy as np
import itertools
import os

import planet
import districts
import buildings
import planet_build
from tqdm import tqdm

init()

# this currently is only built to work for the lithoid megacorp Tavurite Trade Association in 2.6


def create_planets(data):
    output_data = []
    for d in data:
        output_data.append(planet.planet(d))
    return output_data


def export_data(data, filename):
    Path("output/").mkdir(parents=True, exist_ok=True)

    # increment file name to avoid overrwriting data
    i = 0
    while os.path.exists(f"output/{filename}{i}.json"):
        i += 1

    f = open(f"output/{filename}{i}.json", "w")
    json_obj = jsonpickle.encode(data)
    f.write(json_obj)


# def all_subclasses(cls):
#     return set(cls.__subclasses__()).union(
#         [s for c in cls.__subclasses__() for s in all_subclasses(c)]
#     )


# def instantiate_all_subclasses(classes):
#     return [obj() for obj in classes]

empire_name="unoe"

with open("input/{0}.json".format(empire_name)) as f:
    data = json.load(f)

    # create planets from input data
    planets = create_planets(data)

    # use average planets and modifiers to solve resource value equation, or use districts and buildings
    helpers.resource_relative_values = helpers.solve_resource_equations(planets)

    # mask off the resources that we want around 0
    target_production_mask = {
        "housing": 0,
        "amenities": 0,
        "energy": 1,
        "minerals": 1,
        "food": 0,
        "trade": 1,
        "goods": 0,
        "alloys": 1,
        "unity": 1,
        "research": 1,
        "motes": 1,
        "gases": 1,
        "crystals": 1,
        "admin": 0,
        "naval": 1,
    }

    # target equal value produced from each resource
    helpers.target_production_proportions = {
        key: target_production_mask[key] / value
        for (key, value) in helpers.resource_relative_values.items()
    }

    # create possible planet builds
    for index, p in enumerate(planets):
        planet_builds = []
        if index == 0:
            planet_builds.append(planet_build.EmpireCapital(p))
        else:
            for d in helpers.possible_colony_designations:
                if d["name"] == "Mining World":
                    planet_builds.append(planet_build.MiningWorld(p))
                elif d["name"] == "Agri World":
                    planet_builds.append(planet_build.AgriWorld(p))
                elif d["name"] == "Generator World":
                    planet_builds.append(planet_build.GeneratorWorld(p))
                elif d["name"] == "Forge World":
                    planet_builds.append(planet_build.ForgeWorld(p))
                elif d["name"] == "Industrial World":
                    planet_builds.append(planet_build.IndustrialWorld(p))
                elif d["name"] == "Refinery World":
                    planet_builds.append(planet_build.RefineryWorld(p))
                elif d["name"] == "Tech World":
                    planet_builds.append(planet_build.TechWorld(p))
                elif d["name"] == "Fortress World":
                    planet_builds.append(planet_build.FortressWorld(p))
                elif d["name"] == "Bureaucratic World":
                    planet_builds.append(planet_build.BureaucraticWorld(p))

        min_error = float("inf")
        best_build = None
        for b in planet_builds:
            # get the production for this build combined with previous locked in builds
            production = helpers.aggregate_production(helpers.complete_planet_builds, b)

            # calculate the error for this combination
            error = sum(
                [
                    abs(v)
                    for v in helpers.calculate_aggregate_error(
                        helpers.resource_relative_values,
                        helpers.target_production_proportions,
                        production,
                    ).values()
                ]
            )

            # cache the build that minimises overall error
            if error < min_error:
                min_error = error
                best_build = b

        # keep the best build
        helpers.complete_planet_builds.append(best_build)

    # this approach won't work, reached 5 billion iterations just incrementing a number...
    # all_planet_build_combinations = itertools.product(*complete_planet_builds)
    # min_error = float("inf")
    # best_build = None
    # count = 0
    # result = map(countup(count), all_planet_build_combinations)
    # for c in tqdm(all_planet_build_combinations):
    #     production = aggregate_production(c)
    #     error = calculate_aggregate_error(
    #         resource_relative_values, target_production_proportions, production
    #     )
    #     if error < min_error:
    #         min_error = error
    #         best_build = c
    # count+=1

    final_production = helpers.aggregate_production(
        helpers.complete_planet_builds, None
    )
    export_data(final_production, "{0}-production".format(empire_name))

    final_errors = {
        key: value / helpers.resource_relative_values[key]
        for (key, value) in helpers.calculate_aggregate_error(
            helpers.resource_relative_values,
            helpers.target_production_proportions,
            final_production,
        ).items()
    }
    export_data(final_errors, "{0}-errors".format(empire_name))

    builds_to_export= []
    for b in helpers.complete_planet_builds:
        b.prepare_for_export()
        to_export = {k:v for (k,v) in b.__dict__.items() if re.match(r"\_.*", k)}
        builds_to_export.append(to_export)
    export_data(builds_to_export, "{0}-planets".format(empire_name))
