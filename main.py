while True:
    user_action = input("choose add, show, edit, remove or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input("Add a todo: ") + '\n'
            todo = todo.capitalize()
            with open('Todo_list.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open('Todo_list.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('Todo_list.txt', 'r') as file:
                todos = file.readlines()
            # list comprehension -- same as below code
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")

        case 'edit':
            with open('Todo_list.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("Number of the todo to edit: "))
            number = number - 1 #adjust for indexing
            new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo.capitalize()
            with open('Todo_list.txt', 'w') as file:
                file.writelines(todos)

        case 'remove':
            with open('Todo_list.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("Number of the todo to edit: "))
            todos.pop(number - 1)
            with open('Todo_list.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

        case _:
            print("Please type a valid input")

print("Todo list closed.")


