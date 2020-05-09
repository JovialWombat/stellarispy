import helpers
import planet_build
import numpy as np
import math


class planet(object):
    def __init__(self, planet):
        self.__dict__.update(planet)
        self.name = planet["name"]
        self.maximum_districts = planet["maximum_districts"]
        self.maximum_generator_districts = planet["maximum_generator_districts"]
        self.maximum_mining_districts = planet["maximum_mining_districts"]
        self.maximum_agriculture_districts = planet["maximum_agriculture_districts"]
        self.city_districts = 0
        self.worker_districts = 0
        self.generator_districts = 0
        self.mining_districts = 0
        self.agriculture_districts = 0

    def calculate_districts(self):
        a = np.array(
            [[helpers.CITY_DISTRICT_HOUSING, helpers.WORKER_DISTRICT_HOUSING], [1, 1]]
        )
        b = np.array([helpers.POPS_REQUIRED, self.maximum_districts])
        districts = np.linalg.solve(a, b)
        self.city_districts = math.ceil(districts[0])
        self.worker_districts = math.floor(districts[1])

    def optimise_planet(self):
        self.calculate_districts()
        # planet_builds = []
        # for designation in helpers.POSSIBLE_COLONY_DESIGNATIONS:
        #     planet_builds.append(planet_build.planet_build(self, designation))

        # best_build = planet_builds[0]
        # for build in planet_builds:
        #     if build.value > best_build.value:
        #         best_build = build

        # self.designation = best_build.designation
        remaining_worker_districts = self.worker_districts
        while remaining_worker_districts > 0:
            if self.generator_districts < self.maximum_generator_districts:
                self.generator_districts += 1
                remaining_worker_districts -= 1
                if remaining_worker_districts == 0:
                    break
            if self.mining_districts < self.maximum_mining_districts:
                self.mining_districts += 1
                remaining_worker_districts -= 1
                if remaining_worker_districts == 0:
                    break
            # if self.agriculture_districts < self.maximum_agriculture_districts:
            #     self.agriculture_districts += 1
            #     remaining_worker_districts -= 1
            #     if remaining_worker_districts == 0:
            #         break

    def print_planet(self):
        print(
            "{0}:\n\tcity_districts:\t\t{1}\n\tgenerator_districts:\t{2}\n\tmining_districts:\t{3}\n\tagriculture_districts:\t{4}".format(
                self.name,
                self.city_districts,
                self.generator_districts,
                self.mining_districts,
                self.agriculture_districts,
            )
        )
