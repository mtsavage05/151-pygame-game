# simple game starter
#    

import pygame, sys
from pygame.locals import QUIT
from pygame import Rect
from typing import Tuple
from pygame import Vector2
from random import randint 

# GLOBAL GAME CONSTANTS
FPS = 30 #desired frame-rate
SCREEN_W = 800 #screen width
SCREEN_H = 600 # screen height
scale = 3
# asset directories 
BG_HOME = './assets/background/'
PPL_HOME = './assets/people/'
MUSIC_HOME = './assets/music/'
# assigning verables
cur_y = 0
winner = []



## INITIALIZATION FUNCTIONS
def init_images() -> Tuple[pygame.SurfaceType,pygame.SurfaceType]:
    """
    Load and initialize image assets to get pygame surface objects for each

    Parameters: 
        None 
    
    Return
       Surface : the character sheet
       Surface : the background 
    """
    # player sheet
    SHEET = pygame.image.load(PPL_HOME + '_02.png')
    SHEET2 = pygame.image.load(PPL_HOME + '_01.png')
    #print(SHEET.get_width(),SHEET.get_height())
    SHEET = pygame.transform.scale(SHEET,(scale * 64,scale * 51))
    SHEET2 = pygame.transform.scale(SHEET2,(scale * 64,scale * 51))
    SHEET = SHEET.convert_alpha()
    SHEET2 = SHEET2.convert_alpha()
    
    # background 
    BG_0 = pygame.image.load(BG_HOME + 'parallax-forest-back-trees.png')
    #print(BG_0.get_width(), BG_0.get_height())
    BG_0 = pygame.transform.scale(BG_0, (SCREEN_W, SCREEN_H))
    BG_0 = BG_0.convert_alpha()
    
    # second background
    light_image = pygame.image.load(BG_HOME + 'parallax-forest-lights.png')
    light_image = pygame.transform.scale(light_image, (SCREEN_W,SCREEN_H))
    light_image = light_image.convert_alpha()

    # second tree image
    second_tree_image = pygame.image.load(BG_HOME + 'parallax-forest-front-trees.png')
    second_tree_image = pygame.transform.scale(second_tree_image,(SCREEN_W,SCREEN_H))
    second_tree_image = second_tree_image.convert_alpha()
    return SHEET, BG_0, light_image, second_tree_image,SHEET2
#
## TICK FUNCTIONS
def tick_fps(gameClock : pygame.time.Clock) -> int:
    """
    Get the current frames per second as an integer

    Parameters:
       gameClock : Clock  a pygame clock for the game
    
    Return:
       int : current fps as an int
    """
    return int(gameClock.get_fps())
#
def player_movment(pc_aniRect: Rect) -> None:
    """
    Move player legs

    Perameters:
        pc_aniRect : Rect - what anamation the charictor is in.
    
    return:
        None
    """

    pc_aniRect.y = (pc_aniRect.y + pc_aniRect.height) % (pc_aniRect.height*3)
    
    return pc_aniRect
#
def background_movement(cur_x: int) -> int:
    """
    Given a cur_x, change the value for the background to move.

    Perameters:
        cur_x : int - the x value currently assigned for the background

    return:
        new_x : int - the updated x value
    """
    
    new_x = (cur_x - 10) % 800
    return new_x
#
def forest_background_movment(cur_x_second: int):
    """
      Given a cur_x, change the value for the background to move.

    Perameters:
        cur_x : int - the x value currently assigned for the background

    return:
        new_x : int - the updated x value
    """
    new_cur_x_second = (cur_x_second - 5) % 800
    return new_cur_x_second
## DRAW FUNCTIONS
def draw_fps(screen : pygame.SurfaceType, currfps : int  ) -> None:
    """
    Render the current fps to the screen

    Parameters:
        screen : Surface - game screen where all images are drawn
        currfps : int - current fps as int
    
    Return:
        None
    """
    FONT = pygame.font.SysFont('Helvetica', 24)
    FONT_CLR = (100,150,100)
    txt = FONT.render(str(currfps), 1, FONT_CLR)
    screen.blit(txt,(0,0))

    
    return
