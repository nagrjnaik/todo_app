def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # local variable name should be different from global variables
        return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("choose add, show, edit, remove or exit: ")
    user_action = user_action.strip().lower()
    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'  # string slicing to extract from user input after add
        todo = todo.capitalize()

        todos = get_todos(filepath='Todo_list.txt')  # alternate way to write the code for better readability. not always needed.

        todos.append(todo)

        write_todos(todos_arg=todos,filepath='Todo_list.txt')

    elif user_action.startswith("show"):

        todos = get_todos('Todo_list.txt')
        
        # list comprehension -- same as below code
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos('Todo_list.txt')
            number = int(user_action[5:])
            number = number - 1  # adjust for indexing
            # 1 2 3 4 --> user input
            # 0 1 2 3 --> index adjustment
            if number < 0 or number >= len(todos):  # ensure index is valid  # this removes redundant input choice when the index in wrong
                print("There is no item with that number.")
                continue
            else:
                new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo.capitalize()

            write_todos('Todo_list.txt',todos)

        except ValueError:
            print("Your command is not valid.")
            continue  # opposite of break! restarts the code cycle from top

    elif user_action.startswith("remove"):
        try:
            todos = get_todos('Todo_list.txt')
            number = int(user_action[7:])
            todos.pop(number - 1)

            write_todos(todos_arg=todos, filepath='Todo_list.txt')

        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Please enter a value after remove command!")

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")

print("Todo list closed.")
