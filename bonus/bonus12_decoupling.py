feet_inches = input("Enter feet and inches: ")

def parse(feetinches):
    converted = feetinches.split(" ") # will form a list by omitting the space
    feet = float(converted[0])
    inch = float(converted[1])
    return feet, inch


def calculate(feet, inch):
    meters = feet * 0.3048 + inch * 0.0254
    print(f"{feet} feet and {inch} inch is equal to {meters} meters")
    return meters


f, i = parse(feet_inches)
value = calculate(f, i)

if value < 1:
    print("The kid is too short for the rollercoaster ride. Entry denied!")
else:
    print("Enjoy the ride")