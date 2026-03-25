#NUMBER GUESS GAME!!!
import random
jackpot=random.randint(1,100)
user=int(input("GUESS THE NUMBER PLEASE:-"))
attempt=1
while user!=jackpot:
    if(user>jackpot):
        print("GUESS LOWER NUMBER!!!")
    else:
        print("GUESS HIGHER NUMBER!!!")
    attempt+=1
    user=int(input("GUESS NUMBER AGAIN:-"))

print("CONGRATULATION YOU GUESS RIGHT!!!")
print("YOU TOOK",attempt,"attempts")