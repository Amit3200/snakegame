#Snake Game

import pygame
import sys
import random
import time

check_errors= pygame.init()
#second element of tuple shows error 
if check_errors[1] > 0 :
    print("(!) There are number of errors")
    sys.exit(-1)
else:
    print("PyGame sccessfully initialized")

speed=5
#Play Surface Display
playSurface=pygame.display.set_mode((720,480))
pygame.display.set_caption('Snake Game')
#Colors

red = pygame.Color(255,0,0)  #Game Over
green = pygame.Color(0,255,0) # Snake
blue = pygame.Color(0,0,255) 
black = pygame.Color(0,0,0) # Score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food

#FPS FRAME PER SECOND CONTROLLER
fpsConroller = pygame.time.Clock()

#Important variables
snakePos = [100,50] #position of snake we will move right
snakeBody=[[100,50],[90,50],[80,50]] #x axis will move to right snake is of 3 size initially these are blocks

foodPos = [random.randrange(1,72)*10,random.randrange(1,48)*10] #foodposition if you gave 720 then you will pass the food but by multiplying the 10 it will generate numbers which can be divisible by 10 
foodSpawn=True #Food Generated or not

direction = 'RIGHT' #moving
changeto = direction  #to change to the next direction

score=0
#Game  Over Function

def gameOver():
    myFont = pygame.font.SysFont("Century Gothic",72)
    GOsurf = myFont.render('Game Over!',True , red) #sends the message to the surface 
    GOrect = GOsurf.get_rect()#placing message on surface
    GOrect.midtop= (360,15) #Position miidle is obtained by 720/2=360
    playSurface.blit(GOsurf,GOrect) #Placing the components on the screen
    showScore(0)
    pygame.display.flip() # update the screen so that FPS does not affect the screen
    time.sleep(4) 
    pygame.quit() #ends the pygame
    sys.exit() # ends the system console


def showScore(choice=1):
    sFont = pygame.font.SysFont("Century Gothic",24)
    Ssurf = sFont.render('Score : '+str(score),True , black) #sends the message of score to the surface
    Srect =  Ssurf.get_rect()
    if choice==1:
        Srect.midtop = (80,10)
    else:
        Srect.midtop = (360,120)
    playSurface.blit(Ssurf,Srect)


#Events required Main Logic is defined here
while True:
    # imports the key functionality
    for event in pygame.event.get():
        #if the user quits
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:#checking the keys if it is right
                changeto='RIGHT'
            if event.key == pygame.K_LEFT:#checking the keys if it is left
                changeto='LEFT'
            if event.key == pygame.K_UP:#checking the keys if it is up
                changeto='UP'
            if event.key == pygame.K_DOWN:#checking the keys if it is down
                changeto='DOWN' 
            if event.key == pygame.K_ESCAPE:#checking the key if it is for quit
                pygame.event.post(pygame.post.Event(pygame.QUIT)) #posting the quiting the event

    # validation of direction i.e all the bugs are to be removed
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    
    if direction == 'RIGHT':
        #Move Right by changing the x coordinate let
        snakePos[0]+=10
    if direction=='LEFT':
        snakePos[0] -=10
        #Move Up Down By Changing Y coordinate
    if direction =='UP':
        snakePos[1]-=10
    if direction =='DOWN':
        snakePos[1]+=10
    
    #Updating a body whenever when it eats so append a list it is simple
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1]==foodPos[1]:
        score=score+10
        speed+=5
        foodSpawn = False
    else:
        snakeBody.pop()
    
    #Food Spawn Mechanism
    
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,48)*10] #foodposition new
    foodSpawn = True

    #Graphics Part
    playSurface.fill(white) # Changes background to white
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green, # draws a rectangle
        pygame.Rect(pos[0],pos[1],10,10)) #passing the list component
    
    
    pygame.draw.rect(playSurface,brown, # draws a rectangle
        pygame.Rect(foodPos[0],foodPos[1],10,10)) #passing the list component
    
    # Checking the game if you hit wall and then hitting the Game Over
    if snakePos[0]>710 or snakePos[0]<0:
            gameOver()
    if snakePos[1]>470 or snakePos[1]<0:
            gameOver()
    # Checking if the snake hits itself then it should say game Over
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1]== block[1]:
            gameOver()
    
    
    showScore()
    pygame.display.flip() # to make update or commit change
    fpsConroller.tick(speed) #frame per seconds
 































