from functions import get_todos, write_todos

while True:
    user_action = input("choose add, show, edit, remove or exit: ")
    user_action = user_action.strip().lower()
    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'  # string slicing to extract from user input after add
        todo = todo.capitalize()

        todos = get_todos()

        todos.append(todo)

        write_todos(todos_arg=todos)

    elif user_action.startswith("show"):

        todos = get_todos()
        
        # list comprehension -- same as below code
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()
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

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue  # opposite of break! restarts the code cycle from top

    elif user_action.startswith("remove"):
        try:
            todos = get_todos()
            number = int(user_action[7:])
            todos.pop(number - 1)

            write_todos(todos_arg=todos)

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
