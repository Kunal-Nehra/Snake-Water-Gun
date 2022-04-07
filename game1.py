import random

def game(player, comp):
    if(player==comp):
        return None
    
    elif(player=='s'):
        if(comp=='g'):
            return False
        elif(comp=='w'):
            return True
        
    elif(player=='w'):
        if(comp=='g'):
            return True
        elif(comp=='s'):
            return False
        
    elif(player=='g'):
        if(comp=='w'):
            return False
        elif(comp=='s'):
            return True
    
    
playerScore=0
compScore=0

for i in range(1,11):
    
    player=input("YOUR TURN :: SNAKE(s) , WATER(w) or GUN(g) :: ")
    print("Computer's turn :: ", end="")
    
    rand_no= random.randint(1, 3)
    if (rand_no==1):
        comp="s"
    elif(rand_no==2):
        comp="w"
    elif(rand_no==3):
        comp="g"
    print(f"comp choose {comp}")   
    a=game(player, comp)
        
    if a:
        playerScore=playerScore+1
        compScore=compScore
    elif a==None:
        playerScore=playerScore+1
        compScore=compScore+1
    else :
        compScore=compScore+1
        playerScore=playerScore
        
    print("Your Score is :: ",playerScore)
    print("Computer's Score is :: ",compScore)
    
    if(compScore==5 and playerScore<5):
        print("GAME OVER:: YOU LOOSE!!  :( ")
        break
    elif(playerScore==5 and compScore<5):
        print("GAME OVER :: YOU WON!! :) ")
        break
    elif(playerScore==5 and compScore==5):
        print("GAME OVER :: Tie!!  :|")
        break

