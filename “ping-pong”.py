import simplegui
import random

a=0
b=0
ball_r=30
width=800
height=600
pad_width=30
pad_height=50
pad_center1=300
pad_center2=300
pad_vel1=0
pad_vel2=0
ball_pos=[width/2,height/2]
v1=random.choice([1, 2, -1, -2])
v2=random.choice([1, 2, -1, -2])
vel=[v1,v2]

def draw(canvas):
    global pad_center1,pad_center2,pad_vel1,pad_vel2,a,b,ball_pos,v1,v2,vel
    pad_center1+=pad_vel1
    pad_center2+=pad_vel2
    
    canvas.draw_circle(ball_pos,ball_r,5,"Orange","White")
    canvas.draw_line([50,0],[50,600],5,"White")
    canvas.draw_line([750,0],[750,600],5,"White")
    canvas.draw_line([width/2,0],[width/2,height],5,"White")
    canvas.draw_text(str(a), (200, 100), 50, 'White')
    canvas.draw_text(str(b), (600,100), 50, 'White')
    canvas.draw_line([40,pad_center1-pad_height],[40,pad_center1+pad_height],20,"White")
    canvas.draw_line([760,pad_center2-pad_height],[760,pad_center2+pad_height],20,"White")
    
    ball_pos[0]+=vel[0]
    ball_pos[1]+=vel[1]
    
    if ball_pos[0]<(ball_r+50) and  ball_pos[1]<pad_center1+pad_height and ball_pos[1]>pad_center1-pad_height:
       vel[0]=-vel[0]
    elif ball_pos[0]>(750-ball_r) and  ball_pos[1]<pad_center2+pad_height and ball_pos[1]>pad_center2-pad_height:
       vel[0]=-vel[0]
    elif ball_pos[1]<(ball_r):
       vel[1]=-vel[1]
    elif ball_pos[1]>(600-ball_r):
       vel[1]=-vel[1]
    elif ball_pos[0]<(ball_r+50) and ( ball_pos[1]>pad_center1+pad_height or ball_pos[1]<pad_center1-pad_height):
        ball_pos=[width/2,height/2] 
        v1=random.choice([1, 2])
        v2=random.choice([1, 2, -1, -2])
        vel=[v1,v2]
        b+=1
    elif ball_pos[0]>(750-ball_r) and ( ball_pos[1]>pad_center2+pad_height or ball_pos[1]<pad_center2-pad_height):   
         ball_pos=[width/2,height/2]
         v1=random.choice([-1, -2])
         v2=random.choice([1, 2, -1, -2])
         vel=[v1,v2]
         a+=1
            
    if (pad_center1-pad_height)==0:
        pad_vel1=0
    elif (pad_center1+pad_height)==600:
        pad_vel1=0
    elif (pad_center2-pad_height)==0:
        pad_vel2=0
    elif (pad_center2+pad_height)==600:
        pad_vel2=0    

def keydown(key):
    global pad_vel1,pad_vel2
    a=5
    if key==simplegui.KEY_MAP["w"]and not((pad_center1-pad_height)==0):
        pad_vel1-=a
    elif key==simplegui.KEY_MAP["s"]and not((pad_center1+pad_height)==600):
        pad_vel1+=a
    elif key==simplegui.KEY_MAP["up"]and not((pad_center2-pad_height)==0):
        pad_vel2-=a
    elif key==simplegui.KEY_MAP["down"]and not((pad_center2+pad_height)==600):
        pad_vel2+=a
        
def keyup(key):
    global pad_vel1,pad_vel2
    a=5
    if key==simplegui.KEY_MAP["w"] and not((pad_center1-pad_height)==0):
        pad_vel1+=a  
    elif key==simplegui.KEY_MAP["s"]and not(pad_center1+pad_height)==600:
        pad_vel1-=a
    elif key==simplegui.KEY_MAP["up"]and not((pad_center2-pad_height)==0):
        pad_vel2+=a
    elif key==simplegui.KEY_MAP["down"]and not(pad_center2+pad_height)==600:
        pad_vel2-=a
    return

def restart():
    global a,b,ball_pos,vel,v1,v2
    ball_pos=[width/2,height/2]
    v1=random.choice([1, 2, 3, -1, -2, -3])
    v2=random.choice([1, 2, 3, -1, -2, -3])
    vel=[v1,v2]
    
def abcc():
    global a,b
    a=0
    b=0
    restart()
    
f=simplegui.create_frame("pong",width,height)
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.add_button("Restart",abcc,200)

f.start()


