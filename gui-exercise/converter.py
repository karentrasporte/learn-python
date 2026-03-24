import FreeSimpleGUI as sg
import converter_def

feet_label = sg.Text("Enter feet")
inches_label = sg.Text("Enter inches")
feet_input = sg.InputText(tooltip="Enter feet", key="feet")
inches_input = sg.InputText(tooltip="Enter inches", key="inches")
convert_button = sg.Button("Convert", key="convert")
convert_label = sg.Text("",key="convert_label")

window = sg.Window(title="Converter",
                   layout=[[feet_label, feet_input], [inches_label, inches_input], [convert_button,convert_label]],
                   font=("Helvetica",16))

while True:
    event, values = window.read()
    match event:
        case "convert":
            feet = float(feet_input.get())
            inches = float(inches_input.get())

            result = converter_def.convert(feet, inches)
            print(result)

            window['convert_label'].update(value=f"{result:.4} m")
        case sg.WIN_CLOSED:
            break

window.close()