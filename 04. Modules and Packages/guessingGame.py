# number guessing game
import random

def game():
    num=random.randint(0, 10)
    lives=3
    while lives>0:
        guess=int(input("\nguess the number: "))
        if num==guess:
            print("Congratulations! You won 👏")
            break
        else:
            lives-=1
            if lives==0:
                print(f"Sorry! you lose. Correct number was {num}")
            else:
                print(f'Sorry! you guessed wrong number')
                print(f'You have {lives} more lives remaining')

if __name__=='__main__':
    cont="y"
    while cont=="y":
        game()
        cont=input("\npress y to continue playing and n to end game")