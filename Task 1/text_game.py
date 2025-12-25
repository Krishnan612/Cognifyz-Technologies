import random
import sys
import os
import json
from datetime import datetime
QUIZ = "quiz.json"
SCORES = "scores.json"
def get_num(prompt, min_val=None, max_val=None):
    while True:
        try:
            v = int(input(prompt))
            if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                print("Please enter a valid number.")
                continue
            return v
        except ValueError:
            print("Not a number, try again.")
def load_questions(path=None):
    default_questions = [
        {"q": "What is the capital of France?", "opts": {"a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome"}, "ans": "c"},
        {"q": "Which number is prime?", "opts": {"a": "15", "b": "17", "c": "21", "d": "27"}, "ans": "b"},
        {"q": "Which language is primarily used for styling web pages?", "opts": {"a": "HTML", "b": "Python", "c": "CSS", "d": "C++"}, "ans": "c"},
        {"q": "What does CPU stand for?", "opts": {"a": "Central Processing Unit", "b": "Computer Primary Unit", "c": "Central Program Unit", "d": "Control Processing Unit"}, "ans": "a"},
        {"q": "Which planet is known as the Red Planet?", "opts": {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Venus"}, "ans": "b"},
        {"q": "What is 8 * 7?", "opts": {"a": "54", "b": "56", "c": "58", "d": "60"}, "ans": "b"},
    ]
    p = path or QUIZ
    if p and os.path.exists(p):
        try:
            with open(p, "r") as f:
                data = json.load(f)
            if isinstance(data, list):
                print(f"Loaded {len(data)} question(s) from {p}.")
                return data
            print("Quiz file has bad format;So using defaults.")
        except Exception:
            print("Could not read quiz file;So using defaults.")
    return default_questions
def load_scores():
    if os.path.exists(SCORES):
        try:
            with open(SCORES, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}
def save_scores(data):
    try:
        with open(SCORES, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        print("Could not save scores.")
def show_scores():
    data = load_scores()
    print("\n--- Scores ---")
    g = data.get("guessing_game")
    if g:
        print(f"Guessing - {g.get('name')} in {g.get('attempts')} tries on {g.get('date')}")
    else:
        print("Guessing - no record.")
    q = data.get("quiz_game")
    if q:
        print(f"Quiz - {q.get('name')} {q.get('score')}/{q.get('total')} on {q.get('date')}")
    else:
        print("Quiz - no record.")
    print()
def clear_scores():
    c = input("Clear all scores? (y/n): ").strip().lower()
    if c == "y":
        save_scores({})
        print("Scores cleared.")
    else:
        print("Scores kept.")
def update_guess_score(attempts):
    data = load_scores()
    cur = data.get("guessing_game")
    if attempts is None:
        return
    if cur is None or attempts < cur.get("attempts", 999999):
        name = input("New record! Name: ").strip() or "Anon"
        data["guessing_game"] = {"name": name, "attempts": attempts, "date": datetime.now().isoformat()}
        save_scores(data)
        print("Saved.")
def update_quiz_score(score, total):
    data = load_scores()
    cur = data.get("quiz_game")
    if cur is None or score > cur.get("score", -1):
        name = input("New record! Name: ").strip()
        data["quiz_game"] = {"name": name, "score": score, "total": total, "date": datetime.now().isoformat()}
        save_scores(data)
        print("Saved.")
def guess_game():
    print("\n--- Guess the number ---")
    print("1) Easy 1-20 (8 tries)")
    print("2) Normal 1-100 (7 tries)")
    print("3) Hard 1-1000 (6 tries)")
    d = input("Pick 1/2/3: ").strip()
    if d == "1":
        low, high, tries = 1, 20, 8
    elif d == "3":
        low, high, tries = 1, 1000, 6
    else:
        low, high, tries = 1, 100, 7

    secret = random.randint(low, high)
    i = 0
    while i < tries:
        left = tries - i
        g = get_num(f"{left} chance left. Guess the number ({low}-{high}): ", low, high)
        i += 1
        if g == secret:
            print("You guessed it in", i, "tries")
            update_guess_score(i)
            break
        if g > secret:
            print("you'r guess is Higher")
        else:
            print("you'r guess is Lower")
    else:
        print("Out of tries, the number was", secret)
    print()
def quiz():
    print("\n--- Quiz Game ---")
    q = load_questions()
    total = len(q)
    s = 0
    for i, item in enumerate(q, start=1):
        print("\n", i, ")", item['q'])
        for k, v in item['opts'].items():
            print(" ", k, v)
        while True:
            a = input("Answer (a/b/c/d): ").strip().lower()
            if a in item['opts']:
                break
            print("a/b/c/d only")
        if a == item['ans']:
            print("Yes, Correct Answer!")
            s += 1
        else:
            print("No, correct Answer is", item['ans'])
    print("\nScore:", s, "/", total)
    update_quiz_score(s, total)
def menu():
    while True:
        print("\nMenu")
        print("1) Guess")
        print("2) Quiz")
        print("3) Scores")
        print("4) Clear scores")
        print("5) Quit")
        c = input("Pick: ").strip()
        if c == "1":
            guess_game()
        elif c == "2":
            quiz()
        elif c == "3":
            show_scores()
        elif c == "4":
            clear_scores()
        elif c == "5":
            print("Bye, Thank you for playing!")
            sys.exit(0)
        else:
            print("Pick 1-5")
def main():
    print("Text Games")
    menu()
if __name__ == "__main__":
    main()