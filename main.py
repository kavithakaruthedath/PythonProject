todos = []
while True:
    user_action =  input("Type add, show, edit, complete or exit: ")
    user_action =   user_action.strip()

    match user_action:
        case 'add':

            todo = input("Eneter a todo: ") +"\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close();            
            
            todos.append(todo)
            
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            #new_item =  [item.strip('\n') for item in todos]
            
            for index, item in enumerate(new_item):
                #item = item.strip('\n')
                row = f"{index +1}-{item}"
                print (row)
        case 'edit':
            number = int(input("Number of todo to edit:"))
            number = number -1
            new_todo = input("Enter new todo:")
            todos[number] = new_todo
        case 'complete':
            number =  number = int(input("Number of todo to edit:"))
            todos.pop(number-1)
        case 'exit':
            break


