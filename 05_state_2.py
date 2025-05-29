import gradio as gr
from datetime import datetime

def init():
    unique_value = str(datetime.now().time())
    return unique_value

def get_name():
    name = "Antoni"
    return name

def set_greeting(name):
    return f"Cześć {name}"

with gr.Blocks() as ui:
    title = gr.Markdown("")
    name = gr.State("")
    # ui.load(fn=init, inputs=[], outputs=title)
    ui.load(fn=get_name, inputs=[], outputs=[name])
    name.change(fn=set_greeting, inputs=name, outputs=title)

ui.launch()