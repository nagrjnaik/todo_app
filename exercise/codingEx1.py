import random

while True:
    try:
        def generator(upper_bound_arg, lower_bound_arg):
            output = random.randrange(upper_bound_arg, lower_bound_arg)
            return output

        upper_bound = int(input("Enter the upper bound number: "))
        lower_bound = int(input("Enter the lower bound number: "))
        random_number = generator(lower_bound, upper_bound)
        print(random_number)
    except ValueError as e:
        print(f"Please provide proper limits")