import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GeminiBot:
    def __init__(self):
        # Configure API key
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        
        # Create model instance
        self.model = genai.GenerativeModel('gemini-pro')
        
        # Start chat
        self.chat = self.model.start_chat(history=[])
    
    def generate_response(self, user_message):
        try:
            # Generate response
            response = self.chat.send_message(user_message)
            return response.text
            
        except Exception as e:
            return f"An error occurred: {str(e)}"
    
    def reset_conversation(self):
        # Reset chat history
        self.chat = self.model.start_chat(history=[])
        return "Conversation reset successfully"