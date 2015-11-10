from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
import pygame

class Pantalla(object):
    def __init__(self,nombre,display,imagen,x,y,resolucion,piso = None):
        self.nombre=pygame.display.set_caption(nombre)
        self.display=display
        self.resolucion=resolucion
        self.imagen=imagen                                                      #self.imagen guarda la direccion del fondo
        self.fondo=pygame.image.load(imagen).convert()                                    #Carga solo 1 imagen
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
            self.fondo=pygame.image.load(self.imagen).convert()

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
                self.x_init[1]=0
            else:
                self.x_init[0]=0
        else:
            self.x_piso[pos]=self.x_piso[pos] - 16


    def detenerPantalla(self):
            self.x[0]=0
            self.y=420

    def cargarPantalla(self,jugador,enemigo,puntaje,pantalla):
        fuente = pygame.font.Font(None, 25)
        texto = fuente.render("Jum the rock!! Score: "+str(puntaje), True, (255, 255, 255))
        pantalla.toPantalla()
        jugador.toPantalla(self.display)
        enemigo.toPantalla(self.display)
        self.display.blit(texto,[0, 0])#imprime puntaje

    def setEscribir(self,keys,event,cadena):

        f1 = pygame.font.Font(None, 100)
        reloj1 = pygame.time.Clock()
        escribio=False
        caracter=False
        pos_x=0
        caraceterValido=""


        while escribio!=True and caracter!=True: #mientras dejo de escribir y de escribir carcateres

                 for event in pygame.event.get():

                         if event.type == pygame.QUIT:
                                caracter=True
                                escribio = True


                         keys = pygame.key.get_pressed()

                         if keys[pygame.K_ESCAPE]:
                                   carcater=True
                                   escribio=True
                         else:
                                   caracter=False



                         if keys[pygame.K_NUMLOCK]!=True:

                             if pygame.key.get_focused() and escribio!=True and caracter!=True:

                                 for i in xrange(0,len(keys)):

                                   name=pygame.key.name(i)

                                   if keys[i]==1 and caracter!=True:
                                              caracter=True
                                              caraceterValido=name
                                              cadena=cadena+caraceterValido
                                              keys = pygame.key.get_pressed()
                         else:
                               text=f1.render("Desconecta  Bloq Num del teclado Numerico",True,(250,250,250))
                               self.display.blit(text,(0,50))


                 if caracter==True:
                    text=f1.render(cadena,True,(250,250,250))
                    self.display.blit(text,(pos_x+10,100))
                    pos_x=pos_x+50





                 pygame.event.post(event)
                 reloj1.tick(30)
                 pygame.display.update()




        return cadena


    def mostrarCadena(self, cadena):
        f2 = pygame.font.Font(None,300)
        text=f2.render(cadena,True,(255,255,255))
        self.display.blit(text,(0,100))
        pygame.display.update()

    def cadenaVacia(self, cadena):
        respuesta=False
        for i in xrange(0,len(cadena)):
            if cadena[i]=="":
               respuesta=True
        return respuesta

    def mensajeIngrese(self):
        fuente = pygame.font.Font(None, 50)
        texto = fuente.render("Ingrese Su Nombre: [Esc. para finalizar]", True, (255, 255, 255))
        self.display.blit(texto,[0, 0])#imprime










