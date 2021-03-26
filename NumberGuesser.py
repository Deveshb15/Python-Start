import random 

name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the game!")
randNum = random.randint(0,100)
chances = 10

play = "Yes"

def playAgain():
    global play, chances
    play = input("Do you want to play again? (Yes/No): ")
    if play == "Yes":
        randNum = random.randint(0,100)
        chances = 10

while play == "Yes":

    while chances > 0:
        guess = input("Guess a number between 1 to 100: ")

        if int(guess) == randNum:
            print("You Won!")
            print(f"Your score is {chances * 10}")
            playAgain()
            break
        elif int(guess) > randNum:
            print(f"{guess} is higher than the number to be guessed.")
            chances -= 1;
            print(f"You have {chances} left")
        elif int(guess) < randNum:
            print(f"{guess} is smaller than number to be guessed.")
            chances -= 1
            print(f"You have {chances} left")

        if chances == 0:
            print("You Lose!")
            playAgain()
            break

print("Thank you for playing")
        
    
