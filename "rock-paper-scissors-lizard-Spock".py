import random

def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    return number

def number_to_name(number):
    if number == 0:
        name=  "rock"
    elif number == 1:
        name= "Spock"
    elif number == 2:
        name= "paper"
    elif number == 3:
        name= "lizard"
    elif number == 4:
        name= "scissors" 
    return name 

def rpsls(name): 
    print ""
    computer_number = random.randrange(0, 5)
    player_number = name_to_number(name)
   
    print "Player chooses",name
    print "Computer chooses",number_to_name(computer_number)
   
    difference=((player_number - computer_number) % 5)
    if difference == 1 or difference == 2:
        print "Player wins!"
    elif difference == 3 or difference == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    return 
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
