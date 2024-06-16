import time
import pygame
import random

WIDTH = 900
HEIGHT = 600
FPS = 40

pygame.init()

pygame.mixer.music.load("sounds/pisk.mp3")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

font = pygame.font.Font(None, 36)
bg = pygame.image.load("images/bg_1.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
mouse_u = pygame.image.load("images/mouse_u.png").convert_alpha()
mouse_l = pygame.image.load("images/mouse_u.png").convert_alpha()
mouse_r = pygame.image.load("images/mouse_u.png").convert_alpha()
mouse_d = pygame.image.load("images/mouse_u.png").convert_alpha()

bullet_l = pygame.image.load("images/bullet_l.png").convert_alpha()
bullet_r = pygame.image.load("images/bullet_r.png").convert_alpha()
bullet_d = pygame.image.load("images/bullet_d.png").convert_alpha()
bullet_u = pygame.image.load("images/bullet_u.png").convert_alpha()

up = [pygame.image.load("images/up1.png").convert_alpha()]
down = [pygame.image.load("images/down1.png").convert_alpha()]
left = [pygame.image.load("images/left1.png").convert_alpha()]
right = [pygame.image.load("images/right1.png").convert_alpha()]

clock = pygame.time.Clock()
view = left[0]
view_end = left[0]
count = 0
score = 0
time_counter = 0
fps_counter = 0
povorot = 0
player_pos_x = WIDTH/2-50
player_pos_y = HEIGHT/2-50
player_speed = 10
bullet_speed = 30

randomer = 0

mice_u = []
mice_l = []
mice_r = []
mice_d = []

bullets_u = []
bullets_l = []
bullets_r = []
bullets_d = []

mouse_timer = pygame.USEREVENT + 1
pygame.time.set_timer(mouse_timer, 1000)

flag_end_in_start = False

flag_end = True
running = True

try:
    f = open("score.txt")
except IOError:
    f = open('score.txt', 'w')
    for i in range(0, 10):
        f.write(str(i + 1) + ". 0\n")
    f.close()

f = open("score.txt","r")
score_list = f.readlines()
f.close()

def pause():
    flag_start = False
    while not flag_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_start = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flag_start = True

def some(e,bullets,mice_r,mice_l,mice_d,mice_u):
    for m in mice_r:
        if e.colliderect(m):
            mice_r.remove(m)
            bullets.remove(e)
            return 1
    for m in mice_l:
        if e.colliderect(m):
            mice_l.remove(m)
            bullets.remove(e)
            return 1
    for m in mice_u:
        if e.colliderect(m):
            mice_u.remove(m)
            bullets.remove(e)
            return 1
    for m in mice_d:
        if e.colliderect(m):
            mice_d.remove(m)
            bullets.remove(e)
            return 1
    return 0

while running:
    clock.tick(FPS)
    #screen.fill((100, 0, 0))
    screen.blit(bg,(0,0))

    fps_counter += 1
    if fps_counter == FPS:
        time_counter += 1
        fps_counter = 0

    if time_counter > 59:
        end = font.render("Игра завершена!", True, (255, 255, 255))
        screen.blit(end, (WIDTH / 2 - 100, HEIGHT / 2 - 100))
        running = False

    hold = pygame.key.get_pressed()
    if hold[pygame.K_d] or hold[pygame.K_a] or hold[pygame.K_w] or hold[pygame.K_s]:
        if hold[pygame.K_d]:
            povorot = 1
            count += 1
            count = count % len(right)
            view = right[count]
            view_end = right[0]
            screen.blit(view, (player_pos_x,player_pos_y))
            player_pos_x = player_pos_x + player_speed
            if player_pos_x > (WIDTH - 80):
                player_pos_x = WIDTH - 80
        elif hold[pygame.K_a]:
            povorot = 0
            count += 1
            count = count % len(left)
            view = left[count]
            view_end = left[0]
            screen.blit(view, (player_pos_x, player_pos_y))
            player_pos_x = player_pos_x - player_speed
            if player_pos_x < 0:
                player_pos_x = 0
        elif hold[pygame.K_w]:
            povorot = 2
            count += 1
            count = count % len(up)
            view = up[count]
            view_end = up[0]
            screen.blit(view, (player_pos_x, player_pos_y))
            player_pos_y = player_pos_y - player_speed
            if player_pos_y < 0:
                player_pos_y = 0
        elif hold[pygame.K_s]:
            povorot = 3
            count += 1
            count = count % len(down)
            view = down[count]
            view_end = down[0]
            screen.blit(view, (player_pos_x, player_pos_y))
            player_pos_y = player_pos_y + player_speed
            if player_pos_y > HEIGHT-80:
                player_pos_y = HEIGHT-80
    else:
        count = 0
        screen.blit(view_end, (player_pos_x, player_pos_y))

    player_rect = view.get_rect(topleft=(player_pos_x, player_pos_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == mouse_timer:
            randomer = random.randint(0,3)
            if randomer == 0:
                mice_l.append(mouse_l.get_rect(topleft=(-50,random.randint(0, HEIGHT - 100))))
            elif randomer == 1:
                mice_r.append(mouse_r.get_rect(topleft=(WIDTH,random.randint(0, HEIGHT - 100))))
            elif randomer == 2:
                mice_u.append(mouse_u.get_rect(topleft=(random.randint(0, WIDTH - 100),-50)))
            elif randomer == 3:
                mice_d.append(mouse_d.get_rect(topleft=(random.randint(0, WIDTH - 100),HEIGHT)))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if povorot == 0:
                    bullets_l.append(bullet_l.get_rect(topleft=(player_pos_x-15,player_pos_y+30)))
                elif povorot == 1:
                    bullets_r.append(bullet_r.get_rect(topleft=(player_pos_x+45,player_pos_y+30)))
                elif povorot == 2:
                    bullets_u.append(bullet_u.get_rect(topleft=(player_pos_x+30,player_pos_y-15)))
                elif povorot == 3:
                    bullets_d.append(bullet_d.get_rect(topleft=(player_pos_x+30,player_pos_y+45)))
            elif event.key == pygame.K_e:
                ender = font.render("Управление: ", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 120, HEIGHT / 2 - 130))
                ender = font.render("Вверх - w", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 100, HEIGHT / 2 - 100))
                ender = font.render("Вниз - s", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 100, HEIGHT / 2 - 70))
                ender = font.render("Влево - a", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 100, HEIGHT / 2 - 40))
                ender = font.render("Вправо - d", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 100, HEIGHT / 2 - 10))
                ender = font.render("Стрельба - space", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 100, HEIGHT / 2 + 20))
                ender = font.render("Для продолжения игры нажмите - space", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 230, HEIGHT / 2 + 50))
                pygame.display.update()
                pause()
            elif event.key == pygame.K_q:
                for i in range(len(score_list)):
                    text = font.render(score_list[i][0:len(score_list[i])-1],False,(255,255,255))
                    screen.blit(text,(WIDTH/2-75,HEIGHT/2 - 180 + 30 * i))
                ender = font.render("Для продолжения игры нажмите - space", False, (255, 255, 255))
                screen.blit(ender, (WIDTH / 2 - 230, HEIGHT / 2 + 120))
                pygame.display.update()
                pause()

    for m in mice_r:
        screen.blit(mouse_r, m)
        m.x -= 1
        if m.x <= WIDTH-50:
            m.x = WIDTH-50
        if player_rect.colliderect(m):
            mice_r.remove(m)
            pygame.mixer.music.play(0, 2, 0)
            score += 1

    for m in mice_l:
        screen.blit(mouse_l, m)
        m.x += 1
        if m.x >= 0:
            m.x = 0
        if player_rect.colliderect(m):
            mice_l.remove(m)
            pygame.mixer.music.play(0, 2, 0)
            score += 1

    for m in mice_u:
        screen.blit(mouse_u, m)
        m.y += 1
        if m.y >= 0:
            m.y = 0
        if player_rect.colliderect(m):
            mice_u.remove(m)
            pygame.mixer.music.play(0, 2, 0)
            score += 1

    for m in mice_d:
        screen.blit(mouse_d, m)
        m.y -= 1
        if m.y <= HEIGHT - 50:
            m.y = HEIGHT - 50
        if player_rect.colliderect(m):
            mice_d.remove(m)
            pygame.mixer.music.play(0, 2, 0)
            score += 1

    for e in bullets_r:
        screen.blit(bullet_r, e)
        if e.x > WIDTH+10:
            bullets_r.remove(e)
        else:
            e.x += bullet_speed
        score += some(e,bullets_r,mice_r,mice_l,mice_d,mice_u)

    for e in bullets_l:
        screen.blit(bullet_l, e)
        if e.x < -50:
            bullets_l.remove(e)
        else:
            e.x -= bullet_speed
        score += some(e,bullets_l, mice_r, mice_l, mice_d, mice_u)

    for e in bullets_u:
        screen.blit(bullet_u, e)
        if e.y < -50:
            bullets_u.remove(e)
        else:
            e.y -= bullet_speed
        score += some(e,bullets_u,mice_r,mice_l,mice_d,mice_u)

    for e in bullets_d:
        screen.blit(bullet_d, e)
        if e.y > HEIGHT+20:
            bullets_d.remove(e)
        else:
            e.y += bullet_speed
        score += some(e,bullets_d,mice_r,mice_l,mice_d,mice_u)

    ender = font.render("Времени осталось: " + str(60-time_counter) + "сек", False, (255, 255, 255))
    screen.blit(ender, (20, HEIGHT - 30))
    ender = font.render("Управление - e", False, (255, 255, 255))
    screen.blit(ender, (WIDTH - 200, HEIGHT - 60))
    ender = font.render("10 лучших - q", False, (255, 255, 255))
    screen.blit(ender, (WIDTH - 200, HEIGHT - 30))
    ender = font.render("Ваш счет: " + str(score), False, (255, 255, 255))
    screen.blit(ender, (20, HEIGHT - 60))
    pygame.display.update()

ender = font.render("Ваш счет: " + str(score), False, (255, 255, 255))
screen.blit(ender, (WIDTH/2-70, 250))
pygame.display.update()
time.sleep(1)

score_int = []
for i in range(len(score_list)):
    score_int.append(int(score_list[i][(i+1)//10+3:len(score_list[i])-1]))
print(score_int)
score_int.append(score)
score_int.sort(reverse=True)
file = open('score.txt', 'w')
for i in range(0, 10):
    file.write(str(i + 1) + ". " + str(score_int[i]) +"\n")
file.close()

pygame.quit()