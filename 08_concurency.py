import gradio as gr
import time

def processing():
    time.sleep(10)
    return "Koniec"

with gr.Blocks() as ui:
    text = gr.Textbox("Wciśnij przycisk")
    button = gr.Button("Start")
    button.click(fn=processing, outputs=[text])
    ui.queue(default_concurrency_limit=10)
ui.launch()