# AI Chatbot using NLP

This project demonstrates how to build a simple **AI Chatbot** using **Natural Language Processing (NLP)** techniques with Python. The chatbot understands user inputs and provides relevant responses using libraries like **NLTK** and **spaCy**.

---

## 🚀 Features

* 🧠 Processes and understands text using NLP
* 💬 Responds intelligently to greetings, questions, and farewells
* ⚙️ Easily customizable intents and responses via a JSON file
* 🧩 Lightweight and extendable Python implementation
* 🗣️ Command-line chat interface (can be integrated into web apps)

---

## 🧱 Project Structure

```
ai-chatbot-nlp/
│
├── README.md                # Documentation file
├── requirements.txt         # Dependencies
├── intents.json             # Predefined intents and responses
│
└── src/
    ├── chatbot.py           # Main chatbot script
    ├── nlp_utils.py         # NLP preprocessing functions
    └── intents_loader.py    # Loads intents from JSON file
```

---

## 📦 Requirements

Add these to your **requirements.txt**:

```
nltk>=3.8
spacy>=3.7
```

Install them with:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt wordnet stopwords
```

---

## 🧩 Example Intents

**intents.json:**

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["hello", "hi", "hey"],
      "responses": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    },
    {
      "tag": "goodbye",
      "patterns": ["bye", "goodbye", "see you later"],
      "responses": ["Goodbye! Have a great day!", "See you soon!"]
    },
    {
      "tag": "thanks",
      "patterns": ["thank you", "thanks"],
      "responses": ["You're welcome!", "Happy to help!"]
    },
    {
      "tag": "name_query",
      "patterns": ["what is your name", "who are you"],
      "responses": ["I'm your friendly NLP chatbot!", "You can call me ChatBot."]
    }
  ]
}
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-chatbot-nlp.git
cd ai-chatbot-nlp
```

2. Install dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt wordnet stopwords
```

3. Run the chatbot:

```bash
python src/chatbot.py
```

4. Start chatting:

```
You: hello
🤖 Chatbot: Hello! How can I assist you today?

You: what is your name
🤖 Chatbot: I'm your friendly NLP chatbot!

You: bye
🤖 Chatbot: Goodbye! Have a great day!
```

---

## 🧠 How It Works

1. **Preprocessing:** The chatbot tokenizes, lemmatizes, and removes stopwords from user input.
2. **Intent Matching:** It checks if user input matches predefined intent patterns.
3. **Response Generation:** A random response from the matched intent is selected.
4. **Fallback:** If no match is found, it asks the user to rephrase.

---

## 🧩 Future Enhancements

* Add **Machine Learning** intent classification using Scikit-learn or Transformers
* Integrate with APIs (e.g., Weather, Wikipedia)
* Create a **Flask or Streamlit** web interface
* Add **contextual memory** for multi-turn conversations


AI Chatbot using NLP  A ready-to-deploy AI Chatbot project built with Python and Natural Language Processing (NLP) libraries such as NLTK and spaCy. This chatbot can understand and respond to user queries with simple intent recognition and keyword-based responses.
