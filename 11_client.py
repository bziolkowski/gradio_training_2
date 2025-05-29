from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		text="Hello!!",
		history=[],
		api_name="/respond"
)
print(result)