contents = ["Hello", "My name is Nagraj", "And this is my first list program"]
file_names = ["file1.txt","file2.txt","file3.txt"]

for content, file_name in zip(contents, file_names):
    file_name = open (file_name, 'w')
    file_name.write(content)