#
def onDraw(screen : pygame.SurfaceType, bg : pygame.SurfaceType, csheet : pygame.SurfaceType, 
           currfps : int, cx : int, cy : int, pc_aniRect : Rect, cur_x : int,tree_x : int, light_image : int, second_tree_image : pygame.SurfaceType, pc_locRect : Rect, pc_aniRect2 : Rect, pc_locRect2 :Rect,SHEET2 : pygame.SurfaceType) -> None:
    """
    Render the current animation frame/scene 

    Parameters: 
        screen : Surface - the surface for the game screen
        bg : Surface - the background image surface 
        csheet : Surface - the character sheet image surface
        currfps : int - the current frames per second     
        cx : int - character sheet x coord 
        cy : int - character sheet y coord 
        cur_y : int - current y position
        cur_x : int - current x position
        tree_x : int - current x position for tree background
        light_image : Surface - moving lights
        second_tree_image : Surface - moving trees
        pc_locRect : Rect - location of charictor
        pc_locRect2 : Rect - location of the second charictor
        pc_aniRect : Rect - anamation 
        pc_aniRect2 : Rect - anamation of second charictor
        SHEET2  : pygame.SurfaceType - the character sheet image surface


    return:
        None
    """
    # background
    screen.blit(bg, (0,0))
    # player character sheet
    #screen.blit(csheet,(cx,cy))
    #cur_y = player_movment(cur_y)
    
    screen.blit(csheet,pc_locRect,pc_aniRect)
    screen.blit(SHEET2,pc_locRect2,pc_aniRect2)
    draw_fps(screen,currfps)
    
    #second back ground (moving)
    screen.blit(light_image,(cur_x,0),(0,0,SCREEN_W - cur_x,SCREEN_H))
    screen.blit(light_image,(0,0),(SCREEN_W-cur_x,0,cur_x,SCREEN_H))
    
    #second tree image
    #screen.blit(second_tree_image,(0,0))
    
    screen.blit(second_tree_image,(tree_x,0),(0,0,SCREEN_W - tree_x,SCREEN_H))
    screen.blit(second_tree_image,(0,0),(SCREEN_W-tree_x,0,tree_x,SCREEN_H))

    Font2 = pygame.font.SysFont("Helvetica", 30)
    font_clr2 = (255,0,0)
    txt2 = Font2.render(str("Space to continue!"), 1, font_clr2)
    screen.blit(txt2,(300,550))

    pygame.display.update() #always do last! 
    return
#
def onDrawGO(screen : pygame.SurfaceType, bg : pygame.SurfaceType, csheet : pygame.SurfaceType, 
           currfps : int, cx : int, cy : int, pc_aniRect : Rect, cur_x : int,tree_x : int, light_image : int, second_tree_image : pygame.SurfaceType, pc_locRect : Rect, pc_aniRect2 : Rect, pc_locRect2 : Rect,SHEET2 : pygame.SurfaceType) -> None:
    """
    Render the current animation frame/scene 

    Parameters: 
        screen : Surface - the surface for the game screen
        bg : Surface - the background image surface 
        csheet : Surface - the character sheet image surface
        currfps : int - the current frames per second     
        cx : int - character sheet x coord 
        cy : int - character sheet y coord 
        cur_y : int - current y position
        cur_x : int - current x position
        tree_x : int - current x position for tree background
        light_image : Surface - moving lights
        second_tree_image : Surface - moving trees
        pc_locRect : Rect - location of charictor
        pc_locRect2 : Rect - location of the second charictor
        pc_aniRect : Rect - anamation 
        pc_aniRect2 : Rect - anamation of second charictor
        SHEET2  : pygame.SurfaceType - the character sheet image surface

    return:
        None
    """
    # background
    #screen.blit(bg, (0,0))
    # player character sheet
    #screen.blit(csheet,(cx,cy))
    #cur_y = player_movment(cur_y)
    
    screen.blit(csheet,pc_locRect,pc_aniRect)
    screen.blit(SHEET2,pc_locRect2,pc_aniRect2)
    draw_fps(screen,currfps)
    
    #second back ground (moving)
    #screen.blit(light_image,(cur_x,0),(0,0,SCREEN_W - cur_x,SCREEN_H))
    #screen.blit(light_image,(0,0),(SCREEN_W-cur_x,0,cur_x,SCREEN_H))
    
    #second tree image
    #screen.blit(second_tree_image,(0,0))
    
    #screen.blit(second_tree_image,(tree_x,0),(0,0,SCREEN_W - tree_x,SCREEN_H))
    #screen.blit(second_tree_image,(0,0),(SCREEN_W-tree_x,0,tree_x,SCREEN_H))

    Font2 = pygame.font.SysFont("Helvetica", 30)
    font_clr2 = (255,0,0)
    if winner == ["Player 1"]:
        txt2 = Font2.render(str("Game Over. Player 2 Won!"), 1, font_clr2)
    elif winner == ["Player 2"]:
        txt2 = Font2.render(str("Game Over. Player 1 Won!"), 1, font_clr2)
    else:
        txt2 = Font2.render(str("Game Over. Tie Game!"), 1, font_clr2)
    screen.blit(txt2,(250,250))

    pygame.display.update() #always do last! 
    return
