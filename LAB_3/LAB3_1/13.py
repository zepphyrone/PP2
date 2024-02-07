from random import randint
def guessNumber():
    print("Hello! What is your name?")
    name=str(input())
    print(f"{name} Well, {name}, I am thinking of a number between 1 and 20. Take a guess.")
    number=randint(1,20)
    n=0
    while True:
        x=int(input())
        n+=1
        if(x<number):
            print("Your guess is too low. Take a guess")
        elif(x>number):
            print("Your guess is too high. Take a guess")
        else:
            print(f"{number} Good job, {name}! You guessed my number in {n} guesses!")
            break
guessNumber()