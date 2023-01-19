from graphics import *
from person import *
from math import sin, cos, pi, sqrt
import time

def verify_points_distance(p1, p2):
    return sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)

def verify_colision_circles(circle, circle_2):
    centers_distance = verify_points_distance(circle.getCenter(), circle_2.getCenter())
    if centers_distance <= circle.getRadius() + circle_2.getRadius():
        return True
    return False

cont2 = 0
win = GraphWin("Donkey Kong",600,686, autoflush=False)
barril = BarrilAzul(115,198,win)
cenario = Image(Point(300,343),"./assets/cenario.png")
cenario.draw(win)
frameRate = 1.0/60
p1 = Mario(6, 650, win, 25)
Princesa = Princesa(255,128,win)
Dk = Donkey(115,184,win)
vet = []
teste = False
teste2 = False
jogueiBarril = False
cont = 0
while not win.isClosed():
    if verify_colision_circles(barril, p1) and cont < 150:
        p1.morrer()
        break
    start_time = time.time()
    if jogueiBarril:
        for val in vet:
            val.getPosicao()
            val.move()
            if verify_colision_circles(val, p1) == True:
                p1.morrer()
                break
        
    for val in vet:
        if val.acabou == True:
            vet.pop(0)
            val.undraw()
            print("Foi",vet)
    p1.getPosicao()
    p1.move()
    p1.gravidade()
    update(34)
    if cont == 60 and teste == False:
        Dk.inicia(1)
        teste = True
    if cont == 100 and teste2 == False:
        Dk.inicia(2)
        print(cont)
        teste2 = True
    if teste2:
        barril.jogarBarrilAzul(cont, cont2)
    if cont % 120 == 0 and cont != 0:
        Dk.jogarBarril(1)
    if cont % 140 == 0 and cont != 0:
        Dk.jogarBarril(2)
    if cont % 160 == 0 and cont != 0:
        Dk.jogarBarril(3)
        NovoBarril = Barril(190,212,win)
        vet.append(NovoBarril)
        jogueiBarril = True
    if cont % 180 == 0 and cont != 0:
        Dk.jogarBarril(4)
        cont = 0
        cont2 = 1    
    if cont % 100 == 0 and cont != 0:
        Princesa.idle(True)
    if cont % 150 == 0 and cont != 0:
        Princesa.idle(False)
    if p1.ganhou:
        cenario = Image(Point(300,343),"./assets/teladefim.png").draw(win)
        update(24)
        win.getMouse()
    if p1.die:
        
        win.close()
    cont += 1
    end_time = time.time()
    frameTime = end_time - start_time
    if (frameTime) < (frameRate):
        sleep((frameRate) - frameTime)

    
win.close()