from revChatGPT.revChatGPT import Chatbot
import os

config = {
    "email": os.environ["EMAIL"],
    "password": os.environ["PASSWORD"],
    "session_token": os.environ["SESSION_TOKEN"],
}

chatbot = Chatbot(config, conversation_id=None)
chatbot.refresh_session()

def handle_response(prompt) -> str:
    response = chatbot.get_chat_response(prompt, output="text")
    responseMessage = response['message']

    return responseMessage
