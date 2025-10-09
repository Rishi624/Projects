import random
print("Welcome to the snake water gun game")
print("Gun beats snake, snake beats water and water beats gun")
print("There will be 10 rounds and enter word of your choice")
# snake = 0
# gun = 1
# water = 2
comppo = 0
userpo = 0
for i in range(1,11):
    print(f"Round{i}")
    comp = random.randint(0,2)
    user = input("")
    if user.lower() == "snake":
        u=0
    elif user.lower() == "gun":
        u=1
    elif user.lower() == "water":
        u=2
        
    if comp == 0 and u == 0:
        comppo += 0.5
        userpo += 0.5
        print("Round was draw")
    elif comp == 0 and u == 1:
        userpo += 1
        print("You won the round")
    elif comp == 0 and u == 2:
        comppo += 1
        print("Computer won the round")

    elif comp == 1 and u == 0:
        comppo += 1
        print("Computer won the round")
    elif comp == 1 and u == 1:
        userpo += 0.5
        comppo += 0.5
        print("Round was draw")
    elif comp == 1 and u == 2:
        userpo += 1
        print("You won the round")

    
    elif comp == 2 and u == 0:
        userpo += 1
        print("You won the round")
    elif comp == 2 and u == 1:
        comppo += 1
        print("Computer won the round")
    elif comp == 2 and u == 2:
        comppo += 0.5
        userpo += 0.5
        print("Round was draw")

if comppo > userpo:
    print("Computer won the game")
elif comppo < userpo:
    print("You won the game")
else:
    print("Game was draw")