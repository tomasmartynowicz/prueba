from Pantalla import Pantalla
import pygame



class Menu(object):
    _instance=None
    def __new__ (self):
      if not self._instance:
         self._instance=super(Menu,self).__new__(self)
         self.pantalla=[Pantalla("Jump the Rock:",pygame.display.set_mode((1080,420)),'image/fondo.jpg',0,0,1080),
                        Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'image/fondo6.png',0,0,1080,'image/piso.png'),
                        Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'image/gameover.png',0,0,1080),
                        Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'image/f_puntaje.png',0,0,1080),
                        Pantalla("Jump the Rock",pygame.display.set_mode((1080,420)),'image/intruc.jpg',0,0,1080)]
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


