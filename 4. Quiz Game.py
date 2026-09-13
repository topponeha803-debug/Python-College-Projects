questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit",
                    "B. Computer Personal Unit",
                    "C. Central Program Unit",
                    "D. Control Processing Unit"],
        "answer": "A"
    },
    {
        "question": "Which language is used in this project?",
        "options": ["A. Java",
                    "B. Python",
                    "C. C++",
                    "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which device is used to enter data?",
        "options": ["A. Monitor",
                    "B. Printer",
                    "C. Keyboard",
                    "D. Speaker"],
        "answer": "C"
    },
    {
        "question": "What is the brain of computer?",
        "options": ["A. RAM",
                    "B. CPU",
                    "C. ROM",
                    "D. Hard Disk"],
        "answer": "B"
    },
    {
        "question": "Which one is an operating system?",
        "options": ["A. Windows",
                    "B. Python",
                    "C. Google",
                    "D. HTML"],
        "answer": "A"
    }
]

score = 0

print("===== PYTHON QUIZ GAME =====")

for number, q in enumerate(questions, start=1):

    print("\nQuestion", number)
    print(q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")

print("\n===== RESULT =====")
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)

percentage = score / len(questions) * 100

print("Score:", round(percentage, 2), "%")

if percentage >= 80:
    print("Excellent Performance!")
elif percentage >= 50:
    print("Good Performance!")
else:
    print("Need More Practice!")
