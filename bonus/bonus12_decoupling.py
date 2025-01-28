feet_inches = input("Enter feet and inches: ")

def convert(feet_inches_arg):
    converted = feet_inches.split(" ") # will form a list by omitting the space
    feet = float(converted[0])
    inch = float(converted[1])
    meters = feet * 0.3048 + inch * 0.0254
    print(f"{feet} feet and {inch} inch is equal to {meters} meters")
    return meters

value = convert(feet_inches_arg=feet_inches)

if value <= 1.5:
    print("The kid is too short for the rollercoaster ride. Entry denied!")
else:
    print("Enjoy the ride")