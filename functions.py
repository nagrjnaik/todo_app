def get_todos(filepath='Todo_list.txt'):
    """
    Reads the text file and returns the items in a list
    this space called as doc string
    can be accessed by print(help(get_todos))
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # local variable name should be different from global variables
        return todos_local


def write_todos(todos_arg, filepath='Todo_list.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Test")
    """
    The above is used when you want to run this block
    and get the output directly from this program.
    But if you run the other program which is importing
    this functions.py this block won't be executed.
    """