#
def pause_game(pgevent : pygame.event,pause : bool) -> bool:
    """
    Determan if the game should be paused.

    Peramaters:
        pgevent : pygame.event - what event happened
        pause : bool - toggle game to next screen

    Return:
        pause : bool - new toggle
    """

    eventType = pgevent.type
    key = pgevent.key
    if eventType == pygame.KEYDOWN:
        if key == pygame.K_SPACE:
            pause = False
    return pause
#
def movment_onDraw(screen : pygame.surface,bg : pygame.surface,csheet : pygame.surface,curr_fps : int,sheet_x : int,sheet_y : int,pc_aniRect1 : Rect,light_image : pygame.surface,second_tree_image : pygame.surface,pc_locRect1 : Rect,pc_aniRect2 : Rect,pc_locRect2 : Rect,SHEET2 : pygame.Surface,plat1 : Rect,plat2 : Rect,lobull1 : list[Vector2],lobull2 : list[Vector2],platnum : int)-> None:
    """
    Render the current animation frame/scene 
    Also draws everything.

    Parameters: 
        screen : Surface - the surface for the game screen
        bg : Surface - the background image surface 
        csheet : Surface - the character sheet image surface
        currfps : int - the current frames per second     
        cx : int - character sheet x coord 
        cy : int - character sheet y coord 
        cur_y : int - current y position
        cur_x : int - current x position
        tree_x : int - current x position for tree background
        light_image : Surface - moving lights
        second_tree_image : Surface - moving trees
        pc_locRect1 : Rect - location of charictor
        pc_locRect2 : Rect - anamation
        pc_aniRect1 : Rect - location of charictor
        pc_aniRect2 : Rect - anamation
        SHEET2 : pygame.Surface - the character sheet image surface
        plat1 : Rect - first platform
        plat2 : Rect - second platform
        lobull1 : list[Vector2] - list of bullets
        lobull2 : list[Vector2] - list of bullets
        platnum : int - random number to decide what platforms are in play

    return:
        None
    """

    screen.blit(bg, (0,0))
    screen.blit(light_image,(0,0))
    screen.blit(second_tree_image,(0,0))
    if pc_locRect1.x > SCREEN_W + pc_locRect1.width:
        pc_locRect1.x = -pc_locRect1.width
    elif pc_locRect1.x < -pc_locRect1.width:
        pc_locRect1.x = SCREEN_W + pc_locRect1.width
    if platnum == 1:
        pygame.draw.rect(screen,(255,0,0,255),plat1)
    elif platnum == 2:
        pygame.draw.rect(screen,(0,255,0,255),plat2)
    else:
        pygame.draw.rect(screen,(255,0,0,255),plat1)
        pygame.draw.rect(screen,(0,255,0,255),plat2)
    screen.blit(csheet,pc_locRect1,pc_aniRect1)

    if pc_locRect2.x > SCREEN_W + pc_locRect2.width:
        pc_locRect2.x = -pc_locRect2.width
    elif pc_locRect2.x < -pc_locRect2.width:
        pc_locRect2.x = SCREEN_W + pc_locRect2.width

    screen.blit(SHEET2,pc_locRect2,pc_aniRect2)
    draw_fps(screen,curr_fps)
    
    for i in range(len(lobull1)):
        pygame.draw.circle(screen,(0,255,0,255),(lobull1[i].x,lobull1[i].y),10)

    for z in range(len(lobull2)):
        pygame.draw.circle(screen,(0,255,0,255),(lobull2[z].x,lobull2[z].y),10)

    pygame.display.update()

    return
