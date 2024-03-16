import simplegui

width=200
height=200
a=0
b=0
c=0
d=0 
e="00"
g=1
time=0
chance=0

def tick():
    global a,b,c,d,e
    a+=1
    b=a%10
    c=a%600/10
    d=a/600
    if c<10:
       e="0"+str(c)
    else:
       e=c
    
def draw(canvas):
    canvas.draw_text(str(d)+":"+str(e)+"."+str(b),[width*0.55/2,height*1.1/2],40,"White")
    canvas.draw_text(str(time)+"/"+str(chance),[width*3.5/5,height*1/5],24,"Green")
    
def start_button():
    global g
    g=0
    t.start()
    return

def stop_button():
    global chance,time,g
    t.stop()
    g+=1
    if g>0 and g<=1:
       chance+=1
       if (a%10)==0:
           time+=1
       else:
           return
    else:
       return

def reset_button():
    global a,b,c,d,e,chance,time,g
    chance=0
    time=0
    a=0
    b=0
    c=0
    d=0 
    e="00"
    g=1
    t.stop()
    return

f=simplegui.create_frame("clock game",width,height)
t=simplegui.create_timer(100,tick)

f.set_draw_handler(draw)
f.add_button("start",start_button,100)
f.add_button("stop",stop_button,100)
f.add_button("resset",reset_button,100)

f.start()



