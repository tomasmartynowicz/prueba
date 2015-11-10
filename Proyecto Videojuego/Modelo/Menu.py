from modelo.Pantalla import Pantalla
import pygame



class Menu(object):
    _instance=None
    def __new__ (self):
      if not self._instance:
         self._instance=super(Menu,self).__new__(self)
         self.pantalla=[Pantalla("Jump the Rock: Menu Principal",pygame.display.set_mode((1080,420)),'fondo.jpg',0,0,1080),
                        Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'fondo6.png',0,0,1080,'piso.png'),
                        Pantalla("Game Over",pygame.display.set_mode((1080,420)),'gameover.png',0,0,1080),
                        Pantalla("Puntajes",pygame.display.set_mode((1080,420)),'pinkfloyd.png',0,0,1080),
                        Pantalla("Como Jugar",pygame.display.set_mode((1080,420)),'intruc.jpg',0,0,1080)]
         self.opcion_instrucciones=pygame.K_KP0
         self.opcion_jugar=pygame.K_KP1
         self.opcion_verPuntaje=pygame.K_KP2      #singleton
         self.opcion_salir=pygame.K_KP3
         self.opcion_menu=pygame.K_KP_ENTER
         self.lista_puntaje=[]
      return self._instance

    def mostrarMenu(self):
        self.pantalla[0].toPantalla()

    def mostarJuego(self):
        self.pantalla[1].toPantalla()

    def mostrarGameOver(self):
        self.pantalla[2].toPantalla()

    def PantallaPuntaje(self):
        self.pantalla[3].toPantalla()

    def mostrarInstrucciones(self):
        self.pantalla[4].toPantalla()


