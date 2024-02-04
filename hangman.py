import nltk
import random

nltk.download('words')

english_words = set(nltk.corpus.words.words())

lives = 11
word = random.choice(list(english_words))
guesslist = []
guessjoin = ''

for _ in range(len(word)):
    guesslist.append("_")

running = True

while running:
    guesscounter = 0
    guessjoin = ''
    for i in guesslist:
        print(i, end="")
    print('')
    guess = str(input("Enter your guess: ")).lower()

    for i in range(len(word)):
        if guess[0] == word[i]:
            guesslist[i] = guess[0]
        else:
            guesscounter += 1

    if guesscounter == len(word):
        lives -= 1
        print(f"Sorry! {guess.upper()} is not there in the word!")
    else:
        print("Correct!")
    
    if lives == 0:
        print(f"You lost the game! The word was {word}")
        running = False
        break
    
    for i in guesslist:
        guessjoin += i

    if guessjoin == word:
        input("You won the game!")
        running = False
        break