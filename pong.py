import pygame
import sys
import random

def player_animation():
	player.y += player_speed
	opponent.y += opponent_speed
	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_animation():
	global ball_speed_y, ball_speed_x, player_score, opponent_score

	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1

	if ball.left <= 0:
		player_score +=1
		ball_start()

	if ball.right >= screen_width:
		opponent_score +=1
		ball_start()

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def ball_start():
	global ball_speed_y, ball_speed_x
	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

paddlespeed = int(input("Paddle Speed: "))
ballfast = int(input("Ball Speed: "))

def movement():
	global opponent_speed, player_speed, paddlespeed, ballfast
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				player_speed +=paddlespeed
			if event.key == pygame.K_UP:
				player_speed -=paddlespeed
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				player_speed -=paddlespeed
			if event.key == pygame.K_UP:
				player_speed +=paddlespeed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				opponent_speed +=paddlespeed
			if event.key == pygame.K_w:
				opponent_speed -=paddlespeed
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_s:
				opponent_speed -=paddlespeed
			if event.key == pygame.K_w:
				opponent_speed +=paddlespeed


#General Setup
pygame.init()
clock = pygame.time.Clock()

#Main Window
screen_width = 1680
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Ding Dong Ping Pong")

win = pygame.display.set_mode((screen_width, screen_height))

#Colours
colour1 = (31, 31, 31) #grey 12
bg_color = pygame.Color(colour1)
light_grey = (200,200,200)

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

#Game Variables
ball_speed_x = ballfast *random.choice((1,-1))
ball_speed_y = ballfast *random.choice((1,-1))
player_speed = 0
opponent_speed = 0

#Text Variables
player_score = 0
opponent_score = 0
font = pygame.font.Font("freesansbold.ttf", 64)

while True:
	movement()
	ball_animation()
	player_animation()

	# Visuals
	screen.fill(bg_color)
	pygame.draw.rect(screen,light_grey, player)
	pygame.draw.rect(screen,light_grey, opponent)
	pygame.draw.ellipse(screen,light_grey, ball)
	pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

	player_text = font.render(f"{player_score}",False, light_grey)
	screen.blit(player_text,(880,500))
	opponent_text = font.render(f"{opponent_score}",False, light_grey)
	screen.blit(opponent_text,(770,500))

	# Updating the Window
	pygame.display.flip()
	clock.tick(60)
