import sys
import pygame

pygame.init()

boyut=(800,600)
ball=pygame.image.load("ball.jpg")
pencere=pygame.display.set_mode(boyut)
font=pygame.font.SysFont("Helvetica",40)
nazli=font.render("Nazli As",1,(255,0,0),(255,255,255))
# yaziBoyutX=nazli.get_size()[0]
ballX=ball.get_size()[0]
ballY=ball.get_size()[1]


x=0
y=0
xYon=1
yYon=1
clock=pygame.time.Clock()#FPS


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    pencere.fill((0,0,0))
    if x>800-ballX or x<0:
        xYon*=-1

    if y>600-ballY or y<0:
        yYon*=1

    y+=8*yYon
    x+=8*xYon
    pencere.blit(ball, (x, y))#draw images
    pygame.display.update()


