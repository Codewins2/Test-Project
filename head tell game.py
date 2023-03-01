
from twister import com
from project import play





import random



decider = input("Enter 'head' or 'tail'").lower()
user_choice = int(input("Enter the number you will throw"))
opponent_choice = random.randint(1,6) 


result = user_choice + opponent_choice


if decider == "head":
    print("total number: ",result)
    if result % 2 == 1:
        print("Player wins the toss and chooses to bat")
        play()

        
    else:
        print("Computer wins the toss and chooses to bat")
        com()        


elif decider == "tail":
    print("total number: ",result)
    if result % 2 == 0:
        print("The player wins the toss and chooses to bat")
        play()    
        
            
    else:
        print("The computer wins the toss")
        com()



else:
    print("/n Python greets you with an beautiful error message!!!")



# You will need  project and twister to run this head tell game.


























