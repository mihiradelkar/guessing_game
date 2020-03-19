#The best solution for game and it's maximum and minimum attempts list.
import random
games=''
attemptslist=[]
while games=='':
    try:
#         games=int(input("how many games would you like to play?"))
        games=int(10)
    except:
        print("please select using a number")
for game in range (0,games):
#     low=int(input("enter a minimum value"))
#     high=int(input("enter a maximum value"))
    low=int(1)
    high=int(100)
    pick=random.randint(low,high)
    guess= None
    attempts=0
    while pick != guess:
        guess=int((low+high)/2)
#        print(guess)
    
        if guess != pick:
                attempts+=1
                if guess>pick:
#                    print("high")
                    high=guess
                else:
#                    print("low")
                    low=guess
        else:
            print("your number is correct, nice!!!, your attempts to guess answers were:",attempts)
            attemptslist.append(attempts)
            
attemptslist.sort()
print(attemptslist)
