user_entries = ['10', '19.1', '20']

# Convert all entries to float
new = [float(items) for items in user_entries]

# Double each item
new1 = [items + items for items in new]

print(new1)