from os import write
import FreeSimpleGUI as sg
from functions import get_todos, write_todos

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window(title="Free Simple GUI",
                   layout=[[label],[input_box,add_button]],
                   font=("Helvetica",20))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            print(new_todo)
            write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()