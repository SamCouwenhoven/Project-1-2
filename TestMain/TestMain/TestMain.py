﻿
print ("hello world" )
print ("het werkt - Minde ")
print ("het werkt -  lennard")
print ("het werkt - Sam is veranderd")
print ("het werkt - Siham")


import pygame
import random
import time
pygame.init()
 
display_width = 800
display_height = 600
blocklength = 170
blockheight = 50
 
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
bright_green = (10,255,10)
bright_red = ( 255,10,10)
block_color = (53,115,255)
 
car_width = 1
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
 
carImg = pygame.image.load("content/blok.png")
boardImg = pygame.image.load("content/board.png")
board = pygame.transform.scale(boardImg,((display_width),(display_height)))
 
 
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
    button("EXIT",display_width-170,0,170,50,red,bright_red,game_intro)

 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()
    
    
 
def crash():
    message_display('You Crashed')
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
def quitgame():
    pygame.quit()
    quit()
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Survivor!!", largeText)
        TextRect.center = ((display_width/2),50)
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",display_width/2-blocklength/2,150,blocklength,blockheight,green,bright_green,game_loop)
        button("INSTRUCTIONS",display_width/2-blocklength/2,230,blocklength,blockheight,blue,blue,instructions)
        button("EXIT",display_width/2-blocklength/2,310,blocklength,blockheight,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
def instructions():
    while (instructions == True):
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    largetext = pygame.font.SysFont("comicsansms", 20)
    Textplace, TextRect = text_objects("Instructions",largetext)
    TextRect.center = ((display_width/2),50)
    gameDisplay.blit(Textplace,TextRect)
    
    

    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                if event.key == pygame.K_RIGHT:
                    x_change = 15
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
        gameDisplay.blit(board,(0,0))
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
 
        if x > display_width - car_width or x < 0:
            crash()
 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
 
        if y < thing_starty+thing_height:
            print('y crossover')
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
instructions()
pygame.quit()
quit()