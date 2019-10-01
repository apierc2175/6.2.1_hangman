#needs to choose a random word
#needs to give you a certain amount of guesses to guess the word
# needs to say what letters you got right and what ones wrong
#the letters you got right must stay on screen
import random

words = ["program", "coding", "carolina", "circus", "popcorn"]
print("play hangman the answer will be one of the following words! " + str(words))
rand_num = random.randint(1,len(words) - 1)
rand_word = words[rand_num]
rand_word_length = len(rand_word)
guesses_left = 5
print(rand_word)
print("the word is " + str(rand_word_length) + " letters long")

letter_guess = input("Guess a letter inbetween quotes or the whole word: ")
print(letter_guess)

for letter in rand_word:
    if(letter_guess == rand_word):
        print(letter_guess + " is the correct word! Great job you win")
        break
    elif(letter_guess != letter):
        print(letter_guess + " is not a letter in the word")
        guesses_left = guesses_left - 1
        if(guesses_left == 0):
            print("You are out of guesses you lose!")
            break
        letter_guess = input("Try again! Guess a letter inbetween quotes or the whole word: ")
        print("You have " + str(guesses_left) + " guesses left")
    elif(letter_guess == letter):
        print("you guessed the letter " + letter_guess + " correct!")
        guesses_left = guesses_left - 1
        if(guesses_left == 0):
            print("You are out of guesses you lose!")
            break
        letter_guess = input("Good job! Guess a letter inbetween quotes or the whole word: ")
        print("You have " + str(guesses_left) + " guesses left")