#
def onKey(pgevent : pygame.event, ddx : int,VO : float,ddy : float,ACC : int,pc_locRect1 : Rect,pc_locRect2 : Rect,lobull1 : list[Vector2],lobull1V : list[int],bullnum : int)-> tuple:
    """
    What keys are pressed and what they change.

    peramaters:
        pgevent : pygame.event -  what event happens
        dx : int - velocity of x
        ddy : float - acceration of y
        Vo  : float - inital velocity for x
        pc_locRect1 : Rect - location of charictor
        pc_locRect2 : Rect - location of charictor
        lobull1 : list[Vector2] - list of bullet locations
        lobull1V : list[int] - list of velocitys
        bullnum : int - counter of bullets

    return:
        dx : float - velocity of x
        ddy : float - acceration of y
    """
    
    eventType = pgevent.type #KEYDOWN or KEYUP
    key = pgevent.key # The key that's down/up

    
    

    
    if eventType == pygame.KEYDOWN:
        if key == pygame.K_d:
            ddx = ACC
        if key == pygame.K_a:
            ddx = -ACC
        if key == pygame.K_w:
            ddy = -(VO)
        if key == pygame.K_s:
            if bullnum < 3:
                bullnum += 1
                
                lobull1.append(Vector2(pc_locRect1.centerx,pc_locRect1.centery))
                if pc_locRect1.x >= pc_locRect2.x:
                    lobull1V.append(-30)
                else:
                    lobull1V.append(30)
               
        
        

    elif pgevent.type == pygame.KEYUP:
        if key == pygame.K_d:
            ddx = 0
        if key == pygame.K_a:
            ddx = 0
        if key == pygame.K_w:
            ddy = 0
    
    return ddx,ddy,bullnum
#
def onKey2(pgevent : pygame.event, ddx : int,VO : float,ddy : float,ACC : int,pc_locRect1 : Rect,pc_locRect2 : Rect,lobull2 : list[Vector2],lobull2V  : list[Vector2],bullnum : int)-> tuple:
    """
    What keys are pressed and what they change.

    peramaters:
        pgevent : pygame.event -  what event happens
        dx : int - velocity of x
        ddy : float - acceration of y
        Vo  : float - inital velocity for x
        pc_locRect1 : Rect - location of charictor
        pc_locRect2 : Rect - location of charictor
        lobull2 : list[Vector2] - list of bullet locations
        lobull2V : list[int] - list of velocitys
        bullnum : int - counter of bullets

    return:
        dx : float - velocity of x
        ddy : float - acceration of y
    """

    eventType = pgevent.type #KEYDOWN or KEYUP
    key = pgevent.key # The key that's down/up

    
    
    if eventType == pygame.KEYDOWN:
        if key == pygame.K_RIGHT:
            ddx = ACC
        elif key == pygame.K_LEFT:
            ddx = -ACC
        elif key == pygame.K_UP:
            ddy = -(VO)
        if key == pygame.K_DOWN:
            if bullnum < 3:
                
                bullnum += 1
                lobull2.append(Vector2(pc_locRect2.centerx,pc_locRect2.centery))
                if pc_locRect2.x >= pc_locRect1.x:
                    lobull2V.append(-30)
                else:
                    lobull2V.append(30)
               
        

    elif pgevent.type == pygame.KEYUP:
        if key == pygame.K_RIGHT:
            ddx = 0
        elif key == pygame.K_LEFT:
            ddx = 0
        elif key == pygame.K_UP:
            ddy = 0
    
    return ddx,ddy,bullnum
