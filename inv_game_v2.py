import pygame
from pygame.locals import *
import sys
import random
import numpy as np
import Eslope_test as FLUX
import time
import matplotlib.pyplot as plt

def display(screen,table):
    screen.fill((0,10,50))
    back_img = pygame.image.load("back.png")
    back_img = pygame.transform.scale(back_img, (700, 700))
    screen.blit(back_img, (0,0))
    #back_img = pygame.transform.scale(back_img, (100, 50))
    pygame.draw.line(screen,(255,255,255),(700,0),(700,700),width=6)
    pygame.draw.line(screen,(255,255,255),(700,100),(900,100),width=6)
    Scorefont = pygame.font.SysFont(None,35)
    KeyboardFont=pygame.font.SysFont(None,30)
    font=KeyboardFont.render("0 : result",True,(0,255,0))
    screen.blit(font, (800,600))
    y=0
    #fontScore=Scorefont.render("log(E/eV) count",True,(255,255,255))
    #screen.blit(fontScore, (710,150))       
    for logE in ["18","19","20","21"]:
        fontScore=Scorefont.render(logE+"~  "+str(table[logE][1])+"/"+str(table[logE][0]),True,(255,255,255))
        screen.blit(fontScore, (730,250+y))    
        y+=50

class moveball:
    def __init__(self,screen,x,y,Flux):
        self.screen = screen
        self.x = x
        self.y = y
        self.Flux = Flux

    def moving(self):
        energyfont10 = pygame.font.SysFont(None,35)
        energyfontEXP = pygame.font.SysFont(None,25)
        font10=energyfont10.render("10", True, (255,255,255))
        fontEXP=energyfontEXP.render(str(round(self.Flux,1)), True, (255,255,255))
        pygame.draw.circle(self.screen, (255,0,0),(self.x,self.y),self.Flux)
        self.screen.blit(font10, (self.x-15,self.y-40))
        self.screen.blit(fontEXP, (self.x+10,self.y-45))


def lightning(screen,orgx,orgy):
    num=10 #random.randint(1,10)
    x=[None]*num
    y=[None]*num
    x[0]=orgx
    y[0]=orgy
    col2=(255,12,12)
    #col1=(0,0,255)
    col3=(0,0,0)
    for i in range(len(x)-1):
        r=random.randint(-20,20)*10+18
        theta=random.randint(-180,180)*np.pi/180
        x[i+1]=r*np.cos(theta)+x[0]
        y[i+1]=r*np.sin(theta)+y[0]
        pointsize=random.randint(0,4)
        #pygame.draw.circle(screen, col1, (x[i+1],y[i+1]),pointsize+2)
        pygame.draw.circle(screen, col2, (x[i+1],y[i+1]),pointsize+1)
        pygame.draw.circle(screen, col3, (x[i+1],y[i+1]),pointsize)
        #pygame.draw.line(screen,col1,(x[i],y[i]),(x[i+1],y[i+1]),3)
        pygame.draw.line(screen,col2,(x[i],y[i]),(x[i+1],y[i+1]),2)  
        pygame.draw.line(screen,col3,(x[i],y[i]),(x[i+1],y[i+1]),1)       
        pygame.display.update()


def Score(screen,score):
    Scorefont = pygame.font.SysFont(None,40)
    fontScore=Scorefont.render("score : "+str(score),True,(255,255,255))
    screen.blit(fontScore, (720,25))


def Detector_Selection(screen):
    #back_img = pygame.image.load("IMG_7819.png")
    #back_img = pygame.transform.scale(back_img, (300, 300))
    #screen.blit(back_img, (300,0))
    while (1):
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == QUIT:
                pygame.quit()     
                sys.exit()
            button_SSD = pygame.Rect(100, 480, 300, 100)
            button_WCD = pygame.Rect(500, 480, 300, 100)
            font = pygame.font.SysFont(None, 100)    
            text_m = font.render("SSD", True,(0,0,0))
            text_p = font.render("WCD", True,(0,0,0))
            pygame.draw.rect(screen, (0, 150, 150), button_SSD)
            pygame.draw.rect(screen, (0, 150, 150), button_WCD)
            screen.blit(text_m,(175,500))
            screen.blit(text_p,(575,500))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_SSD.collidepoint(event.pos):
                    return "SD3.png"
                if button_WCD.collidepoint(event.pos):
                    return "WCD.png"
                

