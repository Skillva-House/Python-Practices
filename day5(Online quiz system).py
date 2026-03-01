#  Online Quiz System

# List of questions
questions = [
    "1. What is the capital of Pakistan?",
    "2. How many continents are there?",
    "3. What is 5 + 7?"
]

# List of correct answers
answers = ["Islamabad", "7", "12"]

score = 0

print("Welcome to the Quiz!\n")

# Loop through questions
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")

    # Conditional statement
    if user_answer.strip().lower() == answers[i].lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

# Final Score
print("Quiz Finished!")
print("Your Score:", score)

# Grade using conditional statements
if score == 3:
    print("Grade: A")
elif score == 2:
    print("Grade: B")
elif score == 1:
    print("Grade: C")
else:
    print("Grade: Fail")
