import random


with open('New Text Document.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words).strip()
allowed_errors = 7
guesses = []


guesses.append(word[0].lower())
guesses.append(word[3].lower())

done = False

while not done : 
    for letter in word :
        if letter.lower() in guesses:
            print(letter ,end=' ')
        else:
            print('_', end=' ')
    print(" ")

    guess = input(f'Allowed errors left: {allowed_errors}, next guess: ')
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -=1
        if allowed_errors == 0 :
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses :
            done = False

if done:
    print(f'You Found The Word ! It Was {word}')

else:
    print(f'Game Over ! The Word Was { word}')

