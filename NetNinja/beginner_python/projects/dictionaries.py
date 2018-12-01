# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f"I am {key} and I have a {val} belt")

# Using set() to count the number of belts for each color


def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')


ninja_belts = {}


while True:
    ninja_name = input("enter a ninja name: ")
    ninja_belt = input("enter a belt color: ")
# adding the key/value pair to our dictionary
    ninja_belts[ninja_name] = ninja_belt

# This will stop the potential infinite looping
    another = input("add another? (y/n): ")
    if another == "y":
        continue
    else:
        break

# invoking the function

# ninja_intro(ninja_belts)
belt_count(ninja_belts)
