def history_quiz():
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
