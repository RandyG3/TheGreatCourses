import random

"""
numtoguess = random.randint(1, 100)
print(numtoguess)

num_tries = 1

guess = int(input('Enter your guess: '))

while guess != numtoguess:
    num_tries += 1
    if guess > numtoguess:
        print('Too high')
    else:
        print('too low')
    guess = int(input('Enter your guess: '))

print('It took you', num_tries, 'guess to pick', numtoguess)

print(' ' + '\n' + 'His code' + '\n')

passes = 0
"""
passes = 0

while True:
    if passes == 1:
        break
    secretnum = random.randint(1, 100)
    print(secretnum)
    numguesses = 0
    guessed = False
    while not guessed:
        guess = int(input("Enter a guess from 1 to 100: "))
        numguesses += 1
        if guess == secretnum:
            print("You guessed it! It took you", numguesses, "tries!")
            guessed = True
            passes += 1
        elif guess < secretnum:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


print('RC=0')