#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este Menú fue creado por Scotto Laura Sofia
"""
import pygame, os, sys, random, bisect, json, time
from pygame.locals import *
import CadaUnaEnSuLugar,ComeVocales,ElEntrometido,ImpresionPuntajes,AcomodoYFormo

pygame.init()
pygame.event.pump()
pygame.mixer.pre_init(44100,-16,2,1024)

class Opcion():
    '''
        Inicializa un rect blanco, borde gris
        con text pasado como dato
    '''
    def __init__(self,juego):
        super(Opcion,self).__init__()
        self.texto=juego
        def set_cuadro(juego):
            x = pygame.Surface((200,50)).convert()
            x.fill(colores['blanco'])
            fuente = pygame.font.Font("Data/tipografias" + os.path.sep + 'OpenSans.ttf', 18)
            titulo = fuente.render(juego, True, colores['casiNegro'])
            titulo_rect = titulo.get_rect()
            titulo_rect.centerx = x.get_rect().centerx
            titulo_rect.centery = x.get_rect().centery
            x.blit(titulo, titulo_rect)
            pygame.draw.rect(x, colores['gris'], (0, 0, 200, 50), 5)
            pygame.display.update()
            return x
        self.cuadro=set_cuadro(juego)
        self.rect=self.cuadro.get_rect()

    def move_rect(self,x,y):
        '''
            Mueve el rectangulo al punto x,y
        '''
        self.rect.move_ip(x, y)


#paleta de colores
colores={'violetaOscuro':(81,45,168),'lila':(209,196,233),'violeta':(103,58,183),'blanco':(255,255,255),'cian':(0,188,212),'casiNegro':(33,33,33),'grisOscuro':(117,117,117),'gris':(189,189,189)}

#Inicializar pantalla
pantalla = pygame.display.set_mode((300,550))
pygame.display.set_caption('Juego')

#rellenar fondo
fondo = pygame.Surface((300,450))
fondo.fill(colores['violeta'])
fondo_titulo=pygame.Surface((300,100))
fondo_titulo.fill(colores['violetaOscuro'])
pantalla.blit(fondo,(0,100))
pygame.display.flip()
opciones = []

def titulo_juego():
	'''
		Coloco título del juego
	'''
	fuente = pygame.font.Font("Data/tipografias"+os.path.sep+'Barrio.ttf',35)
	titulo = fuente.render(" APRENDÉ JUGANDO ", True, colores['lila'])
	titulo_rect = titulo.get_rect()
	titulo_rect.centerx = fondo_titulo.get_rect().centerx
	titulo_rect = titulo_rect.move(0,25)
	fondo_titulo.blit(titulo, titulo_rect)
	pantalla.blit(fondo_titulo,(0,0))
	pygame.display.flip()

def guardar_juegos():
	juegos = ['Come Vocales','Acomodo Y Formo','El Entrometido','Cada Una En Su Lugar','Jugadas']
	archivo = open("Data/Menú.txt", "w")
	json.dump(juegos, archivo)
	archivo.close()

def cargar_juegos():
    archivo = open("Data/Menú.txt", "r")
    juegos = json.load(archivo)
    archivo.close()
    return juegos

def tablero(juegos):
    '''
        Armo el tablero del menu
        devuelve copia de la pantalla
        actualizada
    '''
    y = 50
    x = 50
    for i in juegos:
        op = Opcion(i)
        op.move_rect(x,y)
        opciones.append(op)
        fondo.blit(op.cuadro,(x,y))
        pantalla.blit(fondo,(0,100))
        y+=75
    pygame.display.flip()
    return pantalla.copy()

def dibujar_rect(color,sup,y):
    '''
		Dibuja rect en el borde cuadro mandado
	'''
    pygame.draw.rect(sup, color, (0, 0, 200, 50), 5)
    pygame.display.update()
    pantalla.blit(sup, (50,y))


def juego():
    '''
        Comienzo el juego
    '''
    titulo_juego()
    guardar_juegos()
    juegos = cargar_juegos()
    pantalla_base = tablero(juegos)
    col=0
    fila=0
    click=False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            else:
                filas=[150,200,225,275,300,350,375,425,450,500]#1 3 5 7 9
                columnas=[50,250]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    fila = bisect.bisect(filas,event.pos[1])
                    col = bisect.bisect(columnas,event.pos[0])
                    if col == 1 and (fila == 1 or fila == 3 or fila == 5 or fila == 7 or fila == 9):
                        pygame.mixer.Sound('Data/Sonidos' + os.path.sep +'124912__greencouch__ploep5.aiff').play()
                        click = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    click = False
                    dibujar_rect(colores['gris'], opciones[0].cuadro, 150)
                    dibujar_rect(colores['gris'], opciones[1].cuadro, 225)
                    dibujar_rect(colores['gris'], opciones[2].cuadro, 300)
                    dibujar_rect(colores['gris'], opciones[3].cuadro, 375)
                    dibujar_rect(colores['gris'], opciones[4].cuadro, 450)
        if click:
            if fila == 1:
                dibujar_rect(colores['cian'],opciones[0].cuadro, 150)
                pygame.display.set_mode((800, 600))
                ComeVocales.juego()
            elif fila == 3:
                dibujar_rect(colores['cian'],opciones[1].cuadro, 225)
                pygame.display.set_mode((800, 600))
                AcomodoYFormo.juego()
            elif fila == 5:
                dibujar_rect(colores['cian'],opciones[2].cuadro, 300)
                pygame.display.set_mode((800,600))
                ElEntrometido.juego()
            elif fila == 7:
                dibujar_rect(colores['cian'],opciones[3].cuadro, 375)
                pygame.display.set_mode((800, 600))
                CadaUnaEnSuLugar.juego()
            elif fila == 9:
                dibujar_rect(colores['cian'],opciones[4].cuadro, 450)
                pygame.display.set_mode((800, 600))
                ImpresionPuntajes.juego()


def main(args):
    juego()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
