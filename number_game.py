import random

def game_level(level):
    global target
    if level == 0:
        print("level 0 : range 1- 100")
        target = random.randint(1,100)

    elif level == 1:
        print("level 1 : range 1- 200")
        target = random.randint(1,200)

    else:
        print("level 2 : range 1- 500")
        target = random.randint(1,500)

    return target

def guess_number(user_choice):

    if(user_choice == "Q" or user_choice == 'q'):
        return "game over"
    
    user_choice = int(user_choice)
    
    if (user_choice == target):
            print("Success : Correct Guess !!")
            return  "You won the game"

    elif (user_choice < target):
            user_choice = input("Your number was too small. Take a bigger guess.")
            guess_number(user_choice)

    else:
            user_choice = input("Your number was too big. Take a smaller guess.")
            guess_number(user_choice)


    return  "You won the game"


level = int(input("choose the difficulty level (level 0, level 1, level 2): "))
game_level(level)
user_choice = input("Guess the target number or Quit(Q) : ")
res = guess_number(user_choice)
print(res)
