import pygame
from pygame.locals import *
import random
from pygame import mixer

mixer.init()
pygame.init()

#time
clock = pygame.time.Clock()
fps = 60
#load music
def bg_music():
    pygame.mixer.music.load('crpl\\musicpac.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1,0.0)
    
def bg_music_stop():
    pygame.mixer.music.load('crpl\\musicpac.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.stop()


bg_music()
jump_fx=pygame.mixer.Sound('crpl\\jump69.mp3')
jump_fx.set_volume(0.9)
death_fx=pygame.mixer.Sound('crpl\\exp.wav')

death_fx.set_volume(0.9)



#dimensions of screen
screen_width = 864
screen_height = 936
#creating display
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('crpl\\Flappy Bird')

#define font
font = pygame.font.SysFont('crpl\\Bauhaus 93', 60 )

#define colours
white = (0 , 0, 0)

#define game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 200
pipe_frequency = 1500 #milisecond
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False 
#load images
bg = pygame.image.load('crpl\\sky.png')
ground_img = pygame.image.load('crpl\\r2.png')
button_img = pygame.image.load('crpl\\restart.png')

#converting text into img on screen
def draw_text( text, font, text_col , x , y):
    img = font.render(text,True,text_col)
    screen.blit(img , (x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int (screen_height / 2)
    score = 0
    bg_music()
    return score    



#classes
class Bird(pygame.sprite.Sprite): 
    def __init__(self, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.images = []
       self.index = 0
       self.counter = 0
       for num in range(1,4):
           img = pygame.image.load(f'crpl\\b{num}.png')
           self.images.append(img)
       self.image = self.images[self.index]
       self.rect = self.image.get_rect()
       self.rect.center = [x,y]
       self.vel = 0
       self.clicked = False

    def update(self): 
        if flying == True:
            #gravity 

            self.vel += 0.5
            if self.vel > 8 :
                self.vel = 8

            if self.rect.bottom <768:
                self.rect.y += int(self.vel)

        if game_over == False :
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
                jump_fx.play()

            if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False
                

            #handle the animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown :
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            #rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index],self.vel * -2 )
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90 )

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x , y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('crpl\\t3.png')
        self.rect = self.image.get_rect()
        #position 1 is from top , -1 is from bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False , True)
            self.rect.bottomleft = [x,y-int(pipe_gap/2)]
        if position == -1:    
            self.rect.topleft = [x, y+ int(pipe_gap/2)]
    def update(self):
        self.rect.x -= scroll_speed 
        if self.rect.right < 0 :
            self.kill()


class Button():
    def __init__(self , x ,y ,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse is over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action = True       

        #draw button
        screen.blit(self.image, (self.rect.x,self.rect.y))

        return action



bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)


 #create restart button instance
button = Button(screen_width//2 -50, screen_height//2 - 100,button_img)       

run = True
#main loop
while run:
    death_check = 0

    clock.tick(fps)

    #draw background
    screen.blit(bg, (0,0)) 
    

    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    

    #draw the ground
    screen.blit(ground_img, (ground_scroll , 768))

    #check the score
    if len(pipe_group) > 0 :
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
            and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True :
             if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                 score += 1
                 pass_pipe = False
                      

    draw_text(str(score),font,white,int(screen_width/2),20)
    #look for collision
    if game_over == False and pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or flappy.rect.top < 0:
        game_over = True
        death_fx.play()
        
        
        


    #check if bird has hit ground
    if flappy.rect.bottom >= 768 and game_over == False:
        game_over = True
        flying = False
        death_fx.play()
        
        


    if game_over == False and flying == True:

        #generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100,100)
            btm_pipe = Pipe(screen_width, int(screen_height/2)+pipe_height,-1)
            top_pipe = Pipe(screen_width, int(screen_height/2)+pipe_height,1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        #draw and scroll the ground
        
        ground_scroll -= scroll_speed
        #scrolling ground animation
        if abs(ground_scroll) > 35:
            ground_scroll = 0  
        pipe_group.update()

    #check for game over and reset
    if game_over == True:
       if button.draw() == True:
            game_over = False
            bg_music_stop()
            reset_game()
            score = reset_game()  
            

       
    #ending the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
        
    
           
    
    pygame.display.update()

pygame.quit()           