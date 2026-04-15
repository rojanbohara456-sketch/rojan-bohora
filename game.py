import pygame
import random
import math
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1100, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("INSANE Python Shooter")

clock = pygame.time.Clock()

WHITE=(255,255,255)
RED=(200,50,50)
GREEN=(50,200,50)
BLUE=(50,120,255)
YELLOW=(255,255,0)
BLACK=(20,20,20)
ORANGE=(255,150,0)

font = pygame.font.SysFont("Arial",22)
bigfont = pygame.font.SysFont("Arial",60)

# sounds
shoot_sound=None
explosion_sound=None

if os.path.exists("gun.wav"):
    shoot_sound=pygame.mixer.Sound("gun.wav")

if os.path.exists("explosion.wav"):
    explosion_sound=pygame.mixer.Sound("explosion.wav")

# load animations
player_frames=[]
for name in ["player1.png","player2.png"]:
    if os.path.exists(name):
        player_frames.append(pygame.image.load(name).convert_alpha())

frame_index=0
frame_timer=0

player=[500,350]
player_health=100
player_speed=4
sprint_speed=7
ammo=40
grenades=3

bullets=[]
grenade_list=[]
explosions=[]
enemies=[]
pickups=[]

score=0
wave=1
boss_active=False

# MAP (tile grid)
TILE=50
map_data=[
"######################",
"#.................A..#",
"#..........###.......#",
"#.................A..#",
"#...####.............#",
"#....................#",
"#.........A..........#",
"#....................#",
"#....#####...........#",
"#....................#",
"#.................A..#",
"######################"
]

walls=[]

for y,row in enumerate(map_data):
    for x,char in enumerate(row):

        if char=="#":
            walls.append(pygame.Rect(x*TILE,y*TILE,TILE,TILE))

        if char=="A":
            pickups.append([x*TILE+20,y*TILE+20,"ammo"])

# save/load highscore
def load_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt") as f:
            return int(f.read())
    return 0

def save_highscore(val):
    with open("highscore.txt","w") as f:
        f.write(str(val))

highscore=load_highscore()

class Enemy:

    def __init__(self):
        self.x=random.randint(100,1000)
        self.y=random.randint(100,600)
        self.health=3
        self.shoot_timer=random.randint(60,120)

    def move(self):

        dx=player[0]-self.x
        dy=player[1]-self.y
        dist=math.hypot(dx,dy)

        if dist<400:
            self.x+=dx/dist*1.5
            self.y+=dy/dist*1.5

    def shoot(self):

        dx=player[0]-self.x
        dy=player[1]-self.y
        dist=math.hypot(dx,dy)

        bullets.append([self.x,self.y,dx/dist,dy/dist,"enemy"])

    def update(self):

        self.move()

        self.shoot_timer-=1

        if self.shoot_timer<=0:
            self.shoot()
            self.shoot_timer=random.randint(100,160)

    def draw(self):
        pygame.draw.circle(screen,RED,(int(self.x),int(self.y)),15)

class Boss:
    def __init__(self):
        self.x=550
        self.y=120
        self.health=100

    def update(self):

        dx=player[0]-self.x
        dy=player[1]-self.y
        dist=math.hypot(dx,dy)

        self.x+=dx/dist*1.2
        self.y+=dy/dist*1.2

        if random.randint(0,40)==1:

            for a in range(-2,3):
                angle=math.atan2(dy,dx)+a*0.2
                bullets.append([self.x,self.y,math.cos(angle),math.sin(angle),"enemy"])

    def draw(self):

        pygame.draw.circle(screen,(180,0,180),(int(self.x),int(self.y)),40)

boss=None

def spawn_wave():

    global boss_active,boss

    if wave%5==0:
        boss_active=True
        boss=Boss()
    else:
        for i in range(wave*3):
            enemies.append(Enemy())

def shoot(mouse):

    global ammo

    if ammo<=0:
        return

    dx=mouse[0]-player[0]
    dy=mouse[1]-player[1]

    dist=math.hypot(dx,dy)

    bullets.append([player[0],player[1],dx/dist,dy/dist,"player"])

    ammo-=1

    if shoot_sound:
        shoot_sound.play()

