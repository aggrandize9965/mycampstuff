


# -*- coding: utf-8 -*-




#import modules

import pygame

import random

import time

from uagame import *


def collision_with_boundaries(snake_head):

    # if snake is outside of boundaries return 1
    if snake_head[0]>=display_width or snake_head[0]<0 or snake_head[1]>=display_height or snake_head[1]<0:
        return 1 
    else:
        return 0
        

def generate_snake(snake_head, snake_position, button_direction, snake_hit_food):

    #uses button_direction to decide where snake head will go
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10
        
    snake_position.insert(0, list(snake_head))
    snake_position.pop()
    
    if snake_hit_food:
        print("---------------->", snake_hit_food)
        if button_direction == 1:
            snake_head[0] += 10
        elif button_direction == 0:
            snake_head[0] -= 10
        elif button_direction == 2:
            snake_head[1] += 10
        elif button_direction == 3:
            snake_head[1] -= 10
        
        snake_position.insert(0, list(snake_head))
        snake_hit_food = False
        
     
    print(snake_position)
    
    
    return snake_position


def display_snake(snake_position):

    crossover = False 
    #uses list of snake's positions to display snake
    for position in snake_position:
        if snake_position.count(position)>=2:
            crossover = True
        else:
            pygame.draw.rect(display,player_color,pygame.Rect(position[0], position[1],10,10))
    return crossover
    

def play_game(snake_head, snake_position, button_direction,display_width,display_height, snake_hit_food):
    crashed = False
    pellet1_y=random.randint(1, display_height /10) * 10
    pellet2_y=random.randint(1,display_height/ 10) * 10  
    pellet1_x=random.randint(1, display_height /10) * 10
    pellet2_x=random.randint(1,display_height/ 10) * 10    
    pellet1 = Food(pellet1_x, pellet1_y)
    pellet2 = Food(pellet2_x, pellet2_y)
    score = 0 
    while crashed is not True:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True 

            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button_direction = 0 
                elif event.key == pygame.K_RIGHT:
                    button_direction = 1
                elif event.key == pygame.K_UP:
                    button_direction = 3 
                elif event.key == pygame.K_DOWN:
                    button_direction = 2

            
        #moves snake position
        snake_position = generate_snake(snake_head , snake_position, button_direction, snake_hit_food)
        snake_hit_food = False
        
    
        #display background and snake
        display.fill(window_color)
        window.draw_string("Score: "+str(score), 20, 20)
        endgame = display_snake(snake_position)
        print("endgame = --------->" ,endgame)
        if endgame:
            crashed = True 
        
        
        if pellet1.show:
            pellet1.display()
        
        
        if pellet2.show:
            pellet2.display()
        
        #display_pellets(pellet1_x,pellet2_x,pellet1_y,pellet2_y)
        pygame.display.update()
                

        #ends game loop if snake leaves the boundary
        if collision_with_boundaries(snake_head) == 1:
            crashed = True
        if pellet1.collidepoint(snake_head[0], snake_head[1]):
            
            pellet1.hide()
            print("hit pellet 1")
            snake_hit_food = True
            score = score + 1
            pellet1_x=random.randint(1, display_height /10) * 10
            pellet1_y=random.randint(1, display_height /10) * 10
            pellet1 = Food(pellet1_x, pellet1_y)
            
        if pellet2.collidepoint(snake_head[0], snake_head[1]):
            
            pellet2.hide()
            print("hit pellet 2")
            snake_hit_food = True
            score = score+1
            pellet2_x=random.randint(1, display_height /10) * 10
            pellet2_y=random.randint(1, display_height /10) * 10
            pellet2 = Food(pellet2_x, pellet2_y)            
           
        clock.tick(20)



    
class Food:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.show = True
        
    def display(self):
        pygame.draw.rect(display,pygame.Color(255,255,0),pygame.Rect(self.x,self.y,10,10))
    
    def hide(self):
        pygame.draw.rect(display,pygame.Color(102,255,255),pygame.Rect(self.x,self.y,10,10))
        pygame.display.update()
        
        
    def collidepoint(self, sx, sy):
        if (sx== self.x and sy == self.y):
            self.show = False
           
            return True
        else:
            return False
            
    

if __name__ == "__main__":
    

    # set variables
    
    display_width = 800

    display_height = 600

    player_color = (255,255,255)

    window_color = (102,255,255)

    clock=pygame.time.Clock()

    

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]
    snake_hit_food = False
    
    #initialize pygame modules    

    pygame.init()

    

    #display game window
    window = Window('Snake Game', display_width, display_height)
    window.set_font_color('black')
    #window.set_font_name('hobostd')    
    window.set_bg_color('white')    
    
    #window.draw_string("Score: ", 20, 20)
    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    #pygame.display.set_caption("Snake Game")
   

    pygame.display.update()
  
    #start the game loop
    
    play_game(snake_head, snake_position, 1,display_width, display_height, snake_hit_food)
    



pygame.quit()