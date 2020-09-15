#!/usr/bin/python
"""
Owner:- Pukhraj
Description:- Ping Pong game written using
              pygame python module
"""
# General modules
import pygame
import sys
import random

# Global variables
WIDTH = 800
HEIGHT = 500
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")
ball = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)
player = pygame.Rect(WIDTH - 20, HEIGHT / 2 - 70, 10, 120)
opponent = pygame.Rect(10, HEIGHT / 2 - 70, 10, 120)
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)


class pingpong():
    def __init__(self):
        """
        Constructor defining default values of the object
        """
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        self.facing_x = 1
        self.facing_y = 1
        self.score_play = 0
        self.score_oppo = 0

    def player(self):
        """
        Player bar movement is handled in this function
        :return:
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and player.bottom <= 500:
            player.y += 5
        if keys[pygame.K_UP] and player.top >= 0:
            player.y -= 5
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= HEIGHT:
            opponent.bottom = HEIGHT

    def ball_moving(self):
        """
        Ball movement is handled in this function
        :return:
        """
        if self.facing_x > 0:
            ball.x += self.ball_speed_x * self.facing_x
            ball.y += self.ball_speed_y * self.facing_y
            if ball.x == 770:
                self.facing_x = -1
            if ball.y == 500:
                self.facing_y = -1
            if ball.y == 0:
                self.facing_y = 1
        else:
            ball.x += self.ball_speed_x * self.facing_x
            ball.y += self.ball_speed_y * self.facing_y
            if ball.x == 10:
                self.facing_x = 1
            if ball.y == 0:
                self.facing_y = 1
            if ball.y == 500:
                self.facing_y = -1

    def check_failure(self):
        """
        If ball doesn't hit the player or opponent bar, the game will restart
        :return:
        """
        if ball.x == 770:
            if player.top < ball.y < player.bottom:
                self.score_play += 1
                pygame.mixer.Sound('pong.wav').play()
            else:
                self.ball_restart()
        if ball.x == 10:
            if opponent.top < ball.y < opponent.bottom:
                self.score_oppo += 1
                pygame.mixer.Sound('pong.wav').play()
            else:
                self.ball_restart()

    def ball_restart(self):
        """
        Once the game restart's, ball will be placed
        in the middle with score of each player and
        opponent as zero
        :return:
        """
        ball.center = (WIDTH / 2, HEIGHT / 2)
        self.score_play = 0
        self.score_oppo = 0
        # self.ball_speed_x *= random.choice((1,-1))
        # self.ball_speed_y *= random.choice((1,-1))
        # print (ball.right)
        # print (player.top)
        # print (player.bottom)

    def opponent(self):
        """
        opponent bar automatic movement is handled in this function
        :return:
        """
        if opponent.top < ball.y:
            opponent.top += 5
        if opponent.bottom > ball.y:
            opponent.bottom -= 5

    def draw(self):
        """
        all the images are drawn using this function
        :return:
        """
        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
        text = font.render(str(self.score_play), 1, (255, 255, 255))
        screen.blit(text, (WIDTH / 2 + 10, HEIGHT / 2))
        text = font.render(str(self.score_oppo), 1, (255, 255, 255))
        screen.blit(text, (WIDTH / 2 - 20, HEIGHT / 2))
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    font = pygame.font.SysFont("comicsans", 30, True)
    ping = pingpong()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ping.draw()
        ping.ball_moving()
        ping.player()
        ping.opponent()
        ping.check_failure()
