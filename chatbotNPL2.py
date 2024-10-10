import spacy

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

# Step 1: Expanded Responses Dictionary
responses = {
    "greeting": "Hello there! How can I assist you today?",
    "how_are_you": "I'm just a bot, but I'm doing great! How can I assist you?",
    "goodbye": "Goodbye! Feel free to return if you need more assistance.",
    "pricing": "Our product pricing varies. Please visit our website for detailed information.",
    "hours": "We are open from 9 AM to 5 PM, Monday through Friday.",
    "location": "We are located at 123 Main Street, Springfield.",
    "shipping": "We offer free shipping for orders above $50. You can find more details on our website.",
    "returns": "You can return any item within 30 days of purchase. Would you like to know more about our return policy?",
    "support": "Our support team is available 24/7 via phone or email.",
    "what_are_you_doing": "I'm just here, ready to assist you with anything you need!"
}


# Step 2: Use spaCy for Natural Language Processing
def get_bot_response(user_input):
    # Analyze the input using spaCy
    doc = nlp(user_input.lower())

    # Check for specific intents based on tokens or entities
    if any(token.lemma_ in ["hello", "hi", "hey", "morning", "afternoon", "evening"] for token in doc):
        return responses["greeting"]

    if any(token.lemma_ in ["bye", "goodbye"] for token in doc):
        return responses["goodbye"]

    if any(token.lemma_ in ["price", "pricing"] for token in doc):
        return responses["pricing"]

    if any(token.lemma_ in ["hour", "open", "opening"] for token in doc):
        return responses["hours"]

    if any(token.lemma_ in ["location", "where"] for token in doc):
        return responses["location"]

    if any(token.lemma_ in ["ship", "shipping"] for token in doc):
        return responses["shipping"]

    if any(token.lemma_ in ["return", "returns"] for token in doc):
        return responses["returns"]

    if any(token.lemma_ in ["support", "help"] for token in doc):
        return responses["support"]

    if any(token.lemma_ in ["how", "feel", "are", "you"] for token in doc):
        return responses["how_are_you"]

    if any(token.lemma_ in ["do", "doing"] for token in doc):
        return responses["what_are_you_doing"]

    # Default fallback if no keyword is detected
    return None


# Step 3: Implementing the Main Chat Loop with Escalation Feature
def chatbot():
    fallback_count = 0  # Count of fallback responses for unknown inputs
    max_fallbacks = 3  # Max allowed fallback responses before escalation

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the loop if the user types 'quit'
        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break

        # Get the bot response
        response = get_bot_response(user_input)

        # If the bot doesn't understand the user input
        if response is None:
            fallback_count += 1
            if fallback_count >= max_fallbacks:
                print("Bot: I'm having trouble understanding. Would you like to speak to a human representative?")
                fallback_count = 0  # Reset the counter after offering to escalate
            else:
                print("Bot: I'm not sure how to respond to that. Can you try asking something else?")
        else:
            print(f"Bot: {response}")
            fallback_count = 0  # Reset fallback count on successful response


# Running the chatbot
chatbot()
