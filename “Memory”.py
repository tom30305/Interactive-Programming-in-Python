import simplegui
import random

width=800
height=100
card_num=range(16)

def new_game():
    global card_index,state,click_num,turn_count,card3,place_1,i,j
    state = 0
    card_index=2*(range(8))
    random.shuffle(card_index) 
    click_num=[0,0]
    turn_count=0
    card3=[]
    place_1=[]

def click(pos):
    global click_num,state,turn_count
    if state==0:
        click_num[0]=((pos[0])//50+1)
        state=1
    elif state==1:
        if ((pos[0])//50+1==click_num[0])or((pos[0])//50+1==click_num[1]):
            state=1
        else:
            click_num[1]=(pos[0])//50+1
            state=2
    else: 
        if ((pos[0])//50+1==click_num[1])or((pos[0])//50+1==click_num[0]):
            state=2
        else:
            click_num[1]=0
            click_num[0]=(pos[0])//50+1
            state=1
            turn_count+=1
        
def draw(canvas):
    for line in card_num:
        global card1,card2
        canvas.draw_line((line*50+25, 5), (line*50+25, 95), 45, 'White')
    card1=card_index[click_num[0]-1]
    card2=card_index[click_num[1]-1]
 
    canvas.draw_line(((click_num[0]-1)*50+25, 5), ((click_num[0]-1)*50+25, 95), 45, 'Yellow')
    canvas.draw_text(str(card1),[((click_num[0]-1)*50+11),(height*1.35/2)], 60, 'Red') 
    canvas.draw_line(((click_num[1]-1)*50+25, 5), ((click_num[1]-1)*50+25, 95), 45, 'Yellow')
    canvas.draw_text(str(card2),[((click_num[1]-1)*50+11),(height*1.35/2)], 60, 'Red')
    label.set_text("Turns = "+str(turn_count))      
       
    if card1==card2:
        global card3,place_1
        card3.append(card2)
        card3.append(card1)            
        place_1.append(click_num[0]-1)
        place_1.append(click_num[1]-1)
    for place in range(len(place_1)):
            canvas.draw_line(((place_1[place])*50+25, 5), ((place_1[place])*50+25, 95), 45, 'Yellow')
            canvas.draw_text(str(card3[place]),[((place_1[place])*50+11),(height*1.35/2)], 60, 'Red')           

                
f= simplegui.create_frame("memory game", width, height)
f.add_button("reset",new_game)
f.set_mouseclick_handler(click)
label = f.add_label("Turns = 0")
f.set_draw_handler(draw)

new_game()
f.start()


