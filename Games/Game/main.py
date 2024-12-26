# Pygame шаблон - скелет для нового проекта Pygame
import time
import pygame

WIDTH = 900
HEIGHT = 600
FPS = 20
# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

f1 = pygame.font.Font(None, 36)

icon = pygame.image.load("images/icon.png").convert_alpha()
pygame.display.set_icon(icon)

# Подгрузка изображений в программу
bomb = pygame.image.load("images/bomb.png").convert_alpha()
bomb = pygame.transform.scale(bomb, (30, 29))
fon = pygame.image.load("images/fon.jpg").convert_alpha()
enemy_1 = pygame.image.load("images/enemy_fleet/fishing_ship_2.png").convert_alpha()
enemy_2 = pygame.image.load("images/enemy_fleet/trade_ship_1.png").convert_alpha()
enemy_3 = pygame.image.load("images/enemy_fleet/war_ship_2.png").convert_alpha()
bomb_end = pygame.image.load("images/bomb_end.png").convert_alpha()
ship_end = pygame.image.load("images/ship_end.png").convert_alpha()
player = pygame.image.load("images/fleet/up.png").convert_alpha()
left_1 = pygame.image.load("images/fleet/left_1.png").convert_alpha()
right_1 = pygame.image.load("images/fleet/right_1.png").convert_alpha()

left = [left_1]
right = [right_1]
clock = pygame.time.Clock()

# Прописываем константы
running = True
count = 0
bomb_counter = 0
score_counter = 0
collide_counter = 0
player_pos_x = WIDTH/2
player_pos_y = HEIGHT-200
player_speed = 15
enemy_speed_1 = 5
enemy_speed_2 = 7
enemy_speed_3 = 10
bomb_speed = 20
bomb_limit = 11

bombs = []
enemies_first = []
enemies_second = []
enemies_third = []


enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1000)

# Проверяем существует ли файл, если нет, то создаем и заполняем нулями
try:
    f = open("results.txt")
except IOError:
    f = open('results.txt', 'w')
    for i in range(0, 10):
        f.write(str(i + 1) + ". 0\n")
    f.close()

# Считываем с файла счет счет игроков
f = open("results.txt", "r")
score_int_list = []
score_string_list = f.readlines()
f.close()

flag_new_level = False
m = 0
m_2 = 0
flag_2 = True

