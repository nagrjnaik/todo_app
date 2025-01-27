try:
    length = float(input("Enter the length for the rectangle: "))
    width = float(input("Enter the width for the rectangle: "))
    if length == width:
        exit("This is a square, please recheck the inputs")
    area = length * width
    print(f"The area of the rectangle is {area}")
except ValueError:
    print(f"Please enter a number")
