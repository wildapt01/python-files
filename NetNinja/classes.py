class Planet:
    # Defining attributes of class Planet with __init__() constructor
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'
# Functions can be added as properties

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


# New instance of class Planet
hoth = Planet()
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(hoth.orbit())
