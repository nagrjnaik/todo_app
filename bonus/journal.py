date = input("Enter today's date (DD-MM-YYYY format): ")
mood = input("Enter today's mood: ")
thoughts = input("Enter your thoughts for today.\n").capitalize()

with open(date + '.txt', 'w') as file:
    file.write(f"Today's mood is {mood}/10!\n")
    file.write(thoughts)
