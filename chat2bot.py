# Step 1: Expanded Responses Dictionary
responses = {
    "hi": "Hello there! How can I assist you today?",
    "hello": "Hello! How can I help you?",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
    "bye": "Goodbye! Feel free to return if you need more assistance.",
    "help": "Sure! I'm here to help. What do you need assistance with?",
    "pricing": "Our product pricing varies. Please visit our website for detailed information.",
    "hours": "We are open from 9 AM to 5 PM, Monday through Friday.",
    "location": "We are located at 123 Main Street, Springfield.",
    "shipping": "We offer free shipping for orders above $50. You can find more details on our website.",
    "returns": "You can return any item within 30 days of purchase. Would you like to know more about our return policy?",
    "support": "Our support team is available 24/7 via phone or email.",
}


# Step 2: Defining the Function to Get Bot Responses
def get_bot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Handle common greetings
    if "hi" in user_input or "hello" in user_input or "hey" in user_input:
        return responses["hi"]

    # Handle common queries with keywords
    if "how are you" in user_input:
        return responses["how are you"]
    if "price" in user_input or "pricing" in user_input:
        return responses["pricing"]
    if "hours" in user_input or "open" in user_input:
        return responses["hours"]
    if "location" in user_input or "where" in user_input:
        return responses["location"]
    if "shipping" in user_input:
        return responses["shipping"]
    if "returns" in user_input or "return" in user_input:
        return responses["returns"]
    if "support" in user_input or "help" in user_input:
        return responses["support"]

    # Default response if no keywords match
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
