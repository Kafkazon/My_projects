import time
import pygame
import random

WIDTH = 900
HEIGHT = 600
FPS = 40


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

font = pygame.font.Font(None, 36)
font_new = pygame.font.Font(None, 28)
bg = pygame.image.load("images/bg.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
grib1 = pygame.image.load("images/grib1.png").convert_alpha()
grib2 = pygame.image.load("images/grib2.png").convert_alpha()
grib3 = pygame.image.load("images/grib3.png").convert_alpha()

up = [pygame.image.load("images/up1.png").convert_alpha(),
      pygame.image.load("images/up2.png").convert_alpha(),
      pygame.image.load("images/up3.png").convert_alpha(),
      pygame.image.load("images/up4.png").convert_alpha()]
down = [pygame.image.load("images/down1.png").convert_alpha(),
        pygame.image.load("images/down2.png").convert_alpha(),
        pygame.image.load("images/down3.png").convert_alpha(),
        pygame.image.load("images/down4.png").convert_alpha(),
        pygame.image.load("images/down5.png").convert_alpha()]
left = [pygame.image.load("images/left1.png").convert_alpha(),
        pygame.image.load("images/left2.png").convert_alpha(),
        pygame.image.load("images/left3.png").convert_alpha(),
        pygame.image.load("images/left4.png").convert_alpha(),
        pygame.image.load("images/left5.png").convert_alpha()]
right = [pygame.image.load("images/right1.png").convert_alpha(),
         pygame.image.load("images/right2.png").convert_alpha(),
         pygame.image.load("images/right3.png").convert_alpha(),
         pygame.image.load("images/right4.png").convert_alpha(),
         pygame.image.load("images/right5.png").convert_alpha()]

clock = pygame.time.Clock()
view = up[0]
view_end = up[0]
count = 0
count_pogan = 0
time_counter = 0
fps_counter = 0
player_pos_x = WIDTH/2
player_pos_y = HEIGHT/2-100
player_speed = 10
mushroom_live = FPS*10
score = 0
randomer = 0
mushrooms_1 = []
mushrooms_2 = []
mushrooms_3 = []
mushroom_timer = pygame.USEREVENT + 1
pygame.time.set_timer(mushroom_timer, 1000)

flag_start = False
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

text = font.render("Здравствуйте!", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 100, HEIGHT/2 - 150))
text = font.render("Вам необходимо собирать грибы, появляющиеся на поле", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 340, HEIGHT/2 - 120))
text = font.render("Всего на игру выделено 90 сек", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 200, HEIGHT/2 - 90))
text = font.render("Белый гриб +10 баллов", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 140, HEIGHT/2 - 60))
text = font.render("Гриб из Марио +5 баллов", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 140, HEIGHT/2 - 30))
text = font.render("Поганка -10баллов", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 140, HEIGHT/2))
text = font.render("Сбор 3 поганок ведет к проигрышу без учета результата", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 320, HEIGHT/2+30))
text = font.render("Для начала игры нажмите клавишу Space", False, (255,255,255))
screen.blit(text, (WIDTH/2 - 240, HEIGHT/2+60))
pygame.display.update()

while not flag_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_start = True
            flag_end_in_start = True
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag_start = True

