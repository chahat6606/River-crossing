import pygame
pygame.init()

# variables used through the code
number_of_enemies = 5
number_of_obstacles = 5
player1_active = True
player2_active = False
obstaclelist = []
enemylist = []
roadlist = []
cnt_player2 = 0
cnt_player1 = 0
score_player1 = 0
score_player2 = 0
total_times_p1_played = 0
total_times_p2_played = 0
player1_time_elapsed = 0
player2_time_elapsed = 0
player1_last_timecnt = 0
player2_last_timecnt = 0
time_per_round = 0
total_time_elapsed = 0
time_count = 0
player_width = 40
round_cnt = 3
bgcolor = [173, 216, 230]  # light blue
red = [255, 0, 0]
white = [255, 255, 255]
black = [0, 0, 0]

# Images and Background Track
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1, 0.0)
enemyImg = pygame.image.load('enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (50, 50))
roadImg = pygame.image.load('sea.png')
roadImg = pygame.transform.scale(roadImg, (700, 70))
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (40, 40))
obstacleImg = pygame.image.load('caution.png')
obstacleImg = pygame.transform.scale(obstacleImg, (50, 50))


# Messages
player1_win_message = "Player 1 Wins!!"
player2_win_message = "Player 2 Wins!!"
player1_time_win = "Player 1 Wins by Time!"
player2_time_win = "Player 2 Wins by Time!"
