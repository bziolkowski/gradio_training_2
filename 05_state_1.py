import gradio as gr
from datetime import datetime

# Takie podejście generuje problemy

current_time = str(datetime.now().time())

with gr.Blocks() as ui:
    title = gr.Markdown(current_time)

ui.launch()