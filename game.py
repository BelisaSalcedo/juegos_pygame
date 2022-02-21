import pygame as pg
import random 
pg.init()

class Bola:
    def __init__(self, x, y, padre,  color = (255, 255, 255), radio = 10):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 0.2
        self.vy = 0.2
        self.padre = padre


    def mover(self):
        self.x += self.vx 
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

        #if self.radio >= self.x >= limDer - self.radio:

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1

    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio)

class Game:
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(ancho // 2, alto // 2, self.pantalla, (255, 255, 0))
        self.bolas = []
        self.numero_bolas =10#random.randint(1,10)
        self.nueva_bola=Bola(0,0,self.pantalla)
        radio=0
        
      
        for i in range  (0,self.numero_bolas) :
            
            self.bolas[i]=self.bolas.append(self.nueva_bola)
            self.nueva_bola.vx=random.randint(1,5)/10
            self.nueva_bola.vy=-random.randint (1,5)/10
            self.nueva_bola.x=random.randint(0,600)
            self.nueva_bola.y=random.randint (0,800)
            radio=random.randint (2,30)
            color=(random.randint (0,255),random.randint (0,255),random.randint (0,255))
            self.bolas[i]= Bola(self.nueva_bola.x,self.nueva_bola.y,self.pantalla,color,radio)
            
        
            
    
        """"
        for i... random de numero de bolas:
            self.bolas.append(nueva_bola)
            diferentes colores
            diferentes tamaños
            diferentes velocidades
        """

        #self.bola1 = Bola(350, 250, self.pantalla, radio=30)
        #self.bola2=Bola(80, 70,self.pantalla, (80,10,90),25)


        #self.bola1.vx = -0.1
        #self.bola1.vy = -0.3
        #self.bola2.vx=-0.5
        #self.bola2.vy=0.5
      

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            #mover todas las bolas
            #self.bola.mover()
            #self.bola1.mover()
            #self.bola2.mover()
            self.pantalla.fill((255, 0, 0)) 
            for i in  (0,self.numero_bolas-1):
                self.bolas[i].mover()
                
                   
            #dibujar todas las bolas
            #self.bola.dibujar()
            #self.bola1.dibujar()
            #self.bola2.dibujar()
            for i in  (0,self.numero_bolas-1):
                self.bolas[i].dibujar()
            
            
            pg.display.flip()

    
if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()
    