import random

responses = {
    "hello": [
        "Hello! How are you?",
        "Hi! Nice to meet you.",
        "Hello! How can I help you?"
    ],

    "how are you": [
        "I am fine!",
        "I am doing great!",
        "I am good, thank you!"
    ],

    "name": [
        "My name is CollegeBot.",
        "You can call me CollegeBot."
    ],

    "study": [
        "Regular practice is the key to success.",
        "Make a timetable and study daily."
    ],

    "bye": [
        "Goodbye!",
        "See you later!",
        "Have a nice day!"
    ]
}


def chatbot():
    print("===== COLLEGE CHATBOT =====")
    print("Type 'bye' to exit.")

    while True:
        message = input("\nYou: ").lower()

        found = False

        for keyword in responses:

            if keyword in message:

                reply = random.choice(responses[keyword])

                print("Bot:", reply)

                found = True

                if keyword == "bye":
                    return

                break

        if not found:
            print(
                "Bot: Sorry, I don't understand that."
            )


chatbot()
