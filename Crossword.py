import random

name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the game!")
words = ["apple", "mango", "banana", "chikoo", "watermelon", "litchi", "plum", "grapes", "guava", "pomegranate", "jackfruit"]
index = random.randint(0, len(words))
word = words[index]
indexes = random.sample(range(0, len(word)), 3)
guesses = ""
chances = 10

for i in indexes:
    guesses += word[i]

play = "Yes"

def playAgain():
    global play
    play = input("Do you want to play again? (Yes/No): ")
    if play == "Yes":
        global chances, word, guesses
        index = random.randint(0, len(words))
        word = words[index]
        indexes = random.sample(range(0, len(word)), 3)
        guesses = ""
        chances = 10
        for i in indexes:
            guesses += word[i]

while play == "Yes":
    
    while chances > 0:

        won = True
        for ch in word:
            if ch in guesses:
                print(ch, end=" ")
            else:
                print("_", end=" ")
                won = False

        if won:
            print("\nYou Won!")
            print(f"Your Score is {chances * 10}")
            playAgain()
            break

        guess = input("\nGuess a character: ")
        guesses += guess

        if guess not in word:
            chances -= 1
            print("\nWrong Answer!")
            print(f"You have {chances} left.")

            if chances == 0:
                print("You Lose")
                playAgain()
                break
                
print("Thanks for playing")
