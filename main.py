todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':

            todo = input("Eneter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of todo to edit:"))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo +'\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of todo to edit:"))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(number - 1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'exit':
            break
