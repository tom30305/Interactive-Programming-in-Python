import simplegui
import random

num=7

def new_game():
    global count
    count=num
    print ""

def range100():
    global count,num
    num=7
    count=num
    print " "
    print "new game. range from 0 to 100"
    print "number of remaining guesses is",count
    global compu_number
    compu_number=random.randrange(0,100) 
    new_game()
    
def range1000():
    global count,num
    num=10
    count=num
    print " "
    print "new game. range from 0 to 1000"
    print "number of remaining guesses is",count
    global compu_number
    compu_number=random.randrange(0,1000)
    new_game()
    
def input_guess(guess_number):
    global count
    play_number=int(guess_number)
    print "guess was",play_number
    count -= 1
    if count==0 and play_number!=compu_number:
        print "game over,number is",compu_number
        print " "
        count=7
        range100()
    elif count==0 and play_number==compu_number:
        print "game over,you are corret~"
        print " "
        count=7
        range100()
    elif play_number==compu_number:
         print "correct"
         print " "
         count=7
         range100()
    else:
        print "number of remaining guesses is",count
        if  play_number==compu_number:
            print "correct"
            print " "
        elif play_number>compu_number:
             print "lower"
             print " "
        else:
             print "higher"
             print " "
        
        
new_game()
range100()


f=simplegui.create_frame("guess number",200,200)
f.add_button("range[0~100)",range100)
f.add_button("range[0~1000)",range1000)
f.add_input("guess number",input_guess,200)

f.start