#
def movement_onTick1(ddx : int,dx : int,pc_locRect1 : Rect,pc_locRect2 : Rect,dy : int,ddy : float,G : float,FLOOR : float,VO : float,dt : int,F : int,lobull1 : list[Vector2],lobull1V : list[int],bull1Count : int,winner : list[str])-> tuple:
    """
    Update over time

    perametars:
        ddx : int - acceleration in the x direction.
        dx : int - velocity of x
        pc_locRect : Rect - possition rectangle
        dy : int - velocity of y
        ddy : float - acceleration of y
        G : float - gravity
        FLOOR : float - floor of person
        VO : float - velocity when leaving the ground
        dt : int - time that passed.
        F : int - friction
        lobull1 : list[Vector2] - list of bullet locations
        lobull1V : list[int] - list of bullet velocities
        bull1Count : int - count bullets
        winner : list[str] - list for winner of the game


    return:
        None
    """
    if pc_locRect1.y < FLOOR:
        ddy = 0
        ddx = 0
        F = 0
    else:
        dx = (dx + ddx)*F 
    if -1 < dx < 1:
        dx = 0
    

    dy = (dy + (ddy + G))

    
    
    pc_locRect1.y = pc_locRect1.y + (dy + ddy/2)
    pc_locRect1.x = pc_locRect1.x + (dx + ddx/2)
    if pc_locRect1.y >= FLOOR:
        dy = 0
        pc_locRect1.y = FLOOR
    
    for i in range(len(lobull1)):
        lobull1[i].x += lobull1V[i]
        if lobull1[i].x > SCREEN_W or lobull1[i].x < 0:
           
            bull1Count += 1
            lobull1[i] = Vector2(SCREEN_W/2,SCREEN_H + 20)
            lobull1V[i] = 0
            
    for z in lobull1:

        if pygame.Rect.collidepoint(pc_locRect2,(z.x,z.y)):
            winner.append("Player 2")


    return dx,dy,bull1Count
#
def movement_onTick2(ddx : int,dx : int,pc_locRect1 : Rect,pc_locRect2 : Rect,dy : int,ddy : float,G : float,FLOOR : float,VO : float,dt : int,F : int,lobull1 : list[Vector2],lobull1V : list[int],bull1Count : int,winner : list[str])-> tuple:
    """
    Update over time

    perametars:
        ddx : int - acceleration in the x direction.
        dx : int - velocity of x
        pc_locRect : Rect - possition rectangle
        dy : int - velocity of y
        ddy : float - acceleration of y
        G : float - gravity
        FLOOR : float - floor of person
        VO : float - velocity when leaving the ground
        dt : int - time that passed.
        F : int - friction
        lobull1 : list[Vector2] - list of bullet locations
        lobull1V : list[int] - list of bullet velocities
        bull1Count : int - count bullets
        winner : list[str] - list for winner of the game


    return:
        None
    """
    if pc_locRect2.y < FLOOR:
        ddy = 0
        ddx = 0
        F = 0
    else:
        dx = (dx + ddx)*F 
    if -1 < dx < 1:
        dx = 0
    

    dy = (dy + (ddy + G))

    
    
    pc_locRect2.y = pc_locRect2.y + (dy + ddy/2)
    pc_locRect2.x = pc_locRect2.x + (dx + ddx/2)
    if pc_locRect2.y >= FLOOR:
        dy = 0
        pc_locRect2.y = FLOOR
    
    for i in range(len(lobull1)):
        lobull1[i].x += lobull1V[i]
        if lobull1[i].x > SCREEN_W or lobull1[i].x < 0:
            bull1Count += 1
            lobull1[i] = Vector2(SCREEN_W/2,SCREEN_H + 20)
            lobull1V[i] = -0
            



            
    for z in lobull1:
        if pygame.Rect.collidepoint(pc_locRect1,(z.x,z.y)):
            winner.append("Player 1")
        


    return dx,dy,bull1Count
