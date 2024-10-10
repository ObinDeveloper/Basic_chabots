# Step 1: Defining the Responses Dictionary
responses = {
    "hi": "Hello there! How can I assist you today?",
    "how are you": "I'm a bot, so I don't have feelings, but I'm functioning properly!",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure, I can help you. What do you need assistance with?",
}


# Step 2: Defining the Function to Get Bot Responses
def get_bot_response(user_input):
    # Convert user input to lowercase to make it case-insensitive
    user_input = user_input.lower()
    # Fetch response from dictionary, return default message if not found
    return responses.get(user_input, "I'm not sure how to respond to that. Can you try asking something else?")


# Step 3: Running the Main Chat Loop
while True:
    # Get user input
    user_input = input("You: ")

    # Exit loop if the user types 'quit'
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    # Get bot response and print it
    response = get_bot_response(user_input)
    print(f"Bot: {response}")
