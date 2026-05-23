import time
import sys
import datetime

def typing_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_response(user_input):
    user_input = user_input.lower().strip()

    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hi there! How can I help you?"

    elif any(word in user_input for word in ["how are you", "how r you", "how are u"]):
        return "I'm fine, thanks! What about you?"

    elif any(word in user_input for word in ["your name", "who are you", "what's your name"]):
        return "I'm a simple rule-based chatbot!"

    elif any(word in user_input for word in ["time", "what time"]):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return "The current time is " + current_time

    elif any(word in user_input for word in ["thank you", "thanks", "thx"]):
        return "You're welcome!"

    elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Have a nice day!"

    else:
        return "I didn't understand that. Please try again."

def chat():
    print("Chatbot is ready! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)
        sys.stdout.write("Bot: ")
        typing_effect(response)

        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break

chat()