def avg_temp():
    try:
        with open('files/temperature_data.txt','r') as file:
            data = file.readlines()

        values = data[1:]  # list slicing to remove the header
        values = [float(items) for items in values]  # list comprehension
        average_local = sum(values) / len(values)
        return average_local
    except (ZeroDivisionError,FileNotFoundError,ValueError) as e:
        print(f"There is <<{e}>> error! please recheck the file")


average = avg_temp()
if average is not None:
    print(f"The average temperature is {average}")