#
def pc_ani_with_movment(ddx : int,pc_aniRect1 : Rect,sheet : pygame.SurfaceType):
    """
    Move player legs with direction

    Perameters:
        ddx : int - acceleration in x
        pc_aniRect : Rect - what anamation the charictor is in.
        sheet : pygame.SurfaceType - charictior sheet

    return:
        None
    """

    if ddx < 0:
        pc_aniRect1.x = sheet.get_width()-sheet.get_width()//4
        pc_aniRect1.y = (pc_aniRect1.y + pc_aniRect1.height) % (pc_aniRect1.height*3)
    elif ddx > 0:
        pc_aniRect1.x = sheet.get_width()//4
        pc_aniRect1.y = (pc_aniRect1.y + pc_aniRect1.height) % (pc_aniRect1.height*3)
    else:
        pc_aniRect1.x = 0
        pc_aniRect1.y = 0

    return
#
def colision_detect(loPlats : list[Rect],pc_locRect1 : Rect,pc_locRect2 : Rect,FLOOR1 : int,FLOOR2 : int,dy1 : int,dy2 : int,BG_0 : pygame.surface,platnum : int) -> tuple:
    """
    See if the charictors are tuching the platforms

    Pramaters:
        loPlats : list[Rects] - platforms in a list
        pc_locRect1 : Rect - player location
        pc_locRect2 : Rect - player location
        FLOOR1 : int - floor for player
        FLOOR2 : int - floor for player
        dy1 : int - velocity in the y direction
        dy2 : int - velocity in the y direction
        BG_0 : pygame.surface - to get hight for surface
        platnum - random number for what platforms are in play

        return:
            int,int - both for floors
    """
    for i in range(len(loPlats)):
        
            if dy1 >= 0:
                if platnum == 1:
                    if pygame.Rect.colliderect(loPlats[i],pc_locRect1) and i == 0:
                        FLOOR1 = loPlats[i].top - 50
                elif platnum == 2:
                    if pygame.Rect.colliderect(loPlats[i],pc_locRect1) and i == 1:
                        FLOOR1 = loPlats[i].top - 50
                else:
                    if pygame.Rect.colliderect(loPlats[i],pc_locRect1):
                        FLOOR1 = loPlats[i].top - 50
                #else:
                    #if i == len(loPlats):
                        #FLOOR1 = int(BG_0.get_height() * .78)
       
            if dy2 >= 0:
                if platnum == 1:
                    if pygame.Rect.colliderect(loPlats[i],pc_locRect2) and i == 0:
                        FLOOR2 = loPlats[i].top - 50
                elif platnum == 2:
                    if pygame.Rect.colliderect(loPlats[i],pc_locRect2) and i == 1:
                        FLOOR2 = loPlats[i].top - 50
                else:
                    if pygame.Rect.colliderect(loPlats[i],pc_locRect2):
                        FLOOR2 = loPlats[i].top - 50
    if not pygame.Rect.colliderect(loPlats[0],pc_locRect1) and not pygame.Rect.colliderect(loPlats[1],pc_locRect1):
        FLOOR1 = int(BG_0.get_height() * .78)
    if not pygame.Rect.colliderect(loPlats[0],pc_locRect2) and not pygame.Rect.colliderect(loPlats[1],pc_locRect2):
        FLOOR2 = int(BG_0.get_height() * .78)
    
    



    #print(dy1,dy2,FLOOR1,FLOOR2)
    return FLOOR1,FLOOR2

