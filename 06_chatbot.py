import gradio
import gradio as gr
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    azure_endpoint="https://oai-isdd-swedencentral.openai.azure.com",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2025-03-01-preview",
    azure_deployment="isdd-gpt-4o-2024-11-20-gs",
)

def respond(text, history):
    conversation = []
    conversation.extend(history)
    conversation.append(
        {"role": "user", "content": text})

    response = client.chat.completions.create(
        model = "isdd-gpt-4o-2024-11-20-gs",
        messages=conversation
    )
    conversation.append(
        {"role": "assistant", "content": response.choices[0].message.content}
    )
    return conversation

def respond_stream(text, history):
    conversation = []
    conversation.extend(history)
    conversation.append(
        {"role": "user", "content": text})
    stream = client.chat.completions.create(
        model = "isdd-gpt-4o-2024-11-20-gs",
        messages=conversation,
        stream=True
    )
    conversation.append({"role": "assistant", "content": ""})

    for chunk in stream:
        if chunk.choices:
            if chunk.choices[0].delta.content is not None:
                chunk_text = chunk.choices[0].delta.content
                conversation[-1]["content"] += chunk_text
                yield conversation

def feedback(vote: gr.LikeData):
    print(f"Vote received. Liked: {vote.liked}")
    print(f"Index of the message with feedback: {vote.index}")
    print(f"Message content: {vote.value}")


def clear_input(text):
    return "", text

with gr.Blocks(css="footer{display:none !important}") as ui:
    chatbot = gr.Chatbot(type="messages")
    input = gr.Textbox()
    input_memory = gr.State("")

    # input.submit(fn=respond, inputs=[input, chatbot], outputs=chatbot, show_progress='minimal')
    input.submit(fn=clear_input, inputs=input, outputs=[input, input_memory]).then(fn=respond_stream, inputs=[input_memory, chatbot], outputs=chatbot, show_progress='minimal')
    chatbot.like(fn=feedback)

ui.launch()

# Uruchomienie serwera z dodatkowymi parametrami
# ui.launch(server_name="0.0.0.0", auth=[("admin", "admin")], auth_message="Zaloguj się", root_path="/app", pwa=True)