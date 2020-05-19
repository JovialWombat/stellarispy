class planet(object):
    def __init__(self, planet):
        self.name = planet["name"]
        self.maximum_districts = planet["maximum_districts"]
        self.maximum_generator_districts = planet["maximum_generator_districts"]
        self.maximum_mining_districts = planet["maximum_mining_districts"]
        self.maximum_agriculture_districts = planet["maximum_agriculture_districts"]
