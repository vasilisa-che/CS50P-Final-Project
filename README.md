# CS50P-Final-Project
The Final Project of the CS50P online course  – the console version of the Wordle game

## Description
This is a final project for HarvardX CS50P course (CS50's Introduction to Programming with Python). This console game Wordle was made by Vasilisa Chebotareva.

In this game you should guess the 5-letter word in 6 tries. The word is a singular noun, where letters can be repeated.

After every attempt the user sees colored guess distribution.
- If the letter is in the word and in the right spot, it turns green 🟩
- If the letter is in the word but in the wrong spot, it turns yellow 🟨
- If the letter is not in the world, it turns white ⬜

In this program I tried to prevent potential mistakes and added some features.
1. A target word (which user should guess) is picked randomly from the .txt file with 5-letter nouns.
2. The user's guess word is checked to be a 5-letter word.
3. The user's guess word is checked to be a singular noun in [Free Dictionary API](https://dictionaryapi.dev/).
4. Identical letters in words are controlled. For example, in a guess word there are two identical letters (letter *a* in the word *award*). The target word is *brain*. So, in the program the first letter *a* turns white (not yellow) and the second *a* turns green (because it is in the right spot).
5. After printing the user's name a stopwatch starts and goes till the victory or last try.
6. When the game is over, the user can copy guess disrtubution made with emoji.

## Installation
It's recommended to first create a python virtual environment and then install the requirements with the following command:
```
pip3 install -r requirements.txt
```

Then run the command:
```
python project.py
```

## Tech used
Python

## Main files

- project.py - main file with the game
- test_project.py - three tests of the main program's functions
- five-letter-words.txt - the list with 5-letter nouns.

## Video Demo


## Acknowledgments

I would like to express my deepest appreciation to David Malan and the whole CS50 team for entertaining lectures and helpful problem sets. 
