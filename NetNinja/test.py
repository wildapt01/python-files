from classes import Planet    # This to import from a module
from space.planet import NewPlanet
from space.calc import planet_mass, planet_vol

hoth = Planet('Hoth', 400000, 5.2, 'Hoth System')
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')
print(hoth.orbit())

naboo = NewPlanet('Naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}.')
