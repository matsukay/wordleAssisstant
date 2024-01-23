# Wordle Assistant

This Python script helps you find possible solutions for the game Wordle by allowing you to specify known letters and their positions.

## Instructions

The script can take either 1 or 2 arguments in addition to the program name.

The first argument is used to specify the letters for which the position within the word is known. All known letters are written with any unknown characters denoted by any non alphabetic character, e.g. '*', '_', or '#'.

The second argument is reserved for letters which are known to be in the word, but their position within the word is unknown. These letters should be written consecutively, e.g., `ab`.

### Example 1:
    py wordleCheat.py ch*** 
  and
    py wordleCheat.py ch###
Both of the above can be used to find all 5 letter words where the first 2 letters are ch.

### Example 2:
    py wordleCheat.py ch*** r
Is used to find all 5 letter words where the first 2 letters are ch and also include the letter r in one of the empty spaces.
