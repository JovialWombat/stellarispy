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
from tqdm.contrib.itertools import product

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


def main():

    empire_name = "tta"

    with open("input/{0}.json".format(empire_name)) as f:
        data = json.load(f)

        # create planets from input data
        planets = create_planets(data)

        # use average planets and modifiers to solve resource value equation, or use districts and buildings
        helpers.resource_relative_values = helpers.solve_resource_equations(planets)

        minimisable_consumables = {
            "housing": 0,
            "amenities": 0,
            "food": 1,
            "goods": 1,
            "admin": 1,
        }
        maximisable_consumables = {
            "energy": 1,
            "minerals": 1,
            "alloys": 1,
            "motes": 1,
            "gases": 1,
            "crystals": 1,
        }
        non_consumables = {
            "trade": 1.0,
            "unity": 1.0,
            "research": 3.0,
            "naval": 1.0,
            "storage": 1.0,
        }
        excluded = {
            "housing": 0,
            "amenities": 0,
            "trade": 1.0,
            "unity": 1.0,
            "naval": 1.0,
            "storage": 1.0,
        }

        # mask off the resources that we want around 0
        target_value_proportion = {
            key: value
            for (key, value) in {
                **minimisable_consumables,
                **maximisable_consumables,
                **non_consumables,
            }.items()
            if key not in excluded.keys()
        }

        # target equal value produced from each resource
        helpers.target_value_proportions = {
            key: value / sum(target_value_proportion.values())
            for (key, value) in target_value_proportion.items()
        }

        penalty_exponent = {
            "food": 1.0,
            "goods": 1.0,
            "admin": 1.0,
            "energy": 1.0,
            "minerals": 1.0,
            "alloys": 1.0,
            "motes": 1.0,
            "gases": 1.0,
            "crystals": 1.0,
            "research": 1.0,
        }
        constant = 0.01
        penalty_exponent = {k: constant * v for (k, v) in penalty_exponent.items()}
        # # create possible planet builds
        # for index, p in enumerate(planets):
        #     planet_builds = []
        #     if index == 0:
        #         planet_builds.append(planet_build.EmpireCapital(p))
        #     else:
        #         for d in helpers.possible_colony_designations:
        #             if d["name"] == "Mining World":
        #                 planet_builds.append(planet_build.MiningWorld(p))
        #             elif d["name"] == "Agri World":
        #                 planet_builds.append(planet_build.AgriWorld(p))
        #             elif d["name"] == "Generator World":
        #                 planet_builds.append(planet_build.GeneratorWorld(p))
        #             elif d["name"] == "Forge World":
        #                 planet_builds.append(planet_build.ForgeWorld(p))
        #             elif d["name"] == "Industrial World":
        #                 planet_builds.append(planet_build.IndustrialWorld(p))
        #             elif d["name"] == "Refinery World":
        #                 planet_builds.append(planet_build.RefineryWorld(p))
        #             elif d["name"] == "Tech World":
        #                 planet_builds.append(planet_build.TechWorld(p))
        #             elif d["name"] == "Fortress World":
        #                 planet_builds.append(planet_build.FortressWorld(p))
        #             elif d["name"] == "Bureaucratic World":
        #                 planet_builds.append(planet_build.BureaucraticWorld(p))

        #     min_error = float("inf")
        #     best_build = None
        #     for b in planet_builds:
        #         # get the production for this build combined with previous locked in builds
        #         production = helpers.aggregate_production(helpers.complete_planet_builds, b)

        #         # calculate the error for this combination
        #         errors = helpers.calculate_aggregate_error(
        #             helpers.resource_relative_values,
        #             helpers.target_value_proportions,
        #             production,
        #         )

        #         error = sum([abs(v) for v in errors.values()])

        #         # cache the build that minimises overall error
        #         if error < min_error:
        #             min_error = error
        #             best_build = b

        #     # keep the best build
        #     helpers.complete_planet_builds.append(best_build)

        # this approach won't work, reached 5 billion iterations just incrementing a number...
        possible_planet_builds = []
        for index, p in enumerate(planets):
            planet_builds = []
            if p.designation != "":
                if p.designation == "EmpireCapital":
                    planet_builds.append(planet_build.EmpireCapital(p))
                elif p.designation == "MiningWorld":
                    planet_builds.append(planet_build.MiningWorld(p))
                # lithoid
                # elif p.designation == "AgriWorld":
                #     planet_builds.append(planet_build.AgriWorld(p))
                elif p.designation == "GeneratorWorld":
                    planet_builds.append(planet_build.GeneratorWorld(p))
                elif p.designation == "ForgeWorld":
                    planet_builds.append(planet_build.ForgeWorld(p))
                elif p.designation == "IndustrialWorld":
                    planet_builds.append(planet_build.IndustrialWorld(p))
                elif p.designation == "RefineryWorld":
                    planet_builds.append(planet_build.RefineryWorld(p))
                elif p.designation == "TechWorld":
                    planet_builds.append(planet_build.TechWorld(p))
                elif p.designation == "BureaucraticWorld":
                    planet_builds.append(planet_build.BureaucraticWorld(p))
            else:
                for d in helpers.possible_colony_designations:
                    if d["name"] == "Mining World":
                        planet_builds.append(planet_build.MiningWorld(p))
                    # lithoid
                    # elif d["name"] == "Agri World":
                    #     planet_builds.append(planet_build.AgriWorld(p))
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
                    elif d["name"] == "Bureaucratic World":
                        planet_builds.append(planet_build.BureaucraticWorld(p))
            possible_planet_builds.append(planet_builds)

        # all_planet_build_combinations = itertools.product(*possible_planet_builds)
        best_fit = float("inf")
        best_build = None
        count = 0
        for c in product(*possible_planet_builds):
            production = helpers.aggregate_production(c, None)

            # d = {k:v for (k, v) in production.items() if v < 0 and k in minimisable_consumables.keys() or k in maximisable_consumables.keys()}
            # if len(d) > 0:
            #     continue

            # calculate the error for this combination
            # minimisable_consumable_errors = helpers.calculate_aggregate_error(
            #     helpers.resource_relative_values,
            #     helpers.target_value_proportions,
            #     production,
            #     minimisable_consumables.keys(),
            # )
            # maximisable_consumable_errors = helpers.calculate_aggregate_error(
            #     helpers.resource_relative_values,
            #     helpers.target_value_proportions,
            #     production,
            #     maximisable_consumables.keys(),
            # )
            # non_consumable_errors = helpers.calculate_aggregate_error(
            #     helpers.resource_relative_values,
            #     helpers.target_value_proportions,
            #     production,
            #     non_consumables.keys(),
            # )
            errors = helpers.calculate_aggregate_error(
                helpers.resource_relative_values,
                helpers.target_value_proportions,
                production,
                list(helpers.target_value_proportions.keys()) + ["jobs"],
            )

            # total_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
            fit = np.prod(
                [np.exp(penalty_exponent[k] * abs(v)) for (k, v) in errors.items()]
            )

            if fit < best_fit:
                best_fit = fit
                best_build = c
        count += 1

        # possible_planet_builds = []
        # for index, p in enumerate(planets):
        #     planet_builds = []
        #     for d in helpers.possible_colony_designations:
        #         if d["name"] == "Empire Capital":
        #             b = planet_build.EmpireCapital(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Mining World":
        #             b = planet_build.MiningWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Agri World":
        #             b = planet_build.AgriWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Generator World":
        #             b = planet_build.GeneratorWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Forge World":
        #             b = planet_build.ForgeWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Industrial World":
        #             b = planet_build.IndustrialWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Refinery World":
        #             b = planet_build.RefineryWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Tech World":
        #             b = planet_build.TechWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))
        #         elif d["name"] == "Bureaucratic World":
        #             b = planet_build.BureaucraticWorld(p)
        #             production = helpers.aggregate_production(None,b)
        #             produced_value = helpers.calculate_total_value(helpers.resource_relative_values, production)
        #             planet_builds.append((b,produced_value))

        #     planet_builds = sorted(planet_builds, key = lambda i: i[1], reverse=True)
        #     possible_planet_builds.append(planet_builds)
        # possible_planet_builds = sorted(possible_planet_builds, key = lambda b: max([b[0][] for b in p]), reverse=True)

        final_production = helpers.aggregate_production(best_build, None)
        export_data(final_production, "{0}-production".format(empire_name))

        # minimisable_consumable_errors = helpers.calculate_aggregate_error(
        #     helpers.resource_relative_values,
        #     helpers.target_value_proportions,
        #     production,
        #     minimisable_consumables.keys(),
        # )
        # maximisable_consumable_errors = helpers.calculate_aggregate_error(
        #     helpers.resource_relative_values,
        #     helpers.target_value_proportions,
        #     production,
        #     maximisable_consumables.keys(),
        # )
        # non_consumable_errors = helpers.calculate_aggregate_error(
        #     helpers.resource_relative_values,
        #     helpers.target_value_proportions,
        #     production,
        #     non_consumables.keys(),
        # )
        errors = helpers.calculate_aggregate_error(
            helpers.resource_relative_values,
            helpers.target_value_proportions,
            final_production,
            list(helpers.target_value_proportions.keys()) + ["jobs"],
        )
        export_data(errors, "{0}-errors".format(empire_name))

        builds_to_export = []
        for b in best_build:
            b.prepare_for_export()
            to_export = {k: v for (k, v) in b.__dict__.items() if re.match(r"\_.*", k)}
            builds_to_export.append(to_export)
        data_to_export = {
            "EmpireCapitals": len([
                b for b in best_build if b._designation == "EmpireCapital"
            ]),
            "MiningWorlds": len([
                b for b in best_build if b._designation == "MiningWorld"
            ]),
            "AgriWorlds": len([
                b for b in best_build if b._designation == "AgriWorld"
            ]),
            "GeneratorWorlds": len([
                b for b in best_build if b._designation == "GeneratorWorld"
            ]),
            "ForgeWorlds": len([
                b for b in best_build if b._designation == "ForgeWorld"
            ]),
            "IndustrialWorlds": len([
                b for b in best_build if b._designation == "IndustrialWorld"
            ]),
            "RefineryWorlds": len([
                b for b in best_build if b._designation == "RefineryWorld"
            ]),
            "TechWorlds": len([
                b for b in best_build if b._designation == "TechWorld"
            ]),
            "BureaucraticWorlds": len([
                b for b in best_build if b._designation == "BureaucraticWorld"
            ]),
            "Planets":builds_to_export
        }
        export_data(data_to_export, "{0}-planets".format(empire_name))
        # builds_to_export = []
        # for c in possible_planet_builds:
        #     for b in c:
        #         b[0].prepare_for_export()
        #         to_export = {k: v for (k, v) in b[0].__dict__.items() if re.match(r"\_.*", k)}
        #         to_export["value"] = b[1]
        #         builds_to_export.append(to_export)
        # export_data(builds_to_export, "{0}-planets".format(empire_name))


if __name__ == "__main__":
    # execute only if run as a script
    main()