def start_main() -> None:
    # initilize pygame
    pygame.init()    
    # set main surface 
    displaysurf = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    # set window caption
    pygame.display.set_caption("My First Game")
    # get Clock for fixed framerate animation
    fpsClock = pygame.time.Clock()

    # get the image surfaces 
    SHEET,BG_0,light_image,second_tree_image,SHEET2 = init_images()   
    
    # prepare music 
    pygame.mixer.music.load(MUSIC_HOME + 'Amber Forest.mp3')
    #start music
    pygame.mixer.music.play(-1)
    
    # initialize game variables (function?!)
    sheet_x = SCREEN_W / 2  #x coordinate for player
    sheet_y = SCREEN_H / 2  #y coordinate for player 
    curr_fps = 0   # current fps 
    cur_x = 0
    tree_x = 0
    pc_aniRect = Rect(SHEET.get_width()//4,0,
                      SHEET.get_width()//4,SHEET.get_height()//3)
    pc_locRect = Rect(BG_0.get_width()//2-SHEET.get_width()//1,
                      int(BG_0.get_height()*.76),
                      SHEET.get_width()//4,SHEET.get_height()//3)  
    pc_aniRect2 = Rect(SHEET.get_width()//4,0,
                      SHEET.get_width()//4,SHEET.get_height()//3)
    pc_locRect2 = Rect(BG_0.get_width()//2-SHEET.get_width() + 300,
                      int(BG_0.get_height()*.76),
                      SHEET.get_width()//4,SHEET.get_height()//3)  
    play = True
    # GAME LOOP GO!
    while play:
        # close game when x in window is hit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                play = pause_game(event,play)

        # Tick goes the clock - UPDATE GAME VARIABLES 
        curr_fps = tick_fps(fpsClock)
        # player movment
        cur_x = background_movement(cur_x)
        pc_aniRect = player_movment(pc_aniRect)
        pc_aniRect2 = player_movment(pc_aniRect2)
        tree_x = forest_background_movment(tree_x)
        # DRAW THE SCENE BASED ON CONSTANTS AND VARIABLES 
        onDraw(displaysurf,BG_0,SHEET,curr_fps,sheet_x,sheet_y,pc_aniRect,cur_x,tree_x,light_image,second_tree_image,pc_locRect,pc_aniRect2,pc_locRect2,SHEET2)        
    
        # fix clock to FPS to end the loop
        fpsClock.tick(FPS)
        # END GAME LOOP

def movement_main():
     # initilize pygame
    pygame.init()    
    # set main surface 
    displaysurf = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    # set window caption
    pygame.display.set_caption("PVP")
    # get Clock for fixed framerate animation
    fpsClock = pygame.time.Clock()

    # get the image surfaces 
    # get the image surfaces 
    SHEET,BG_0,light_image,second_tree_image,SHEET2 = init_images()   
    

    #set verabales
    sheet_x = SCREEN_W / 2  #x coordinate for player
    sheet_y = SCREEN_H / 2  #y coordinate for player 
    curr_fps = 0   # current fps
    
    pc_aniRect1 = Rect(0,0,
                      SHEET.get_width()//4,SHEET.get_height()//3)
    pc_locRect1 = Rect(BG_0.get_width()//2-SHEET.get_width()//1,
                      int(BG_0.get_height()*.78),
                      SHEET.get_width()//4,SHEET.get_height()//3)
    pc_aniRect2 = Rect(0,0,
                      SHEET.get_width()//4,SHEET.get_height()//3)
    pc_locRect2 = Rect(BG_0.get_width()//2-SHEET.get_width() + 300,
                      int(BG_0.get_height()*.78),
                      SHEET.get_width()//4,SHEET.get_height()//3)

    dx = 0
    dx2 = 0
    ACC = 5
    H = 100
    XH = 100
    dy = 0
    dy2 = 0
    ddx = 0
    ddx2 = 0

    ddy = 0
    ddy2 = 0
    VX = 20

    #F = VX / (VX + ACC)
    F = VX / (VX + ACC)
    F2 = F
    #G = (2 * H * (VX**2)) / (XH**2)
    G = (2 * H * (VX**2)) / (XH**2)
    #VO = (2 * H * VX) /XH
    VO = (2 * H * VX) / XH
    FLOOR1 = int(BG_0.get_height() * .78)
    FLOOR2 = int(BG_0.get_height() * .78)
    plat1 = Rect(SCREEN_W/1.65,SCREEN_H/1.35,200,20)
    plat2 = Rect(SCREEN_W/10,SCREEN_H/1.35,200,20)
    loPlats = [plat1,plat2]
    dt = 0
    et = 0
    lobull1 = []
    lobull1V = []
    bull1Count = 0

    lobull2 = []
    lobull2V = []
    bull2Count = 0

    bullnum1 = 0
    bullnum2 = 0

    gamestate = True

    platnum = randint(1,3)
    
    while gamestate == True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                ddx,ddy,bullnum1 = onKey(event,ddx,VO,ddy,ACC,pc_locRect1,pc_locRect2,lobull1,lobull1V,bullnum1)
                ddx2,ddy2,bullnum2 = onKey2(event,ddx2,VO,ddy2,ACC,pc_locRect1,pc_locRect2,lobull2,lobull2V,bullnum2)
        
        curr_fps = tick_fps(fpsClock)
        dt = fpsClock.tick(FPS)
        et += dt
        FLOOR1,FLOOR2 = colision_detect(loPlats,pc_locRect1,pc_locRect2,FLOOR1,FLOOR2,dy,dy2,BG_0,platnum)
        dx,dy,bull1Count = movement_onTick1(ddx,dx,pc_locRect1,pc_locRect2,dy,ddy,G,FLOOR1,VO,dt,F,lobull1,lobull1V,bull1Count,winner)
        dx2,dy2,bull2Count = movement_onTick2(ddx2,dx2,pc_locRect1,pc_locRect2,dy2,ddy2,G,FLOOR2,VO,dt,F2,lobull2,lobull2V,bull2Count,winner)
        
        pc_ani_with_movment(ddx,pc_aniRect1,SHEET)
        pc_ani_with_movment(ddx2,pc_aniRect2,SHEET2)
        movment_onDraw(displaysurf,BG_0,SHEET,curr_fps,sheet_x,sheet_y,pc_aniRect1,light_image,second_tree_image,pc_locRect1,pc_aniRect2,pc_locRect2,SHEET2,plat1,plat2,lobull1,lobull2,platnum)
        
        if bull1Count == 3 and bull2Count == 3:
            winner.append("Tie")
        if winner != []:
            gamestate = False
        
def game_over():
    # initilize pygame
    pygame.init()    
    # set main surface 
    displaysurf = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    # set window caption
    pygame.display.set_caption("Game Over!")
    # get Clock for fixed framerate animation
    fpsClock = pygame.time.Clock()

    # get the image surfaces 
    SHEET,BG_0,light_image,second_tree_image,SHEET2 = init_images()   
    
    # prepare music 
    #pygame.mixer.music.load(MUSIC_HOME + 'Amber Forest.mp3')
    #start music
    #pygame.mixer.music.play(-1)
    
    # initialize game variables (function?!)
    sheet_x = SCREEN_W / 2  #x coordinate for player
    sheet_y = SCREEN_H / 2  #y coordinate for player 
    curr_fps = 0   # current fps 
    cur_x = 0
    tree_x = 0
    pc_aniRect = Rect(SHEET.get_width()//4,0,
                      SHEET.get_width()//4,SHEET.get_height()//3)
    pc_locRect = Rect(BG_0.get_width()//2-SHEET.get_width()//1,
                      int(BG_0.get_height()*.76),
                      SHEET.get_width()//4,SHEET.get_height()//3)  
    pc_aniRect2 = Rect(SHEET.get_width()//4,0,
                      SHEET.get_width()//4,SHEET.get_height()//3)
    pc_locRect2 = Rect(BG_0.get_width()//2-SHEET.get_width() + 300,
                      int(BG_0.get_height()*.76),
                      SHEET.get_width()//4,SHEET.get_height()//3)  
    play = True
    # GAME LOOP GO!
    while play:
        # close game when x in window is hit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                play = pause_game(event,play)

        # Tick goes the clock - UPDATE GAME VARIABLES 
        curr_fps = tick_fps(fpsClock)
        # player movment
        cur_x = background_movement(cur_x)
        pc_aniRect = player_movment(pc_aniRect)
        pc_aniRect2 = player_movment(pc_aniRect2)
        tree_x = forest_background_movment(tree_x)
        # DRAW THE SCENE BASED ON CONSTANTS AND VARIABLES 
        onDrawGO(displaysurf,BG_0,SHEET,curr_fps,sheet_x,sheet_y,pc_aniRect,cur_x,tree_x,light_image,second_tree_image,pc_locRect,pc_aniRect2,pc_locRect2,SHEET2)        
    
        # fix clock to FPS to end the loop
        fpsClock.tick(FPS)
        # END GAME LOOP
        
    
def main():
    start_main()
    movement_main()
    game_over()

if __name__ == '__main__':
    main()
