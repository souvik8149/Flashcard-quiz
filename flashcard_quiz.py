"""
flashcard_quiz.py

A simple CLI flashcard quiz app that asks the user 4 fun questions.
It tracks your score, shows correct answers if you get them wrong,
and lets you play again as many times as you want!
"""


def flashcard_quiz():
    """
    Runs the flashcard quiz:
    - Loops through predefined questions
    - Takes user input (case insensitive)
    - Shows correct/incorrect feedback
    - Tracks and displays total score
    - Option to play again
    """

    quiz = [
        {"question": "What is the capital of France? =", "answer": "Paris"},
        {"question": "2 + 2 = ", "answer": "4"},
        {"question": "Your nickname ? , Hint(Munn_) =  ", "answer": "Munni"},
        {"question": "Which language are we coding in? = ", "answer": "Python"}
    ]

    print("\n" + "-" * 70)
    print("   Welcome to Flashcard quize let's see how intelligent you are 🧠 ") 
    print("-" * 70 + "\n")

    while True:
        score = 0

        for item in quiz:
            user = input(item["question"] + " ").strip().lower()
            if user == item["answer"].strip().lower():
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong answer the right answer is {item['answer']}\n")

        print(f"You got {score} out of {len(quiz)} correct!")

        while True:
            play_again = input("Wanna play again y/n : ")
            if play_again in ["yes" , "y" , "no" , "n"]:
                break
            print("Invalid choice.. Choose y/n")
        if play_again in ["n" , "no"]:
            print("\n" + "-" * 40)
            print("    Thanks for playing, 👋 Goodbye!")
            print("-" * 40)
            break
        print("\n")

if __name__ == "__main__":
    flashcard_quiz()