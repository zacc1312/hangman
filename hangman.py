#import the libraries
from english_words import english_words_set
import random

#convert the set to a list
allwords=list(english_words_set)

#creates an empty dict to store the letters from the word
lettersdict = {}

correctlettersguessed = []

checkifletterwascorrect = None

win=False

lettersguessed = []

lives=6

#starting game sequence
repeat=True
print("welcome to hangman by zack")

hangmen= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

hangmen.reverse()

while repeat:

    lettersdict = {}

    correctlettersguessed = []

    checkifletterwascorrect = None

    win=False

    lettersguessed = []

    lives=6

    word=random.choice(allwords)

    word=word.lower()

    for i in range(0,len(word)):
        lettersdict.update({word[i]: i})

    while not win and lives > 0:

        letterguessed = "aa"

        print("\n\n")
        for char in word:
            if char in correctlettersguessed:
                print(char,end=" ")
            else:
                print("_",end=" ")

        while not len(letterguessed) == 1:
            print("\n\nenter a letter")
            letterguessed = str(input())
                
            if len(letterguessed) != 1:
                print("must be one character long")

            if letterguessed in word:
                del lettersdict[letterguessed]

                correctlettersguessed.append(letterguessed)

                print(hangmen[lives])

                if lettersdict == {}:
                    win=True

            else:
                lives-=1

                print(hangmen[lives])

    if lives==0:
        print(f"you lose! womp womp. the word was: {word}")

        repeatprompt = str(input("play again? enter 'yes' or 'no'"))

        if repeatprompt == "yes":
            repeat =  True

    if win:
        print(f"you win! the word was: {word}")

        repeatprompt = str(input("play again? enter 'yes' or 'no'"))

        if repeatprompt == "yes":
            repeat =  True

        else:
        	repeat = False

exit()
