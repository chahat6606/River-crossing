import math
import random
import pygame
from config import *

pygame.init()

screen = pygame.display.set_mode((640, 900))
pygame.display.set_caption("River Crossing")
screen.fill(bgcolor)


class ENEMY:
    global enemyImg
    # enemy
    # enemyX_change=3
    # enemyY_change=0

    def __init__(self, x, y):
        self.enemyX = x
        self.enemyY = y
        self.enemyX_change = 3

    def enemy(self, x, y):
        #pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
        screen.blit(enemyImg, (x, y))


class OBSTACLE:
    global obstacleImg

    def __init__(self, x, y):
        self.obstacleX = x
        self.obstacleY = y

    def obstacle(self, x, y):
        screen.blit(obstacleImg, (x, y))
      #  pygame.draw.rect(screen, (255, 255, 0), (x, y, 50, 50))


class PLAYER:
    global playerImg
    playerX_change = 0
    playerY_change = 0

    def __init__(self, x, y):
        pygame.draw.rect(screen, (255, 255, 255),
                         (x, y, player_width, player_width))

        self.playerX = x
        self.playerY = y

    playerY = 600
    playerX_change = 0
    playerY_change = 0

    def player(self, x, y):
        screen.blit(playerImg, (x, y))
       # pygame.draw.rect(screen, (255, 255, 255),
        #                 (x, y, player_width, player_width))


class ROAD:
    global roadImg

    def __init__(self, x, y):
        self.roadX = x
        self.roadY = y
    roadX_change = 0
    roadY_change = 0

    def road(self, x, y):
        screen.blit(roadImg, (x - 20, y + 50))
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 640, 50))


p1 = PLAYER(320, 800)
p2 = PLAYER(320, 0)
# list of objects of a road and creating roads


def add_roads():
    global ROAD
    yc = 0
    for i in range(6):
        roadlist.append(ROAD(0, yc))  # 120,240,360,480,600 pe roads hai
        yc += 120

# creating enemies here number of enemies is total_enemies_enemies and
# enemies per row ncreases with level


def add_enemies():
    global ENEMY
    enemyyc = 60
    for j in range(number_of_enemies):
        enemylist.append(ENEMY(random.randint(60, 580), enemyyc))
        enemyyc += 120


def add_obstacles():
    global OBSTACLE
    obstacleyc = 120
    for i in range(number_of_obstacles):
        obstaclexc = random.randint(0, 120)
        obstaclelist.append(OBSTACLE(obstaclexc, obstacleyc))
        obstaclexc = random.randint(200, 400)
        obstaclelist.append(OBSTACLE(obstaclexc, obstacleyc))
        obstaclexc = random.randint(450, 580)
        obstaclelist.append(OBSTACLE(obstaclexc, obstacleyc))
        obstacleyc += 120


add_obstacles()
add_enemies()
add_roads()

score = 0
# game loop


# collision checker
def iscollisionmoving(enemyX, enemyY, playerX, playerY):
    if playerX >= enemyX and playerX <= enemyX + 50:
        if playerY >= enemyY and playerY <= enemyY + 50:
            return True
        if playerY + player_width >= enemyY and playerY + player_width <= enemyY + 50:
            return True

    if playerX + player_width >= enemyX and playerX + player_width <= enemyX + 50:
        if playerY >= enemyY and playerY <= enemyY + 50:
            return True
        if playerY + player_width >= enemyY and playerY + player_width <= enemyY + 50:
            return True
    return False


def iscollisionfixed(enemyX, enemyY, playerX, playerY):
    if playerX >= enemyX and playerX <= enemyX + 50:
        if playerY >= enemyY and playerY <= enemyY + 50:
            return True
        if playerY + player_width >= enemyY and playerY + player_width <= enemyY + 50:
            return True

    if playerX + player_width >= enemyX and playerX + player_width <= enemyX + 50:
        if playerY >= enemyY and playerY <= enemyY + 50:
            return True
        if playerY + player_width >= enemyY and playerY + player_width <= enemyY + 50:
            return True
    return False

# def calc_player1():


def get_player1_score():
    global PLAYER
    global score_player1
    global p1
    global player1_active
    # global p1.playerY
    if p1.playerY >= 650:
        score_player1 += 0
        return
    if player1_active:
        x = p1.playerY // 50
        y = (12 - x) // 2
        score_player1 = score_player1 + y * 10 + (12 - x - y) * 15


def get_player2_score():
    global PLAYER
    global p2
    global player2_active
    global score_player2
    if player2_active:
        if p2.playerY <= 50:
            return
        x = p2.playerY // 50
        y = (x - 1) // 2
        score_player2 += (y * 15 + (x - 1 - y) * 10)


