import helpers


class planet_build(object):
    def __init__(self, planet, designation):
        self.__dict__.update(planet)
        self.designation = designation
        self.energy = 0
        self.minerals = 0
        self.food = 0
        self.alloys = 0
        self.goods = 0
        self.advanced = 0
        self.research = 0
        self.calculate_resource_production()
        # self.calculate_value()

    def calculate_resource_production(self):
        if self.designation.name == "Empire Capital":
            pass
        elif self.designation.name == "Urban World":
            pass
        elif self.designation.name == "Mining World":
            pass
        elif self.designation.name == "Agri World":
            pass
        elif self.designation.name == "Generator World":
            pass
        elif self.designation.name == "Forge World":
            pass
        elif self.designation.name == "Industrial World":
            pass
        elif self.designation.name == "Refinery World":
            pass
        elif self.designation.name == "Tech World":
            pass
        elif self.designation.name == "Fortress World":
            pass
        elif self.designation.name == "Rural World":
            pass
        elif self.designation.name == "Bureaucratic World":
            pass