def FluxTable(screen,genE,getE):
    screen.fill((0,0,0))
    bin_edges = np.linspace(18, 21, 15) 
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hist(genE,bins=bin_edges,alpha=0.5,color="red")
    ax.hist(getE,bins=bin_edges,alpha=0.5,color="blue")
    ax.set_xlim(18,21)
    ax.set_yscale("log")
    fig.savefig("reslut.png")
    result_img = pygame.image.load("reslut.png")
    font = pygame.font.SysFont("hg正楷書体pro", 200)    
    text = font.render("Result", True,(255,0,0))
    button = pygame.Rect(680, 15, 200, 50)
    font2 = pygame.font.SysFont("hg正楷書体pro", 50)  
    RESTART = font2.render("RESTART", True,(0,0,255))
    screen.blit(result_img, (100,200))
    screen.blit(text,(250,50))
    pygame.draw.rect(screen, (0, 150, 150), button)
    screen.blit(RESTART,(700,20))
    pygame.display.update()
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()     
                sys.exit()
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    return 1


def countdown(screen):
    font = pygame.font.SysFont("hg正楷書体pro", 500)    
    for num in ["3","2","1"]:
        screen.fill((0,10,50))
        text = font.render(num, True,(0,255,0))
        screen.blit(text,(350,200))
        pygame.display.update()
        time.sleep(1)



def count_time(screen,time):
    font = pygame.font.SysFont("hg正楷書体pro", 50) 
    s = round(time/1000,2)
    if s < 0:
        s = 0.00
    text = font.render(str(s), True,(0,255,0))
    screen.blit(text,(730,180))
    pygame.display.update()


def detector(det):
    img = pygame.image.load(det)
    img = pygame.transform.scale(img, (200, 175))
    if det == "SD3.png":
        HitX = (-100,+50)
        HitY = (+550,+570)
    if det == "WCD.png":
        HitX = (-130,+130)
        HitY = (+550,+570)
    return img,HitX,HitY


    

def main():
    while (1):
        restart = 0
        pygame.init()
        genE=[]
        getE=[]
        screen = pygame.display.set_mode((900,700))
        pygame.display.set_caption("Eslope")
        det_img,hitx,hity = detector(Detector_Selection(screen))
        screen.fill((0,0,0))
        SCORE=0
        table={"18":[0,0],"19":[0,0],"20":[0,0],"21":[0,0]}
        countdown(screen)
        time30 = pygame.time.get_ticks()+30000
        countTIME = 0
        while restart == 0 :
            y=0
            E=FLUX.Flux(1)
            x=random.randint(100,600)
            genE.append(E)
            while ( y<710 and restart == 0 ):
                countTIME = pygame.time.get_ticks()
                if time30 <= countTIME:
                    restart = FluxTable(screen,genE,getE)
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX >= 700:
                    mouseX = 600
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()     
                        sys.exit()
                key = pygame.key.get_pressed()
                if key[pygame.K_0]:
                    restart = FluxTable(screen,genE,getE)
                display(screen,table)
                screen.blit(det_img, (mouseX-100,450))   
                moveball(screen,x,y,E).moving()
                if mouseX+hitx[0] <= x <= mouseX+hitx[1] and hity[0] <= y <= hity[1]:
                    y,score=710,E
                else:
                    y,score=y,0
                SCORE+=round(score,1)
                if score > 0:
                    table[str(int(score))][1]+=1
                getE.append(score)
                Score(screen,round(SCORE,1))
                count_time(screen,abs(countTIME-time30+30))
                y += E
                pygame.display.update()
            table[str(int(E))][0]+=1
if __name__ == "__main__":
    main()