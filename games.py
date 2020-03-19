#game for guessing the number.
import random
games=''
while games=='':
    try:
        games=int(input("how many games would you like to play the game ?"))
    except:
        print("please select using a number")
for game in range (0,games):
    pick=random.randint(1,25)
    guess= None
    attempts=0
    
    while pick != guess:
        try:
            guess=int(input("enter your guess number (between 1-25)"))
        except:
            print("please enter numbers only")
            continue
            
        if guess != pick:
            attempts+=1
            if guess>pick:
                print("high")
            else:
                print("low")
        else:
            print("your number is correct, nice!!!, your attempts to guess answers were:",attempts)
            if attempts>7:
                print ("loser!!!, you took too many attempts")
            else:
                print("winner!!!, nice you completed in 6 attempts")
