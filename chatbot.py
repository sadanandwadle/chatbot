print("Chatbot: Hello! I am a simple chatbot.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hi!")

    elif user == "how are you":
        print("Chatbot: I am fine.")

    elif user == "what is your name":
        print("Chatbot: I am a chatbot.")

    elif user == "bye":
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
