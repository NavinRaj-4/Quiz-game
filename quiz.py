questions = {
    "What is the capital of India?": "Delhi",
    "What is 5 + 3?": "8",
    "What is the color of sky?": "Blue",
    "Which language is used for AI?": "Python"
}

score = 0

print("\n===== QUIZ GAME =====")

for question, answer in questions.items():
    print("\n" + question)
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", answer)

print("\n===== RESULT =====")
print("Your Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! 🎉")
elif score >= 2:
    print("Good job 👍")
else:
    print("Keep practicing 💪")