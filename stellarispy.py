# this currently is only built to work for the lithoid megacorp Tavurite Trade Association in 2.6
import json
import planet
import helpers
import jsonpickle
from colorama import init
from colorama import Fore, Back, Style

init()


def create_planets(data):
    output_data = []
    for d in data:
        output_data.append(planet.planet(d))
    return output_data


def export_data(data):
    f = open("output_data.json", "w")
    json_obj = jsonpickle.encode(data)
    f.write(json_obj)


def solve_resource_equations(planets):
    resource_values = {}
    # housing, amenities, energy,minerals,food,trade,goods,alloys, influence, unity, phys, soc, eng, motes, gases, crystals, living metal, zro, dark matter, nanites, admin cap, naval cap
    


with open("data.json") as f:
    data = json.load(f)
    # create planets from input data
    planets = create_planets(data)
    # use average planets and modifiers to solve resource value equation, or use districts and buildings
    # resource_values = solve_resource_equations(planets)
    # create possible builds, excluding capital
    # for every possible permutation of planet designations:
    # calculate net resource production and total resource value
    # discard those with any negative resource production
    # possibly balance advanced resources by their value to stop one dominating?
    # pick the maximum total resource value

    for p in planets:
        p.optimise_planet()
        p.print_planet()

    # generators = sorted(planets, key=lambda x: x.generator_districts, reverse=True)
    # for p in generators:
    #     print(Fore.YELLOW)
    #     p.print_planet()
    # miners = sorted(planets, key=lambda x: x.mining_districts, reverse=True)
    # for p in miners:
    #     print(Fore.RED)
    #     p.print_planet()
    # farmers = sorted(planets, key=lambda x: x.agriculture_districts, reverse=True)
    # for p in farmers:
    #     print(Fore.GREEN)
    #     p.print_planet()
    export_data(planets)
