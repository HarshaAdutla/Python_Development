# Hangman Game
import random

words = ["namaste", "welcome", "something", "nothing"]
word = random.choice(words)
word_count = len(word)
print(word)
# print(type(word_count))
masked_word = "_"*len(word)
print(masked_word)
attempts = 6
letter = input("Guess a letter!\n")
# if letter in word:
while attempts > 0:
    if letter in word:
        new_word = word.replace("_", letter)
        break
    else:
        attempts -= 1


