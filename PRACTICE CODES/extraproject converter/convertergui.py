import FreeSimpleGUI as sg
from converter import feetinch_to_meter

sg.theme("Black")

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

button1 = sg.Button("Convert", key="convert")
button2 = sg.Button("Exit")
output_label = sg.Text(key="output")

window = sg.Window("Converter",
                   layout=[[label1, input1],
                           [label2, input2],
                           [button1, button2, output_label]])


while True:
    event, values = window.read()
    match event:
        case "convert":
            try:
                print(event, values)
                feet = values["feet"][0]
                inch = values["inches"][0]
                output = feetinch_to_meter(feet, inch)
                window["output"].update(value=output)
            except IndexError:
                sg.popup("Please provide two numbers", font=("Helvetica", 10))
        case "Exit":
            break
    
window.close()
