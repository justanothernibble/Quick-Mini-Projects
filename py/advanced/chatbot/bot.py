conversation_count = 0

def tokeniseAndCleanString(string, token):
    import nltk
    from nltk.corpus import stopwords
    # Create an array of tokens from the string through tokenisation

    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    tokens = nltk.word_tokenize(string.lower())
    cleaned_tokens = [token for token in tokens if token not in stop_words]
    return cleaned_tokens



def generate_response(string):
    from nltk.stem import PorterStemmer
    porter_stemmer = PorterStemmer()
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
            words_to_intent[word] = intent

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
        response += "I do not know the weather at the moment. "
    if "farewell" in intents_found:
        response += "Goodbye!"


    return response