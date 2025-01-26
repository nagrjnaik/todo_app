date = input("Enter today's date (DD-MM-YYYY format): ")
mood = input("Enter today's mood: ")
journal = input("Enter your thoughts for today.\n").capitalize()

with open(date + '.txt', 'w') as file:
    file.write(journal)
