import gradio as gr

def language(lang):
    if lang == 'polski':
        return gr.Dropdown(choices=["raz", "dwa", "trzy"], visible=True)
    else:
        return gr.Dropdown(choices=["one", "two", "three"], visible=True)

with gr.Blocks() as ui:
    radio = gr.Radio(choices=["polski", "angielski"], interactive=True)
    dropdown = gr.Dropdown(choices=[], interactive=True, multiselect=True, visible=False)

    checkbox_g = gr.CheckboxGroup(choices=["Opcja 1", "Opcja 2"], visible=True)

    number = gr.Number(interactive=True, value=5, minimum=1, maximum=10, step=0.5)

    slider = gr.Slider(interactive=True, value=5, minimum=1, maximum=10, step=0.5)

    radio.select(fn=language, inputs=radio, outputs=dropdown)

ui.launch()