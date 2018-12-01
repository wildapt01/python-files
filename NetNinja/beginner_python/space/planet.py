class NewPlanet:
    # Class attribute:
    shape = "round"
    # Defining instance attributes of class Planet with __init__() constructor - Dynamic!

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
# Instance method:

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
# Class method:

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'
# Static method

    @staticmethod
    def spin(speed="2000 mph"):
        return f'The planet spins at {speed}'
