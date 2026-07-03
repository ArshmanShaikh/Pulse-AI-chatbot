def PulseAI():
    print("=" * 70)
    print("Hey! I am your Pulse-AI 🤖. How may I help you?")
    print("=" * 70)

    responses = {
        "hello": "Hey there! How can I help you?",
        "hi": "Hello! Nice to meet you!",
        "hey": "Hey! What's up?",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "See you later! Take care!",
        "what is your name?": "My name is Pulse-AI!",
        "who are you?": "I am DecoBot, a rule-based AI chatbot!",
        "how are you?": "I am doing great, thank you for asking!",
        "age?": "I was just created, so I am brand new!",
        "who made you?": "I was built by a DecodeLabs intern!",
        "help": "I can answer basic questions. Just type something!",
        "what can you do?": "I can chat with you using predefined rules!",
        "thanks": "You're welcome!",
        "thank you": "Happy to help!",
        "good morning": "Good Morning! Hope you have a wonderful day!",
        "good night": "Good Night! Sleep well!",
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
        "fact": "Did you know? Python was named after Monty Python, not the snake!"
    }

    while True:
        user = input("You: ").strip().lower()

        if user == "":
            print("Pulse-AI: Please type something!")
            continue

        if user in ["exit", "quit", "bye"]:
            print("Pulse-AI: Goodbye! 👋")
            break

        print("Pulse-AI:", responses.get(user, "Sorry, I didn't understand that. Please try again."))
        print()


if __name__ == "__main__":
    PulseAI()