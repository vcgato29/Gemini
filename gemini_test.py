from vertexai.preview.language_models import ChatModel
from google.oauth2 import service_account
import vertexai

creds = service_account.Credentials.from_service_account_file("gemini-mesh-agent-key.json")
vertexai.init(project="gemini-mesh-poc", location="us-central1", credentials=creds)

chat_model = ChatModel.from_pretrained("chat-bison")
chat = chat_model.start_chat()
response = chat.send_message("What is the role of QSPN in the Netsukuku routing mesh?")
print(response.text)
