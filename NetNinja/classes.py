class Planet:
    # Defining attributes of class Planet with __init__() constructor - Hard-coded values!
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'
# Functions can be added as instance properties

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


# New instance of class Planet
# hoth = Planet()
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(hoth.orbit())


class newPlanet:
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


hoth = newPlanet('Hoth', 200000, 5.5, 'Hoth System')
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(hoth.orbit())

naboo = newPlanet('Naboo', 300000, 8, 'Naboo System')
print(f'Name is: {naboo.name}')
print(f'Radius is: {naboo.radius}')
print(naboo.orbit())
