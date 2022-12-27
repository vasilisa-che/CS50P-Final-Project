"""This is a final project for HarvardX CS50P course (CS50's Introduction to Programming with Python)
This terminal version of the Wordle game was made by Vasilisa Chebotareva"""

import random
import requests
from rich.console import Console
from rich.markdown import Markdown
from rich.theme import Theme
from stopwatch import Stopwatch


def instructions():
    game_rules = """
# WORDLY
## HOW TO PLAY

Guess the 5-letter word in 6 tries. The word should be a singular noun.
Letters can be repeated in the word.
The color of the tiles changes after every guess.

## COLOR CODES
- If the letter is in the word and in the right spot, it turns green 🟩
- If the letter is in the word but in the wrong spot, it turns yellow 🟨
- If the letter is not in the word, it turns white ⬜
---
"""

    console = Console()
    rules = Markdown(game_rules)
    console.print(rules)


def target_word():
    """
    return the target word which user has to guess
    """
    with open("five-letter-words.txt") as file:
        words = []
        for line in file:
            words.append(line.rstrip())
        word = random.choice(words)
    return word


def users_guess():
    """
    check whether the user printed a 5-letter word
    """
    guess = input("\nYour guess: ").strip().lower()
    return check_users_guess(guess)


def check_users_guess(guess):
    if not guess.isalpha():
        print("Your word must contain letters and no other symbols. Try again!")
        return users_guess()

    if len(guess) != 5:
        print("The word length is not equal 5. Try again!")
        return users_guess()
    """
    check whether the user printed a singular noun
    """
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + guess
    res = requests.get(url)
    data = res.json()
    part_of_speech = []
    try:
        for i in data:
            for j in i["meanings"]:
                part_of_speech.append(j["partOfSpeech"])
        if "noun" not in part_of_speech:
            print("The word is not a common singular noun. Try again!")
            return users_guess()
    except TypeError:
        print("The word is not in the dictionary. Try again!")
        return users_guess()

    return guess


def compare_words(target, guess, letters, i):
    guess_progress = ""
    for n in range(5):
        if guess[n] == target[n]:
            guess_progress += guess[n]
        elif guess[n] not in target:
            guess_progress += " "

    for n in range(5):
        if guess[n] == target[n]:
            x = " " + guess[n] + " "
            letters[i][n] = {x: "correct"}
        elif guess[n] in target and (target.count(guess[n]) - guess_progress.count(guess[n])) >= 1:
            x = " " + guess[n] + " "
            letters[i][n] = {x: "wrong"}
        else:
            x = " " + guess[n] + " "
            letters[i][n] = {x: "unable"}

    return letters


def compare_words_emoji(target, guess, emoji, i):
    guess_progress = ""
    for n in range(5):
        if guess[n] == target[n]:
            guess_progress += guess[n]
        elif guess[n] not in target:
            guess_progress += " "

    for n in range(5):
        if guess[n] == target[n]:
            emoji[i][n] = "🟩"
        elif guess[n] in target and (target.count(guess[n]) - guess_progress.count(guess[n])) >= 1:
            emoji[i][n] = "🟨"

    return emoji


def end_screen_victory(target, duration_is_sec, name):
    min = f"{duration_is_sec // 60:.0f}"
    if min == "1":
        minutes = min + " minute"
    else:
        minutes = min + " minutes"
    sec = f"{duration_is_sec % 60:.0f}"
    if sec == "1":
        seconds = sec + " second"
    else:
        seconds = sec + " seconds"
    congrats = f"""
# 🎊 {name.upper()}, YOU GUESSED THE WORD "{target.upper()}" in {minutes} {seconds} 🎊
## GUESS DISTRIBUTION
"""

    console = Console()
    cn = Markdown(congrats)
    console.print(cn)


def end_screen_loss(target, duration_is_sec, name):
    min = f"{duration_is_sec // 60:.0f}"
    if min == "1":
        minutes = min + " minute"
    else:
        minutes = min + " minutes"
    sec = f"{duration_is_sec % 60:.0f}"
    if sec == "1":
        seconds = sec + " second"
    else:
        seconds = sec + " seconds"
    result = f"""
# ❌ {name.upper()}, YOU DIDN'T GUESS THE WORD "{target.upper()}" ❌
## GAME DURATION: {minutes} {seconds}
---
## GUESS DISTRIBUTION
"""

    console = Console()
    rs = Markdown(result)
    console.print(rs)


def main():
    """ print the game rules """
    instructions()

    """ start the game """
    name = input("PRINT YOUR NAME TO START THE GAME: ")
    line = """
---
"""
    console = Console()
    line_p = Markdown(line)
    console.print(line_p)

    stopwatch = Stopwatch(2)

    """ set the target word from the .txt file """
    target = target_word()

    """ set the guess distribution """
    custom_theme = Theme({
        "correct": "bold white on green",
        "wrong": "bold white on yellow",
        "unable": "bold white on white",
        "default": "bold black on black"
    })
    console_theme = Console(theme=custom_theme)
    letters = [[{"   ": "default"} for i in range(5)] for j in range(6)]
    emoji = [["⬜", "⬜", "⬜", "⬜", "⬜"] for _ in range(6)]

    """ guessing the word in six tries """
    for i in range(6):
        intro = f"""
# ROUND {i + 1}

        """
        round_n = Markdown(intro)
        console.print(round_n)

        """show all attempts"""
        for word in letters:
            for letter in word:
                for key, value in letter.items():
                    console_theme.print(key.upper(), style=value, end="")
                    console_theme.print(" ", end="")
            print()

        guess = users_guess()
        letters = compare_words(target, guess, letters, i)
        emoji = compare_words_emoji(target, guess, emoji, i)
        if target == guess:
            break

    stopwatch.stop()
    duration_is_sec = stopwatch.duration

    if target == guess:
        end_screen_victory(target, duration_is_sec, name)

    else:
        end_screen_loss(target, duration_is_sec, name)

    """ show guess distribution and emoji result"""
    for word in letters:
        for letter in word:
            for key, value in letter.items():
                console_theme.print(key.upper(), style=value, end="")
                console_theme.print(" ", end="")
        print()


    x = """
## COPY YOUR EMOJI RESULT
"""
    copy_e = Markdown(x)
    console.print(copy_e)

    for i in emoji:
        console.print(*i)


if __name__ == "__main__":
    main()
