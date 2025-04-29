def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you?": "I'm just a program, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

def main():
    print("Welcome to the Simple Python Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()