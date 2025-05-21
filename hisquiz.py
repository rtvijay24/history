define history_quiz():
    """Main function placeholder for History Quiz."""
    pass
def print_banner():
    print("Welcome to the History Quiz!")


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m']

def print_banner():
    print(CYAN + "\n🏺 Welcome to the History Quiz! 🏺\n" + RESET)

    def print_question(q, options):
    print(YELLOW + q + RESET)
    for key, val in options.items():
        print(f"  {key}) {val}")

def get_valid_input():
    while True:
        ans = input("Enter your answer (a/b/c/d): ").lower()
        if ans in ['a', 'b', 'c', 'd']:
            return ans
        print(RED + "Invalid input, try again." + RESET)
def ask_question(question, options, correct):
    print_question(question, options)
    answer = get_valid_input()
    if answer == correct:
        print(GREEN + "Correct!\n" + RESET)
        return True
    else:
        print(RED + f"Wrong! Correct answer is '{correct}'.\n" + RESET)
        return False


def question1():
    return ask_question(
        "Who was the first President of the United States?",
        {'a': 'George Washington', 'b': 'Thomas Jefferson', 'c': 'Abraham Lincoln', 'd': 'John Adams'},
        'a'
    )
def question2():
    return ask_question(
        "In which year did World War II end?",
        {'a': '1942', 'b': '1945', 'c': '1939', 'd': '1950'},
        'b'
    )
def question3():
    return ask_question(
        "The Great Wall of China was primarily built to protect against which group?",
        {'a': 'Mongols', 'b': 'Romans', 'c': 'Vikings', 'd': 'Ottomans'},
        'a'
    )
    
def question4():
    return ask_question(
        "Who discovered America in 1492?",
        {'a': 'Ferdinand Magellan', 'b': 'Christopher Columbus', 'c': 'Vasco da Gama', 'd': 'James Cook'},
        'b'
    )
def question5():
    return ask_question(
        "Which empire was ruled by Julius Caesar?",
        {'a': 'Greek Empire', 'b': 'Egyptian Empire', 'c': 'Roman Empire', 'd': 'Persian Empire'},
        'c'
    )
questions = [question1, question2, question3, question4, question5]
def run_history_quiz():
    print_banner()
    score = 0
    for q in questions:
        if q():
            score += 1
    print(f"You scored {score}/{len(questions)}!")
import time

def loading():
    print("Loading questions", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
def run_history_quiz():
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    print(f"You scored {score}/{len(questions)}!")
def show_score(score, total):
    print(f"\nYou scored {score}/{total}!")
    if score == total:
        print("🏆 Excellent! Perfect score!")
    elif score >= total * 0.6:
        print("👍 Good job!")
    else:
        print("📘 Keep learning!")
def run_history_quiz():
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    show_score(score, len(questions))
def ask_replay():
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer == 'y':
        run_history_quiz()
    else:
        print("Thanks for playing!")
def run_history_quiz():
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    show_score(score, len(questions))
    ask_replay()
def run_history_quiz():
    """Run the full history quiz with questions, scoring, and replay."""
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    show_score(score, len(questions))
    ask_replay()

def ask_question(question, options, correct):
    """
    Display a question and options, validate input, and return True if correct.
    """
    print_question(question, options)
    answer = get_valid_input()
    if answer == correct:
        print(GREEN + "Correct!\n" + RESET)
        return True
    else:
        print(RED + f"Wrong! Correct answer is '{correct}'.\n" + RESET)
        return False
def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting.")
        exit()
def get_valid_input():
    while True:
        ans = safe_input("Enter your answer (a/b/c/d): ").lower()
        if ans in ['a', 'b', 'c', 'd']:
            return ans
        print(RED + "Invalid input, try again." + RESET)

define ask_replay():
    answer = safe_input("Do you want to play again? (y/n): ").lower()
    if answer == 'y':
        run_history_quiz()
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    run_history_quiz()
"""
History Quiz Module
Includes a multiple-choice history quiz game with scoring and replay.
"""

import time (for timer )

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
