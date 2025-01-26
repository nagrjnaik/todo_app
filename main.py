while True:
    user_action = input("choose add, show, edit, remove or exit: ")
    user_action = user_action.strip().lower()
    if 'add' in user_action:
        todo = user_action[4:] + '\n'  # string slicing to extract from user input after add
        todo = todo.capitalize()
        with open('Todo_list.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('Todo_list.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('Todo_list.txt', 'r') as file:
            todos = file.readlines()
        # list comprehension -- same as below code
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif 'edit' in user_action:
        with open('Todo_list.txt', 'r') as file:
            todos = file.readlines()
        number = int(user_action[5:])
        number = number - 1 #adjust for indexing
        new_todo = input("Enter a new todo: ") + '\n'
        todos[number] = new_todo.capitalize()
        with open('Todo_list.txt', 'w') as file:
            file.writelines(todos)

    elif 'remove' in user_action:
        with open('Todo_list.txt', 'r') as file:
            todos = file.readlines()
        number = int(user_action[7:])
        todos.pop(number - 1)
        with open('Todo_list.txt', 'w') as file:
            file.writelines(todos)

    elif 'exit' in user_action:
        break

    else:
        print("Command is not valid!")

print("Todo list closed.")
