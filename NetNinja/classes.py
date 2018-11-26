class Planet:
    # Defining attributes of class Planet with __init__() constructor - Hard-coded values!
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'
# Functions can be added as properties

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


# New instance of class Planet
# hoth = Planet()
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(hoth.orbit())


class newPlanet:
    # Defining attributes of class Planet with __init__() constructor - Dynamic!
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = newPlanet('Hoth', 200000, 5.5, 'Hoth System')
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(hoth.orbit())

naboo = newPlanet('Naboo', 300000, 8, 'Naboo System')
print(f'Name is: {naboo.name}')
print(f'Radius is: {naboo.radius}')
print(naboo.orbit())
