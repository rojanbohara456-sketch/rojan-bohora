import pygame
import random

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,80,80)
BLUE = (80,180,255)
YELLOW = (255,255,0)

font = pygame.font.SysFont("Arial",28)
big_font = pygame.font.SysFont("Arial",60)

# Player
player = pygame.Rect(WIDTH//2, HEIGHT-70, 50, 50)
player_speed = 6
health = 5

# Bullets
bullets = []
enemy_bullets = []

# Enemies
enemies = []
enemy_speed = 2

# Stars for background
stars = [[random.randint(0,WIDTH), random.randint(0,HEIGHT)] for i in range(80)]

score = 0

def spawn_enemy():
    x = random.randint(0, WIDTH-40)
    y = random.randint(-200,-40)
    enemies.append(pygame.Rect(x,y,40,40))

for i in range(6):
    spawn_enemy()

def draw_stars():
    for star in stars:
        pygame.draw.circle(screen,WHITE,star,2)
        star[1]+=1
        if star[1]>HEIGHT:
            star[1]=0

def draw_text(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))

def start_screen():

    waiting = True
    while waiting:

        screen.fill(BLACK)

        draw_text("SPACE SHOOTER",big_font,WHITE,WIDTH//2-200,200)
        draw_text("Press SPACE to Start",font,WHITE,WIDTH//2-120,300)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

start_screen()

running = True

while running:

    clock.tick(60)
    screen.fill(BLACK)

    draw_stars()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx, player.y,5,15))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x>0:
        player.x -= player_speed

    if keys[pygame.K_RIGHT] and player.x<WIDTH-50:
        player.x += player_speed

    pygame.draw.rect(screen,BLUE,player)

    for bullet in bullets:
        bullet.y -= 10
        pygame.draw.rect(screen,YELLOW,bullet)

    bullets = [b for b in bullets if b.y>0]

    for enemy in enemies:

        enemy.y += enemy_speed

        pygame.draw.rect(screen,RED,enemy)

        if random.randint(0,200)==1:
            enemy_bullets.append(pygame.Rect(enemy.centerx,enemy.bottom,5,15))

        if enemy.y>HEIGHT:
            enemy.y=random.randint(-200,-40)
            enemy.x=random.randint(0,WIDTH-40)
            health-=1

        for bullet in bullets:

            if enemy.colliderect(bullet):
                score+=1
                enemy.y=random.randint(-200,-40)
                enemy.x=random.randint(0,WIDTH-40)

                if bullet in bullets:
                    bullets.remove(bullet)

    for ebullet in enemy_bullets:

        ebullet.y += 6
        pygame.draw.rect(screen,WHITE,ebullet)

        if ebullet.colliderect(player):
            health -= 1
            enemy_bullets.remove(ebullet)

    enemy_bullets = [b for b in enemy_bullets if b.y<HEIGHT]

    draw_text("Score: "+str(score),font,WHITE,10,10)
    draw_text("Health: "+str(health),font,WHITE,10,40)

    if health <= 0:

        screen.fill(BLACK)
        draw_text("GAME OVER",big_font,RED,WIDTH//2-160,250)
        draw_text("Score: "+str(score),font,WHITE,WIDTH//2-60,330)
        draw_text("Close window to exit",font,WHITE,WIDTH//2-100,370)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    pygame.display.update()

pygame.quit()