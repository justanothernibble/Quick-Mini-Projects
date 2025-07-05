import requests

from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file
# Now you can access variables
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ----- TOKENISATION -----
import nltk
from nltk.corpus import stopwords
# Create an array of tokens from the string through tokenisation
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def tokeniseAndCleanString(string, token):
    tokens = nltk.word_tokenize(string.lower())
    cleaned_tokens = [token for token in tokens if token not in stop_words]
    return cleaned_tokens


# ----- STEMMING AND RESPONSE GENERATION -----
from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()

response_list = []
string_list = []
def generate_response(string):
    tokenised_and_cleaned = tokeniseAndCleanString(string.lower(), "the")
    stemmed_tokens = [porter_stemmer.stem(token) for token in tokenised_and_cleaned]
    intent_dict = {
    "greeting": ["hello", "hi", "hey", "hola"],
    "farewell": ["bye", "goodbye"],
    "identity": ["name", "your"],
    "weather": ["weather", "temperature"],
    }

    words_to_intent = {}
    for intent, words in intent_dict.items():
        for word in words:
            stemmed_word = porter_stemmer.stem(word)
            words_to_intent[stemmed_word] = intent

    print(words_to_intent)

    intents_found = set()
    for token in stemmed_tokens:
        if token in words_to_intent:
            intents_found.add(words_to_intent[token])



    response = ""
    if "greeting" in intents_found:
        response += "Hello, how's it going? "
    if "identity" in intents_found:
        response += "I am a chatbot, but you can just call me Bob. "
    if "weather" in intents_found:
        try:
            url = f"{BASE_URL}?q=London&appid={API_KEY}&units=metric"
            weather_response = requests.get(url, timeout=5)
            if weather_response.status_code == 401:
                response += "Weather service authentication failed. "
            elif weather_response.status_code == 404:
                response += "Weather for London not found. "
            elif weather_response.status_code == 429:
                response += "Weather service rate limit exceeded. "
            elif weather_response.status_code >= 500:
                response += "Weather service unavailable. "
            else:
                weather_response.raise_for_status()
                data = weather_response.json()
                temp = data.get("main", {}).get("temp")
                desc = data.get("weather", [{}])[0].get("description")
                if temp is not None and desc:
                    response += f"The temperature in London is {temp}°C, and the weather is {desc}. "
                else:
                    response += "Couldn't retrieve weather details. "
        except requests.RequestException:
            response += "Error fetching weather information. "
    if "farewell" in intents_found:
        response += "Goodbye!"

    string_list.append(string)
    response_list.append(response)
