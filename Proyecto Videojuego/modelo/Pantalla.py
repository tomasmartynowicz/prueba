from Jugador import Jugador
from Enemigo import Enemigo
import pygame
pygame.init()

class Pantalla(object):
    def __init__(self,nombre,display,imagen,x,y,resolucion,piso = None):
        self.nombre=pygame.display.set_caption(nombre)
        self.display=display
        self.resolucion=resolucion
        self.imagen=imagen                                                      #self.imagen guarda la direccion del fondo
        self.fondo=pygame.image.load(imagen).convert_alpha()                                    #Carga solo 1 imagen
        self.x=[x,x+resolucion]
        self.y=y
        self.dir_piso=piso                                                      #Atributos del piso
        if piso != None:
            self.piso=pygame.image.load(self.dir_piso)
            self.x_piso=[x,x+resolucion]
            self.x_init=[x,x+resolucion]
            self.y_piso=362
            self.t=1

    #Setters
    def setNombre(self, nombre):
            self.nombre=pygame.display.set_caption(nombre)

    def setDisplay(self,x,y):
            self.display=pygame.display.set_mode((x,y))

    def setImagen(self):
            self.fondo=pygame.image.load(self.imagen).convert_alpha()

    def setPiso(self):
        self.piso=pygame.image.load(self.piso).convert_alpha()

    def setX(self, x):
            self.x=x

    def setY(self, y):
            self.y=y
    #toPantalla()
    def toPantalla(self):  #tipo el toString()
         fondoCopy=self.fondo.copy()                        #imprime en pantalla los 2 fondos
         self.display.blit(self.fondo,[self.x[0], self.y])  #Copia el fondo a otra superficie
         self.display.blit(fondoCopy,[self.x[1],self.y])    #y imprime el fondo con las coordenadas correspondientes
         if self.dir_piso != None:
            pisoCopy=self.piso.copy()
            self.display.blit(self.piso,[self.x_piso[0],self.y_piso])
            self.display.blit(pisoCopy,[self.x_piso[1],self.y_piso])



    #metodos

    def moverPantalla(self,pos):          #cambia la posicion de 1 fondo, por lo que se pasa como
        if self.x[pos]<=-self.resolucion:      #parametro la posicion en X[]
            self.x[pos]=self.resolucion
            self.y=420
        else:
            self.x[pos]=self.x[pos]-2 #es 2
            self.y=0

    def moverPiso(self,pos):                        #Nuevo metodo para mover el piso
        if self.x_piso[pos]<=-self.resolucion:
            self.x_piso[pos]=self.resolucion
            self.x_init[pos]=self.resolucion
            if pos == 0:
                self.x_piso[1]=0
                self.x_init[1]=0
            else:
                self.x_piso[0]=0
                self.x_init[0]=0
        else:
            self.x_piso[pos]=self.x_piso[pos] - 16


    def detenerPantalla(self):
            self.x[0]=0
            self.y=420

    def cargarPantalla(self,jugador,enemigo,puntaje,pantalla):
        fuente = pygame.font.Font('font/Snickles.ttf',50)
        texto = fuente.render("Jump the rock!! Score: "+str(puntaje), True, (255, 255, 255))
        pantalla.toPantalla()
        jugador.toPantalla(self.display)
        enemigo.toPantalla(self.display)
        self.display.blit(texto,[0, 0])#imprime puntaje

    def setEscribir(self,keys,cadena):
        caraceterValido=""
        inicioCadena=0
        caracter=False

                #keys = pygame.key.get_pressed()

        for i in xrange(0,len(keys)):
               name=pygame.key.name(i)
               if keys[i]==1 and caracter!=True and self.esLetra(keys):
                             caracter=True
                             caraceterValido=name
                             inicioCadena=inicioCadena+1


        if keys[pygame.K_BACKSPACE]:
                    cadena=cadena[:inicioCadena-1]
                    caracter=True

        if caracter:
                    cadena=cadena+caraceterValido

        return cadena


    def mostrarCadena(self, cadena):
        f2 = pygame.font.Font('font/HEADOH__.ttf',80)
        text=f2.render("Escriba Su Nombre: "+cadena,True,(255,255,255))
        self.display.blit(text,(0,100))
        pygame.display.update()

    def cadenaVacia(self, cadena):
        respuesta=False
        for i in xrange(0,len(cadena)):
            if cadena[i]=="":
               respuesta=True
        return respuesta

    def mensajeIngrese(self):
        fuente = pygame.font.Font('font/Fontin-Italic.ttf',30)
        texto = fuente.render("[Presione prolongadamente la tecla [Esc.] para finalizar]", True, (255, 255, 255))
        self.display.blit(texto,[0, 0])#imprime



    def esLetra(self, letra):
      keys=letra
      respuesta=False
      if keys[pygame.K_a]:respuesta=True
      if keys[pygame.K_b]:respuesta=True
      if keys[pygame.K_c]:respuesta=True
      if keys[pygame.K_d]:respuesta=True
      if keys[pygame.K_e]:respuesta=True
      if keys[pygame.K_f]:respuesta=True
      if keys[pygame.K_g]:respuesta=True
      if keys[pygame.K_h]:respuesta=True
      if keys[pygame.K_i]:respuesta=True
      if keys[pygame.K_j]:respuesta=True
      if keys[pygame.K_k]:respuesta=True
      if keys[pygame.K_l]:respuesta=True
      if keys[pygame.K_m]:respuesta=True
      if keys[pygame.K_n]:respuesta=True
      if keys[pygame.K_o]:respuesta=True
      if keys[pygame.K_p]:respuesta=True
      if keys[pygame.K_q]:respuesta=True
      if keys[pygame.K_r]:respuesta=True
      if keys[pygame.K_s]:respuesta=True
      if keys[pygame.K_t]:respuesta=True
      if keys[pygame.K_u]:respuesta=True
      if keys[pygame.K_v]:respuesta=True
      if keys[pygame.K_w]:respuesta=True
      if keys[pygame.K_x]:respuesta=True
      if keys[pygame.K_y]:respuesta=True
      if keys[pygame.K_z]:respuesta=True
      return respuesta





