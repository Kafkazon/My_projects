import time
import pygame
import random

WIDTH = 900
HEIGHT = 600
FPS = 20

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

font = pygame.font.Font(None, 36)

bg = pygame.image.load("images/bg.png").convert_alpha()
snow = pygame.image.load("images/snow.png").convert_alpha()
shield_1 = pygame.image.load("images/shield_1.png").convert_alpha()
shield_2 = pygame.image.load("images/shield_2.png").convert_alpha()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
player = pygame.image.load("images/up.png").convert_alpha()
left = [pygame.image.load("images/left_1.png").convert_alpha(),
pygame.image.load("images/left_2.png").convert_alpha(),
pygame.image.load("images/left_3.png").convert_alpha(),
pygame.image.load("images/left_4.png").convert_alpha()]
right = [pygame.image.load("images/right_1.png").convert_alpha(),
pygame.image.load("images/right_2.png").convert_alpha(),
pygame.image.load("images/right_3.png").convert_alpha(),
pygame.image.load("images/right_4.png").convert_alpha()]
clock = pygame.time.Clock()

count = 0
time_counter = 0
fps_counter = 0
player_pos_x = WIDTH/2
player_pos_y = HEIGHT-80
player_speed = 15
jump_energy = 6
snow_speed = 10

snowballs = []
shields = []

snowball_timer = pygame.USEREVENT + 1
pygame.time.set_timer(snowball_timer, 1000)
try:
    f = open("score.txt")
except IOError:
    f = open('score.txt', 'w')
    for i in range(0, 10):
        f.write(str(i + 1) + ". 0\n")
    f.close()
f = open("score.txt", "r")
score_int_list = []
score_string_list = f.readlines()
f.close()

running = True
flag_end = 1
flag_pause = 0
flag_shield = 0
flag_jump = 0
m = 7

while running:
    clock.tick(FPS)
    #screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    fps_counter += 1
    if fps_counter == FPS:
        time_counter += 1
        if time_counter % 5 == 0:
            snow_speed += 1
        fps_counter = 0

    if flag_end == 0:
        end = font.render("Проигрыш!", True, (0,0,0))
        screen.blit(end, (WIDTH / 2 - 70, HEIGHT / 2 - 100))
        running = False

    hold = pygame.key.get_pressed()
    if hold[pygame.K_d]:
        count += 1
        count = count % len(right)
        screen.blit(right[count], (player_pos_x,player_pos_y))
        player_pos_x = player_pos_x + player_speed
        if player_pos_x > (WIDTH - 50):
            player_pos_x = WIDTH - 50
    elif hold[pygame.K_a]:
        count += 1
        count = count % len(left)
        screen.blit(left[count], (player_pos_x, player_pos_y))
        player_pos_x = player_pos_x - player_speed
        if player_pos_x < 10:
            player_pos_x = 10
            if (flag_shield):
                screen.blit(shield_2, (player_pos_x + 20, player_pos_y + 40))
        elif (flag_shield):
            screen.blit(shield_2, (player_pos_x + 30, player_pos_y + 40))
    else:
        count = 0
        screen.blit(player, (player_pos_x, player_pos_y))
        if(flag_shield):
            screen.blit(shield_2, (player_pos_x-10, player_pos_y+40))

    player_rect = player.get_rect(topleft=(player_pos_x,player_pos_y))

    if hold[pygame.K_q]:
        score_table_upper = font.render("10 лучших результатов", False, (0,0,0))
        screen.blit(score_table_upper, (0, 170))
        for i in range(0,10):
            score_table = font.render(score_string_list[i][0:len(score_string_list[i])-1], False, (0,0,0))
            screen.blit(score_table,(30,200+i*22))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == snowball_timer:
            if(random.randint(0,100) < 10):
                shields.append(shield_1.get_rect(topleft=(random.randint(0,WIDTH-100),-20)))
            else:
                snowballs.append(snow.get_rect(topleft=(random.randint(0,WIDTH-100),-20)))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag_jump = 1
            elif event.key == pygame.K_p:
                flag_pause = 1

    while flag_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_start = True
                running = False
                flag_pause = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    flag_pause = False
    if flag_jump:
        if m > 0:
            player_pos_y -= jump_energy**2/2
            m -= 1
        elif m > -7:
            player_pos_y += jump_energy**2/2
            m -= 1
        else:
            m = 7
            flag_jump = 0

    for e in snowballs:
        screen.blit(snow, e)
        if player_rect.colliderect(e):
            if(flag_shield):
                flag_shield = 0
            else:
                flag_end = 0
            snowballs.remove(e)
        elif e.y > HEIGHT-50:
            e.y += 1
        elif e.y > HEIGHT:
            snowballs.remove(e)
        else:
            e.y += snow_speed

    for e in shields:
        screen.blit(shield_1, e)
        if player_rect.colliderect(e):
             flag_shield = 1
             shields.remove(e)
        elif e.y > HEIGHT:
            shields.remove(e)
        else:
            e.y += snow_speed

    ender = font.render("Управление: ", False, (0, 0, 0))
    screen.blit(ender, (0, 0))
    ender = font.render("Влево - a", False, (0, 0, 0))
    screen.blit(ender, (0, 30))
    ender = font.render("Вправо - d ", False, (0, 0, 0))
    screen.blit(ender, (0, 60))
    ender = font.render("Прыжок - space", False, (0, 0, 0))
    screen.blit(ender, (0, 90))
    ender = font.render("Пауза - p", False, (0, 0, 0))
    screen.blit(ender, (0, 120))
    ender = font.render("Таблица лучших - q", False, (0, 0, 0))
    screen.blit(ender, (0, 150))
    ender = font.render("Время: " + str(time_counter) + "сек", False, (0, 0, 0))
    screen.blit(ender, (WIDTH-150, 20))
    pygame.display.update()

ender = font.render("Ваше время: " + str(time_counter) + "сек", False, (0,0,0))
screen.blit(ender, (WIDTH/2-100, 250))

pygame.display.update()
time.sleep(1)

for i in range(0, 10):
    score_int_list.append(int(score_string_list[i][((i + 1) // 10 + 2):len(score_string_list[i])]))

score_int_list.append(time_counter)
score_int_list.sort(reverse=True)
score_int_list = score_int_list[0:10]

file = open('score.txt', 'w')
for i in range(0,10):
    file.write(str(i+1) + ". " + str(score_int_list[i]) + "\n")
file.close()

pygame.quit()