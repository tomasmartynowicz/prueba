import pygame
from modelo.Jugador import Jugador
from modelo.Enemigo import Enemigo
from modelo.Sonido import Sonido
from modelo.Juego import Juego
from modelo.Pantalla import Pantalla
from modelo.Menu import Menu
pygame.init()


salir = False

reloj1 = pygame.time.Clock()


# CONSTANTES Y Inicializacion de variables
BLANCO = (255, 255, 255)
cadena=""
escribio=False
tiempo=1
#Prueba Setters

jugador=Jugador('Perro4.png',0,320,"jugador1")
jugador.setImagen('Perro4.png')
jugador.setX(0)
jugador.setY(320)
jugador.setAlias("jugador1")

enemigo=Enemigo('rock.png',500,320)
enemigo.setImagen('rock.png')
enemigo.setX(1000)
enemigo.setY(320)

menu=Menu()

pantalla= menu.pantalla[0]

newGame=Juego(jugador,enemigo,pantalla,0)
newGame.setJugador(jugador)
newGame.setEnemigo(enemigo)
newGame.setPantalla(pantalla)
newGame.setPuntaje(0)

pantalla2=menu.pantalla[0]

jump=Jugador('fondo2.jpg',320,20,"jugador1")
iconoUnla=Jugador('unla.png',0,0,"jugador1")
roca=Jugador('rock.png',320,20,"jugador1")
#salir=True
#Bucle principal del videojuego
escribio=False

while salir != True:

    for event in pygame.event.get():

            keys = pygame.key.get_pressed()

            pantalla2.toPantalla()

            #test escribir pantalalla
            if escribio!=True:
              cadena=pantalla2.setEscribir(keys,event,cadena)


            if keys[pygame.K_ESCAPE]:
               pantalla2.mostrarEscribir(cadena)
               escribio=True


            if event.type == pygame.QUIT:
                      salir = True

    pygame.event.post(event)


    reloj1.tick(30)
    pygame.display.update()


pygame.quit()
quit()




