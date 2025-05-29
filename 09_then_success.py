import gradio as gr
import time

def processing():
    time.sleep(3)
    return "Koniec"

def success():
    return gr.Text("Udało się", visible=True)

def processing_failed():
    raise Exception("An exception occurred")

with gr.Blocks() as ui:
    text = gr.Textbox("Wciśnij przycisk")
    button = gr.Button("Start")
    text2 = gr.Textbox(visible=False)
    #button.click(fn=processing, outputs=text).then(success, inputs=[], outputs=text2)

    # To się nie uda, bo processing_filed wyrzuca wyjątek
    button.click(fn=processing_failed).success(success, inputs=[], outputs=text2)

ui.launch()