def throw_grenade(mouse):

    global grenades

    if grenades<=0:
        return

    dx=mouse[0]-player[0]
    dy=mouse[1]-player[1]

    dist=math.hypot(dx,dy)

    grenade_list.append([player[0],player[1],dx/dist,dy/dist,120])

    grenades-=1

def explosion(x,y):

    explosions.append([x,y,10])

    if explosion_sound:
        explosion_sound.play()

running=True
spawn_wave()

while running:

    clock.tick(60)
    screen.fill(BLACK)

    mouse=pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            shoot(mouse)

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_g:
                throw_grenade(mouse)

    keys=pygame.key.get_pressed()

    speed=player_speed

    if keys[pygame.K_LSHIFT]:
        speed=sprint_speed

    if keys[pygame.K_w]:
        player[1]-=speed
    if keys[pygame.K_s]:
        player[1]+=speed
    if keys[pygame.K_a]:
        player[0]-=speed
    if keys[pygame.K_d]:
        player[0]+=speed

    # player animation
    if len(player_frames)>0:

        frame_timer+=1

        if frame_timer>10:
            frame_timer=0
            frame_index=(frame_index+1)%len(player_frames)

        screen.blit(player_frames[frame_index],(player[0]-20,player[1]-20))
    else:
        pygame.draw.circle(screen,GREEN,(int(player[0]),int(player[1])),15)

    # bullets
    for b in bullets[:]:

        b[0]+=b[2]*10
        b[1]+=b[3]*10

        color=YELLOW if b[4]=="player" else ORANGE
        pygame.draw.circle(screen,color,(int(b[0]),int(b[1])),4)

        if b[4]=="enemy":
            if math.hypot(player[0]-b[0],player[1]-b[1])<15:
                player_health-=5
                bullets.remove(b)

        for e in enemies[:]:

            if b[4]=="player":
                if math.hypot(e.x-b[0],e.y-b[1])<15:
                    e.health-=1
                    bullets.remove(b)

                    if e.health<=0:
                        enemies.remove(e)
                        explosion(e.x,e.y)

                        score+=1

        if boss_active and b[4]=="player":
            if math.hypot(boss.x-b[0],boss.y-b[1])<40:
                boss.health-=1
                bullets.remove(b)

    # grenades
    for g in grenade_list[:]:

        g[0]+=g[2]*6
        g[1]+=g[3]*6
        g[4]-=1

        pygame.draw.circle(screen,BLUE,(int(g[0]),int(g[1])),6)

        if g[4]<=0:
            explosion(g[0],g[1])

            for e in enemies[:]:
                if math.hypot(e.x-g[0],e.y-g[1])<100:
                    enemies.remove(e)
                    score+=1

            grenade_list.remove(g)

    # enemies
    for e in enemies:
        e.update()
        e.draw()

    # boss  
    if boss_active:

        boss.update()
        boss.draw()

        if boss.health<=0:
            boss_active=False
            explosion(boss.x,boss.y)
            score+=20
            wave+=1
            spawn_wave()

    # explosions
    for ex in explosions[:]:

        pygame.draw.circle(screen,ORANGE,(int(ex[0]),int(ex[1])),ex[2])
        ex[2]+=3

        if ex[2]>60:
            explosions.remove(ex)

    # pickups
    for p in pickups[:]:

        pygame.draw.rect(screen,YELLOW,(p[0],p[1],15,15))

        if math.hypot(player[0]-p[0],player[1]-p[1])<20:
            ammo+=20
            pickups.remove(p)

    # map walls
    for w in walls:
        pygame.draw.rect(screen,(90,90,90),w)

    # next wave
    if len(enemies)==0 and not boss_active:
        wave+=1
        spawn_wave()

    # UI
    screen.blit(font.render(f"Health: {player_health}",True,WHITE),(10,10))
    screen.blit(font.render(f"Ammo: {ammo}",True,WHITE),(10,40))
    screen.blit(font.render(f"Grenades: {grenades}",True,WHITE),(10,70))
    screen.blit(font.render(f"Score: {score}",True,WHITE),(10,100))
    screen.blit(font.render(f"HighScore: {highscore}",True,WHITE),(10,130))

    if player_health<=0:

        if score>highscore:
            save_highscore(score)

        text=bigfont.render("GAME OVER",True,RED)
        screen.blit(text,(400,300))

    pygame.display.update()

pygame.quit()