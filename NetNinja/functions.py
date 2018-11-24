# def greet(name, time):
#     print(f"Good {time} {name}, hope you are well")


# name = input("Enter your name: ")
# time = input("Enter the time of the day: ")

# greet(name, time)

def area(radius):
    return 3.142*radius**2


def vol(area, length):
    print(area*length)


radius = int(input("Enter a radius: "))
length = int(input("Enter a length: "))

# area_calc = area(radius)
# vol(area_calc, length)

# or pass the function area() as an argument:
vol(area(radius), length)