while running:
    clock.tick(FPS)
    #screen.fill((0, 0, 0))
    screen.blit(bg,(0,0))

    fps_counter += 1
    if fps_counter == FPS:
        time_counter += 1
        if time_counter % 3 == 0 and mushroom_live > FPS*5:
            mushroom_live -= 1
        fps_counter = 0

    if count_pogan > 2:
        end = font.render("Игра завершена!", True, (255, 255, 255))
        screen.blit(end, (WIDTH / 2 - 100, HEIGHT / 2 - 100))
        end = font.render("Счет не засчитан!", True, (255, 255, 255))
        screen.blit(end, (WIDTH / 2 - 90, HEIGHT / 2 - 70))
        running = False
        flag_end_in_start = True

    elif time_counter > 90:
        end = font.render("Игра завершена!", True, (255, 255, 255))
        screen.blit(end, (WIDTH / 2 - 100, HEIGHT / 2 - 100))
        running = False

    hold = pygame.key.get_pressed()
    if hold[pygame.K_d] or hold[pygame.K_a] or hold[pygame.K_w] or hold[pygame.K_s]:
        if hold[pygame.K_d]:
            count += 1
            count = count % len(right)
            view = right[count]
            view_end = right[0]
            screen.blit(view, (player_pos_x,player_pos_y))
            player_pos_x = player_pos_x + player_speed
            if player_pos_x > (WIDTH - 100):
                player_pos_x = WIDTH - 100
        elif hold[pygame.K_a]:
            count += 1
            count = count % len(left)
            view = left[count]
            view_end = left[0]
            screen.blit(view, (player_pos_x, player_pos_y))
            player_pos_x = player_pos_x - player_speed
            if player_pos_x < 0:
                player_pos_x = 0
        elif hold[pygame.K_w]:
            count += 1
            count = count % len(up)
            view = up[count]
            view_end = up[0]
            screen.blit(view, (player_pos_x, player_pos_y))
            player_pos_y = player_pos_y - player_speed
            if player_pos_y < 0:
                player_pos_y = 0
        elif hold[pygame.K_s]:
            count += 1
            count = count % len(down)
            view = down[count]
            view_end = down[0]
            screen.blit(view, (player_pos_x, player_pos_y))
            player_pos_y = player_pos_y + player_speed
            if player_pos_y > HEIGHT-100:
                player_pos_y = HEIGHT-100
    else:
        count = 0
        screen.blit(view_end, (player_pos_x, player_pos_y))

    player_rect = view.get_rect(topleft=(player_pos_x, player_pos_y))

    if hold[pygame.K_q]:
        score_table_upper = font.render("10 лучших результатов", False, (255, 255, 255))
        screen.blit(score_table_upper, (0, 170))
        for i in range(0,10):
            score_table = font.render(score_list[i][0:len(score_list[i])-1], False, (255, 255, 255))
            screen.blit(score_table,(30,200+i*20))
        score_table = font.render("Для продолжения игры нажмите Пробел", False, (255, 255, 255))
        screen.blit(score_table, (0, 200 + 10 * 20))
        pygame.display.update()
        flag_pause = True
        while flag_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    flag_pause = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flag_pause = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == mushroom_timer:
            randomer = random.randint(0,2)
            if randomer == 0:
                mushrooms_1.append(grib1.get_rect(topleft=(random.randint(0, WIDTH - 100),random.randint(0, HEIGHT - 100))))
            elif randomer == 1:
                mushrooms_2.append(grib2.get_rect(topleft=(random.randint(0, WIDTH - 100),random.randint(0, HEIGHT - 100))))
            elif randomer == 2:
                mushrooms_3.append(grib3.get_rect(topleft=(random.randint(0, WIDTH - 100),random.randint(0, HEIGHT - 100))))

    for e in mushrooms_1:
        screen.blit(grib1, e)
        if player_rect.colliderect(e):
             mushrooms_1.remove(e)
             score += 10
        if len(mushrooms_2) > 0:
            if mushrooms_2[len(mushrooms_2)-1].colliderect(e):
                mushrooms_1.remove(e)
        if len(mushrooms_3) > 0:
            if mushrooms_3[len(mushrooms_3)-1].colliderect(e):
                mushrooms_1.remove(e)

    for e in mushrooms_2:
        screen.blit(grib2, e)
        if player_rect.colliderect(e):
            mushrooms_2.remove(e)
            score += 5
        if len(mushrooms_1) > 0:
            if mushrooms_1[len(mushrooms_1) - 1].colliderect(e):
                mushrooms_2.remove(e)
        if len(mushrooms_3) > 0:
            if mushrooms_3[len(mushrooms_3) - 1].colliderect(e):
                mushrooms_2.remove(e)

    for e in mushrooms_3:
        screen.blit(grib3, e)

        if player_rect.colliderect(e):
            mushrooms_3.remove(e)
            count_pogan += 1
            score -= 10
            if score < 0:
                score = 0
        if len(mushrooms_1) > 0:
            if mushrooms_1[len(mushrooms_1) - 1].colliderect(e):
                mushrooms_3.remove(e)
        if len(mushrooms_2) > 0:
            if mushrooms_2[len(mushrooms_2) - 1].colliderect(e):
                mushrooms_3.remove(e)

    ender = font.render("Времени осталось: " + str(90-time_counter) + "сек", False, (255, 255, 255))
    screen.blit(ender, (20, HEIGHT - 30))
    ender = font.render("Поганок собрано: " + str(count_pogan), False, (255, 255, 255))
    screen.blit(ender, (20, HEIGHT - 60))
    ender = font.render("Ваш счет: " + str(score), False, (255, 255, 255))
    screen.blit(ender, (20, HEIGHT - 90))
    ender = font.render("Управление: ", False, (255,255,255))
    screen.blit(ender, (WIDTH - 250, HEIGHT - 130))
    ender = font.render("Вверх - w", False, (255,255,255))
    screen.blit(ender, (WIDTH - 230, HEIGHT - 110))
    ender = font.render("Вниз - s", False, (255,255,255))
    screen.blit(ender, (WIDTH - 230, HEIGHT - 90))
    ender = font.render("Влево - a", False, (255,255,255))
    screen.blit(ender, (WIDTH - 230, HEIGHT - 70))
    ender = font.render("Вправо - d", False, (255,255,255))
    screen.blit(ender, (WIDTH - 230, HEIGHT - 50))
    ender = font.render("Лучшие прохождения - q", False, (255, 255, 255))
    screen.blit(ender, (WIDTH - 330, HEIGHT - 30))
    pygame.display.update()

time.sleep(1)
if not flag_end_in_start:
    ender = font.render("Ваш счет: " + str(score), False, (255, 255, 255))
    screen.blit(ender, (WIDTH/2-70, 250))
    pygame.display.update()
    time.sleep(1)

    score_int = []
    for i in range(len(score_list)):
        score_int.append(int(score_list[i][(i + 1) // 10 + 3:len(score_list[i]) - 1]))
    score_int.append(score)
    score_int.sort(reverse=True)
    file = open('score.txt', 'w')
    for i in range(0, 10):
        file.write(str(i + 1) + ". " + str(score_int[i]) + "\n")
    file.close()

pygame.quit()