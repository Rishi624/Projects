import random

print("<---Welcome to the game--->")
print("Rules are simple")
print("System will generate a random number you should guess it in 10 chances")

num = random.randint(1,1000)
for i in range(1,11):
    print(f"Chance number:{i}")
    unum = int(input("Enter number"))
    if unum<num:
        print("Greater")

    elif unum>num:
        print("Lesser")
    
    else:
        print("You won")
        a = 1
        break
else:
    print("You lost")
