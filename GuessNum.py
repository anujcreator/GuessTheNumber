import random
guesses = 0
random_num = random.randint(0, 100)

while guesses < 10:
    
    guessed_num = int(input("Enter Number: "))
    
    if guessed_num == random_num:
        print("YOU WON!!")
        break
    elif guessed_num < random_num:
        print("Guess is LOW")
    else:
        print("Guess is HIGH")
        
    guesses += 1
    