running = True
Clock = pygame.time.Clock()
while running:

    # pygame.time.delay(50)
    Clock.tick(60)
    screen.fill((0, 0, 255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    if player1_active:
        # keystroke  is pressed check whether its right or left

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                p1.playerX_change = -5
                #("left arrow is pressed")

            if event.key == pygame.K_RIGHT:
                p1.playerX_change = 5
                #("right arrow is pressed")

            if event.key == pygame.K_UP:
                p1.playerY_change = -5

            if event.key == pygame.K_DOWN:
                p1.playerY_change = 5

        if event.type == pygame.KEYUP:
            # ("released")
            p1.playerX_change = 0
            p1.playerY_change = 0

        # player movement
        p1.playerX += p1.playerX_change
        p1.playerY += p1.playerY_change
        if p1.playerX < 0:
            p1.playerX = 0
        if p1.playerX > 590:
            p1.playerX = 590
        if p1.playerY >= 750:
            p1.playerY = 750
        if p1.playerY < 0:
            p1.playerY = 0
    else:
        # control for player2
        # keystroke  is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                p2.playerX_change = -5
                #("left arrow is pressed")

            if event.key == pygame.K_d:
                p2.playerX_change = 5
                #("right arrow is pressed")

            if event.key == pygame.K_w:
                p2.playerY_change = -5

            if event.key == pygame.K_s:
                p2.playerY_change = 5

        if event.type == pygame.KEYUP:
            # ("released")
            p2.playerX_change = 0
            p2.playerY_change = 0

        # player movement
        p2.playerX += p2.playerX_change
        p2.playerY += p2.playerY_change
        if p2.playerX < 0:
            p2.playerX = 0
        if p2.playerX > 590:
            p2.playerX = 590
        if p2.playerY >= 750:
            p2.playerY = 750
        if p2.playerY < 0:
            p2.playerY = 0

    # this is for roads nothing needs to be done now in this
    for i in range(6):
        roadlist[i].road(roadlist[i].roadX, roadlist[i].roadY)

        # call the blipping function
    p1.player(p1.playerX, p1.playerY)
    p2.player(p2.playerX, p2.playerY)

    # making the ship obstacles
    for i in range(15):
        obstaclelist[i].obstacle(
            obstaclelist[i].obstacleX,
            obstaclelist[i].obstacleY)

    # adding enemies on the screen
    for i in range(number_of_enemies):
        if enemylist[i].enemyX > (640 - 50) or enemylist[i].enemyX < 0:
            enemylist[i].enemyX_change *= (-1)

        enemylist[i].enemyX += enemylist[i].enemyX_change
        enemylist[i].enemy(enemylist[i].enemyX, enemylist[i].enemyY)

    # collision detection with moving obstacles
    for i in range(number_of_enemies):
        if player1_active:
            if iscollisionmoving(
                    enemylist[i].enemyX,
                    enemylist[i].enemyY, p1.playerX, p1.playerY):
                total_times_p1_played += 1
                ("its over-player1")
                get_player1_score()
                total_time_elapsed = pygame.time.get_ticks()
                p1.playerY = 800
                p1.playerX = 295
                cnt_player1 = 0
                total_times_p1_played += 1
                for i in range(number_of_enemies):
                    if enemylist[i].enemyX_change < 0:
                        enemylist[i].enemyX_change = -(3 + cnt_player2 * 3)
                    else:
                        enemylist[i].enemyX_change = (3 + cnt_player2 * 3)
                player2_active = True
                player1_active = False
                player1_time_elapsed += (pygame.time.get_ticks() -
                                         player1_last_timecnt)
                player1_last_timecnt = pygame.time.get_ticks()
        else:
            if iscollisionmoving(
                    enemylist[i].enemyX,
                    enemylist[i].enemyY, p2.playerX, p2.playerY):
                total_times_p2_played += 1
                ("its over-player2")
                get_player2_score()
                total_time_elapsed = pygame.time.get_ticks()
                round_cnt -= 1
                p2.playerY = 0
                p2.playerX = 295
                cnt_player2 = 0
                # update the enemy speed
                for i in range(number_of_enemies):
                    if enemylist[i].enemyX_change < 0:
                        enemylist[i].enemyX_change = -(3 + cnt_player1 * 3)
                    else:
                        enemylist[i].enemyX_change = (3 + cnt_player1 * 3)
                player1_active = True
                player2_active = False
                player2_time_elapsed += (pygame.time.get_ticks() -
                                         player2_last_timecnt)
                player2_last_timecnt = pygame.time.get_ticks()

    # collision detection obstacles first for player 1 and second for player 2
    for i in range(15):
        if player1_active:
            if iscollisionfixed(
                    obstaclelist[i].obstacleX,
                    obstaclelist[i].obstacleY, p1.playerX, p1.playerY):

                ("its over-player1")
                get_player1_score()
                total_time_elapsed = pygame.time.get_ticks()

                p1.playerY = 800
                p1.playerX = 295
                cnt_player1 = 0
                total_times_p1_played += 1
                for i in range(number_of_enemies):
                    if enemylist[i].enemyX_change < 0:
                        enemylist[i].enemyX_change = -(3 + cnt_player2 * 3)
                    else:
                        enemylist[i].enemyX_change = (3 + cnt_player2 * 3)
                player1_active = False
                player2_active = True
                player1_time_elapsed += (pygame.time.get_ticks() -
                                         player1_last_timecnt)
                player1_last_timecnt = pygame.time.get_ticks()
        else:
            if iscollisionfixed(
                    obstaclelist[i].obstacleX,
                    obstaclelist[i].obstacleY, p2.playerX, p2.playerY):
                ("its overplayer2")
                total_times_p2_played += 1
                get_player2_score()
                total_time_elapsed = pygame.time.get_ticks()
                round_cnt -= 1
                p2.playerY = 0
                p2.playerX = 295
                cnt_player2 = 0
                ("collision")
                for i in range(number_of_enemies):
                    if enemylist[i].enemyX_change < 0:
                        enemylist[i].enemyX_change = -(3 + cnt_player1 * 3)
                    else:
                        enemylist[i].enemyX_change = (3 + cnt_player1 * 3)
                player2_active = False
                player1_active = True
                player2_time_elapsed += (pygame.time.get_ticks() -
                                         player2_last_timecnt)
                player2_last_timecnt = pygame.time.get_ticks()

    # jeetna
    if player1_active:
        if p1.playerY == 0:
            total_times_p1_played += 1
            cnt_player1 += 1
            score += 1
            (score)
            score_player1 += 125
            total_time_elapsed = pygame.time.get_ticks()

            p1.playerY = 800
            p1.playerX = 295

            for i in range(number_of_enemies):
                if enemylist[i].enemyX_change < 0:
                    enemylist[i].enemyX_change -= (3 * cnt_player2)
                else:
                    enemylist[i].enemyX_change += (3 * cnt_player2)
            player1_active = False
            player2_active = True
            player1_time_elapsed += (pygame.time.get_ticks() -
                                     player1_last_timecnt)
            player1_last_timecnt = pygame.time.get_ticks()

    if player2_active:
        if p2.playerY == 750:
            total_times_p2_played += 1
            total_time_elapsed = pygame.time.get_ticks()
            round_cnt -= 1
            cnt_player2 += 1
            score += 1
            p2.playerY = 0
            p2.playerX = 295
            score_player2 += 125
            for i in range(number_of_enemies):
                if enemylist[i].enemyX_change < 0:
                    enemylist[i].enemyX_change -= (3 * cnt_player1)
                else:
                    enemylist[i].enemyX_change += (3 * cnt_player1)
            player1_active = True
            player2_active = False
            player2_time_elapsed += (pygame.time.get_ticks() -
                                     player2_last_timecnt)
            player2_last_timecnt = pygame.time.get_ticks()

    # total rounds will be three so this is to check that rounds have been
    # completed
    if total_times_p2_played >= 3:
        music_play = False
        # (total_times_p2_played)
        if score_player1 > score_player2:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 900))
            font = pygame.font.Font(None, 36)
            text4 = font.render(player1_win_message, True, (255, 255, 255))
            screen.blit(text4, (120, 328))

        elif score_player2 > score_player1:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 900))
            font = pygame.font.Font(None, 36)
            text4 = font.render(player2_win_message, True, (255, 255, 255))
            screen.blit(text4, (120, 328))
        else:

            if player1_time_elapsed > player2_time_elapsed:
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 900))
                font = pygame.font.Font(None, 36)
                text4 = font.render(
                    player2_time_win, True, (255, 255, 255))
                screen.blit(text4, (120, 328))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 900))
                font = pygame.font.Font(None, 36)
                text4 = font.render(
                    player1_time_win, True, (255, 255, 255))
                screen.blit(text4, (120, 328))

        text5 = font.render("Player1 Total Score:" +
                            str(score_player1), True, (255, 255, 255))
        screen.blit(text5, (120, 378))
        text6 = font.render("Player2 Total Score:" +
                            str(score_player2), True, (255, 255, 255))
        screen.blit(text6, (120, 414))
        text7 = font.render("Player1 Total Time:" +
                            str(player1_time_elapsed / 1000) +
                            " seconds", True, (255, 255, 255))
        screen.blit(text7, (120, 450))
        text8 = font.render("Player2 Total Time:" +
                            str(player2_time_elapsed / 1000) +
                            " seconds", True, (255, 255, 255))
        screen.blit(text8, (120, 486))

    # add in those removed lines after your for loop.
    if total_times_p2_played < 3:
        font = pygame.font.Font(None, 36)
        time_display = font.render("Time:" +
                                   str((pygame.time.get_ticks() -
                                        (total_time_elapsed) -
                                        time_count) //
                                       1000), True, (255, 255, 255))
        score1 = font.render("Player1:" +
                             str(score_player1), True, (255, 255, 255))
        score2 = font.render("Player2:" +
                             str(score_player2), True, (255, 255, 255))
        rounds = font.render("Round Left: " +
                             str(round_cnt), True, (255, 255, 255))
        screen.blit(time_display, (450, 864))
        screen.blit(score1, (450, 832))
        screen.blit(score2, (450, 796))
        screen.blit(rounds, (0, 864))
    pygame.display.update()
