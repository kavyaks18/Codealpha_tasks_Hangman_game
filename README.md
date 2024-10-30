# Hangman Game

This project is a Python implementation of the classic Hangman game. The objective is to guess a secret word, one letter at a time, with a limited number of incorrect guesses allowed.

## Table of Contents
- [Features](#features)
- [Game Rules](#game-rules)
- [How to Play](#how-to-play)
- [Customization](#customization)
- [Example Output](#example-output)

## Features
- Random word selection from a predefined list of words.
- Dynamic display of the word’s progress with blanks (`_`) for unguessed letters.
- Player gets feedback for correct and incorrect guesses.
- Visual representation of a "hangman" as the player makes incorrect guesses.
- Game ends when the player guesses the word or exhausts all allowed incorrect guesses.

## Game Rules
- The player must guess the word by guessing one letter at a time.
- Each correct guess reveals the corresponding letter in the word.
- Each incorrect guess brings the player closer to "losing" by drawing part of the hangman.
- The game is over when the player either guesses all the letters or makes 6 incorrect guesses.

## How to Play
- After running the game, the program will randomly choose a word from a predefined list.
- You will be shown the number of letters in the word, and your job is to guess letters one by one.
- If your guess is correct, the letter will be revealed in the word.
- If your guess is incorrect, part of the hangman will be drawn.
- You have a total of 6 incorrect guesses before the game ends.
- The game will display whether you've won or lost at the end.


## Customization
You can modify the list of words the game selects from by changing the `words` list in the `hangman.py` file. Simply add or remove words as desired:
```python
words = ['python', 'developer', 'hangman', 'programming', 'algorithm', 'function', 'variable']
```

## Example Output
```python
Welcome to Hangman!
The word has 7 letters.

_ _ _ _ _ _ _ 
Incorrect guesses left: 6
Guessed letters: 

Guess a letter: p
Good guess! 'p' is in the word.

p _ _ _ _ _ _ 
Incorrect guesses left: 6
Guessed letters: p
```
