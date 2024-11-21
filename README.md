# gemini-chatbot
This is a chat bot web application based on Gemini

Steps to follow 
1. Clone the repository 

2. Create a root folder or directory and paste all the files and folders as shown below

gemini-chatbot/
│
├── app/
│   ├── __init__.py (optional)
│   ├── main.py
│   ├── chatbot.py
│   └── templates/
│       └── index.html
│
├── .env
└── run.py


2. Paste your google gemini api key in the .env file as 
   GEMINI_API_KEY = "your_api_key_here"

3. Run commands in your Terminal one by one as
    pip install google-generativeai flask python-dotenv
    python run.py
