while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter todo:") + "\n"

            with open("todos.txt","r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("todos.txt","r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index+1}-{item}"
                print(row)

        case "edit":
            number = int(input("Which number do you want to edit?"))
            number = number - 1
            new_todo = input("Enter your new to do:")
            todos[number] = new_todo

        case "complete":
            number = int(input("Which number do you want to complete?"))
            todos.pop(number-1)

        case "exit":
            break

print("Bye!")