while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    # screen.blit(fon, (0, 0))

    # Начальная надпись с правилами
    if(flag_2):
        if(m_2 < FPS * 1.5):
            rules = f1.render("Чтобы перейти на новый уровень, сбейте 10 кораблей", True, (255, 255, 255))
            screen.blit(rules, (WIDTH / 2 - 350, 200))
            pygame.display.update()
            m_2 += 1
        else:
            flag_2 = 0
            m_2 = 0

    # Усложнение игры, если сбиты 10 кораблей
    if collide_counter == 10:
        flag_new_level = 1
        enemy_speed_1 += 1
        enemy_speed_2 += 1
        enemy_speed_3 += 1
        bomb_limit += 1
        collide_counter = 0
        bomb_counter = 0
    # Надпись о новом уровне
    if flag_new_level:
        if (m < FPS * 2):
            new_level = f1.render("Новый уровень, боезапас пополнен и увеличен ", True, (255, 255, 255))
            screen.blit(new_level, (WIDTH/2-300, HEIGHT/2))
            m += 1
        else:
            flag_new_level = 0
            m = 0
    # Проверка на то, потрачены ли все бомбы, если да, то завершаем игру
    elif not bombs and bomb_counter == bomb_limit:
        end = f1.render("Ты проиграл!", True, (255, 255, 255))
        screen.blit(end, (WIDTH / 2 - 100, HEIGHT / 2 - 100))
        running = False

    # Блок отвечающий за передвижение игрока
    hold = pygame.key.get_pressed()
    if hold[pygame.K_d]:
        count += 1
        count = count % len(right)
        screen.blit(right[count], (player_pos_x-100,player_pos_y))
        player_pos_x = player_pos_x + player_speed
        if player_pos_x > (WIDTH - 90):
            player_pos_x = WIDTH - 90
    elif hold[pygame.K_a]:
        count += 1
        count = count % len(left)
        screen.blit(left[count], (player_pos_x-100, player_pos_y))
        player_pos_x = player_pos_x - player_speed
        if player_pos_x < 100:
            player_pos_x = 100
    else:
        count = 0
        screen.blit(player, (player_pos_x-50, player_pos_y))
    # Блок выводящий топ 10 при нажатии на q
    if hold[pygame.K_q]:
        score_table_upper = f1.render("10 лучших результатов", False, (255, 255, 255))
        screen.blit(score_table_upper, (0, 170))
        for i in range(0,10):
            score_table = f1.render(score_string_list[i][0:len(score_string_list[i])-1], False, (255, 255, 255))
            screen.blit(score_table,(30,200+i*20))

    for event in pygame.event.get():
        # Проверка на нажатие крестика
        if event.type == pygame.QUIT:
            running = False
        # Создание врагов по таймеру
        elif event.type == enemy_timer:
            enemies_first.append(enemy_1.get_rect(topleft=(WIDTH, 10)))
            enemies_second.append(enemy_2.get_rect(topleft=(-50, 70)))
            enemies_third.append(enemy_3.get_rect(topleft=(WIDTH, 130)))
        # Пуск бомб при нажатии пробела
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bomb_counter < bomb_limit:
                    bomb_rect = bomb.get_rect(topleft=(player_pos_x-25,player_pos_y))
                    bombs.append(bomb_rect)
                    bomb_counter += 1

    # Блок отвечающий за передвижение врагов
    for e in enemies_first:
        screen.blit(enemy_1, e)
        e.x -= enemy_speed_1
        # if e.x < -50:
        #     enemies_first.remove(e)

    for e in enemies_second:
        screen.blit(enemy_2, e)
        e.x += enemy_speed_2
        # if e.x > WIDTH+50:
        #     enemies_second.remove(e)

    for e in enemies_third:
        screen.blit(enemy_3, e)
        e.x -= enemy_speed_3

    # Блок отвечающий за передвижение бомб
    for b in bombs:
        if b.y < 10:
            b.y = 10
            screen.blit(bomb_end,b)
            bombs.remove(b)
        else:
            screen.blit(bomb, b)
            b.y -= bomb_speed

    # Блок отвечающий за столкновение бомбы и врага
    for b in bombs:
        for e in enemies_first:
            if b.colliderect(e):
                if e:
                    screen.blit(ship_end, e)
                    enemies_first.remove(e)
                    score_counter += 1
                    collide_counter += 1
                if b:
                    screen.blit(bomb_end, b)
                    bombs.remove(b)
                break
        if bombs:
            for e in enemies_second:
                if b.colliderect(e):
                    if e:
                        screen.blit(ship_end, e)
                        enemies_second.remove(e)
                        collide_counter += 1
                        score_counter += 2
                    if b:
                        screen.blit(bomb_end, b)
                        bombs.remove(b)
                    break
        if bombs:
            for e in enemies_third:
                if b.colliderect(e):
                    if e:
                        screen.blit(ship_end, e)
                        enemies_third.remove(e)
                        collide_counter += 1
                        score_counter += 3
                    if b:
                        screen.blit(bomb_end, b)
                        bombs.remove(b)
                    break
    # Вывод правил, счета и тп
    score = f1.render("Ваш счет: " + str(score_counter), True,(255, 255, 255))
    screen.blit(score,(25,HEIGHT-50))
    count_of_bombs = f1.render("Количество снарядов: " + str(bomb_limit-bomb_counter), True,(255, 255, 255))
    screen.blit(count_of_bombs, (25, HEIGHT - 25))
    rules = f1.render("Управление:", True, (255, 255, 255))
    screen.blit(rules, (WIDTH-300, HEIGHT - 120))
    rules = f1.render("a - вправо", True, (255, 255, 255))
    screen.blit(rules, (WIDTH - 280, HEIGHT - 100))
    rules = f1.render("d - влево", True, (255, 255, 255))
    screen.blit(rules, (WIDTH - 280, HEIGHT - 80))
    rules = f1.render("space - выстрел", True, (255, 255, 255))
    screen.blit(rules, (WIDTH - 280, HEIGHT - 60))
    rules = f1.render("q - лучшие результаты", True, (255, 255, 255))
    screen.blit(rules, (WIDTH - 280, HEIGHT - 40))
    #count_of_bombs = f1.render("Количество снарядов: " + str(bomb_limit - bomb_counter), True, (255, 255, 255))

    pygame.display.update()


time.sleep(1)
# Приведение счета из файла из строчного в целочисленный формат
for i in range(0, 10):
    score_int_list.append(int(score_string_list[i][((i + 1) // 10 + 2):len(score_string_list[i])]))

score_int_list.append(score_counter)
score_int_list.sort(reverse=True)
score_int_list = score_int_list[0:10]
file = open('results.txt', 'w')
# Вывод обновленного топ 10 в файл
for i in range(0,10):
    file.write(str(i+1) + ". " + str(score_int_list[i]) + "\n")
file.close()

pygame.quit()