# chatbot.py
"""
AI Chatbot with NLP
-------------------
A simple chatbot built using Python and NLTK.
It uses text preprocessing and pattern matching to respond to user queries.
"""

import nltk
import random
import string
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download necessary data
nltk.download('punkt')
nltk.download('wordnet')

# Sample corpus for chatbot training
corpus = """
Hello! How are you?
Hi there!
I am a chatbot created using NLP.
How can I help you today?
I can answer simple questions about AI and Python.
Artificial Intelligence is the simulation of human intelligence by machines.
Python is a popular programming language used for data science and AI.
Goodbye!
See you later!
"""

# Tokenize the text
sent_tokens = nltk.sent_tokenize(corpus)

lemmatizer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token.lower()) for token in tokens if token not in string.punctuation]

def respond(user_input):
    user_input = user_input.lower()
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good evening']
    responses = ['Hello!', 'Hi there!', 'Hey!', 'Hi, how can I assist you?']
    
    # Greeting response
    if user_input in greetings:
        return random.choice(responses)
    
    # Check for keywords
    elif 'python' in user_input:
        return "Python is a high-level, interpreted programming language widely used in AI and data science."
    elif 'ai' in user_input or 'artificial intelligence' in user_input:
        return "Artificial Intelligence is the ability of a machine to mimic human behavior."
    elif 'your name' in user_input:
        return "I’m your friendly AI chatbot!"
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure I understand that. Can you rephrase?"

# Chat loop
print("🤖 Chatbot: Hello! I'm your AI Chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("🤖 Chatbot: Goodbye! 👋")
        break
    else:
        print("🤖 Chatbot:", respond(user_input))
