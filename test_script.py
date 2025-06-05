from google.ai import generativelanguage as glm
from google.api_core.client_options import ClientOptions
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client_options = ClientOptions(api_key=api_key)
client = glm.ServicesClient(client_options=client_options)

models = client.list_models()
print("Available models:")
for model in models:
    print(model.name)
