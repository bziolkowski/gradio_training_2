import gradio as gr
import pandas as pd
import time

def process_file(file):
    print(file)
    time.sleep(3)
    df = pd.read_excel(file)
    return gr.DataFrame(value=df, visible=True)

with gr.Blocks() as ui:
    file = gr.File(file_count="single", type="filepath")
    table = gr.Dataframe(visible=False)
    file.upload(fn=process_file, inputs=[file], outputs=[table])

ui.launch()