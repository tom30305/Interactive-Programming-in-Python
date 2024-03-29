# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
play=False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 700 )
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image =image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.fire=False
        
    def get_pos(self):
        return self.pos   
    
    def get_radius(self):
        return self.radius
    
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image,[130,45],self.image_size,self.pos,self.image_size,self.angle)
        else:
            canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)
        
    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.angle+=self.angle_vel
        forward=angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0]+=forward[0]*0.1
            self.vel[1]+=forward[1]*0.1
        
        self.vel[0]*=(1-0.02)
        self.vel[1]*=(1-0.02)
   
        if self.pos[0]<0:
            self.pos[0]=WIDTH
        elif self.pos[0]>WIDTH:
            self.pos[0]=0
        if self.pos[1]<0:
            self.pos[1]=HEIGHT
        elif self.pos[1]>HEIGHT:
            self.pos[1]=0 
                    
    def shoot(self):
        forward=angle_to_vector(self.angle)
        missile_pos=[self.pos[0]+self.radius*forward[0],self.pos[1]+self.radius*forward[1]]
        missile_vel=[self.vel[0]+5*forward[0],self.vel[1]+5*forward[1]]
        missile_group.add(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        
    def get_pos(self):
        return self.pos

    def get_radius(self):
        return self.radius
    
    def draw(self, canvas):
        if self.animated:
            self.image_center = [self.image_center[0] + self.image_size[0] * self.age, self.image_center[1]]
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.angle+=self.angle_vel
        
        if self.lifespan and self.age < self.lifespan:
            self.age += 10
            return False
        else:
            return True
        
    def collide(self, other_object):
        if dist(self.pos, other_object.get_pos()) < self.radius + other_object.get_radius():
            return True
        else:
            return False

        
def keydown(key):
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
        ship_thrust_sound.play()
    elif key==simplegui.KEY_MAP["left"]:
         my_ship.angle_vel=-5*math.pi/180
    elif key==simplegui.KEY_MAP["right"]:
         my_ship.angle_vel=5*math.pi/180
    elif key==simplegui.KEY_MAP["space"]:
         my_ship.shoot()
         missile_sound.play()

def keyup(key):
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust = False
        ship_thrust_sound.rewind()
    elif key==simplegui.KEY_MAP["left"]:
         my_ship.angle_vel=0
    elif key==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel=0

           
def draw(canvas):
    global time,lives, score, rock_group, play
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    canvas.draw_text("Lives:"+str(lives),(30,50),30,"Red")
    canvas.draw_text("Score:"+str(score),(670,50),30,"Red")
    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(canvas, rock_group)
    process_sprite_group(canvas, missile_group)
    process_sprite_group(canvas, explosion_group)
    
    my_ship.update()
    
    if group_collide(rock_group, my_ship) > 0:
        lives -= 1
        explosion_sound.play()
    if group_group_collide(missile_group, rock_group):
        score+=10
        explosion_sound.play()
    
    if lives ==0:
        rock_group = set([])
        soundtrack.pause()
        timer.stop()
        play=False
        
    if  not play:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], splash_info.get_size())


# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, play
    if len(rock_group) <= 12 and play:
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        rock_vel = [(random.choice([1,0,-1])) * 0.5 ,(random.choice([1,0,-1])) * 0.5 ]
        rock_ang_vel = random.choice([1,0.5,0,-0.5,-1]) * 0.01  
        while dist(rock_pos, my_ship.pos) < 100:
            rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        rock_group.add(Sprite(rock_pos, rock_vel, 0, rock_ang_vel, asteroid_image, asteroid_info))
    
def click(pos):
    global play,score,lives
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    width_splash = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    height_splash = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not play) and width_splash and height_splash:
        play = True
        score = 0
        lives = 3
        timer.start()
        soundtrack.rewind()
        soundtrack.play()
    
def group_collide(group,other_object):
    num_collides=0
    for explosion in set(group):
        if explosion.collide(other_object):
            explosion_group.add(Sprite(explosion.get_pos(), (0, 0), 0, 0, explosion_image, explosion_info, explosion_sound))
            group.remove(explosion)
            num_collides+=1
    return num_collides


def process_sprite_group(canvas, group):
    for sprite in set(group):
        sprite.draw(canvas)
        if sprite.update():
            group.remove(sprite)

def group_group_collide(group, second_group):
    total = 0
    for collide in set(group):
        count = group_collide(second_group, collide)
        if count > 0:
            group.remove(collide)
        total += count
    return total

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

