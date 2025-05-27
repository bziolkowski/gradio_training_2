import gradio as gr

def resize(col_size):
    return gr.Column(scale=col_size)

with gr.Blocks() as ui:
    with gr.Tab("Main"):
        with gr.Row():
            gr.Button(value="Przycisk 1", scale=1)
            gr.Button(value="Przyciek 2", scale=2)
        with gr.Row():
            gr.Button(value="Przycisk 3")
            gr.Button(value="Przyciek 4")

        with gr.Row():
            with gr.Column(scale=1):
                pass
                # gr.Button(value="Przyciek 5")
                # gr.Button(value="Przyciek 6")
            with gr.Column(scale=2) as col:
                gr.Button(value="Przyciek 7")
                gr.Button(value="Przyciek 8")
    with gr.Tab("About"):
        gr.Markdown("Aleśmy się narobili")
        
    with gr.Accordion(label="Settings", open=False):
        size = gr.Slider(minimum=1, maximum=5, value=1)



    size.change(fn=resize, inputs=size, outputs=col)



ui.launch()
