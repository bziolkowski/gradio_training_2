import gradio as gr

def calc(text):
    operation_list = text.split(' ')
    arg1 = int(operation_list[0])
    arg2 = int(operation_list[2])
    operation = operation_list[1]

    if operation == "+":
        result = arg1 + arg2

    elif operation == "-":
        result = arg1 - arg2

    elif operation == "*":
        result = arg1 * arg2

    elif operation == "/":
        result = arg1 / arg2
    else:
        result = "Invalid operation"

    return gr.Textbox(value=result, visible=True)

with gr.Blocks() as ui:
    input = gr.Textbox(placeholder="Podaj działanie")
    output = gr.Textbox(visible=False)

    input.submit(fn=calc, inputs=input, outputs=output)

ui.launch()