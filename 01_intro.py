import gradio as gr

def process_text(text):
    return gr.Textbox(value=text, visible=True), gr.Button(value="A ku ku!"), gr.Textbox(value="")

with gr.Blocks() as ui:
    title_1 = gr.Markdown("### Tytuł strony")
    title_2 = gr.Markdown('<p style="text-align: center;">Wyśrodkuje się </p>')
    # Obok siebie, na życzenie grupy (drugi "zniknięty" na początku)
    with gr.Row():
        text_input = gr.Textbox(placeholder="Default text", label="Tu coś wpisujemy")
        text_output = gr.Textbox(visible=False)
    button = gr.Button(value="Inkrementuj")

    text_input.submit(process_text, text_input, [text_output, button, text_input])
    button.click(fn=lambda x: int(x)+1, inputs=text_input, outputs=text_output)

ui.launch()