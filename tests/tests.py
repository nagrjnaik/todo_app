filenames = ["1.raw data.txt", "2.app.txt", "3.py.txt"]
filenames = [filename.replace('.', '-', 1) for filename in filenames]
print(filenames)
