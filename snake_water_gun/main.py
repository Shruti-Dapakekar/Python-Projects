import random
'''
Basic logic of code
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice (s/g/w): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    raise ValueError("Invalid choice. Enter s for snake, w for water, or g for gun.")

you = youDict[youstr]

print(f"You choose :{reverseDict[you]} \nComputer choose :{reverseDict[computer]}")

if (computer == you):
    print("Its a Draw !!")
else:
    if (computer == -1 and you == 1):
        print("You Win!!")
    elif (computer == -1 and you == 0):
        print("You Lose!!")
    elif (computer == 1 and you == -1):
        print("You Win!!")
    elif (computer == 1 and you == 0):
        print("You Win!!")
    elif (computer == 0 and you == -1):
        print("You Lose!!")
    elif (computer == 0 and you == 1):
        print("You Lose!!")
    else:
        print("Something went wrong")

# The whole else part can also be writen as 
# if (computer == you):
#     print("Its a Draw !!")
# else:
#     if computer - you == -1 and computer - you == 2:
#         print("You Win")
#     else:
#         print("You Lose")