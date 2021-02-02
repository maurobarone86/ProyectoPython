#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este listado fue creado por Barone Mauro César
"""
import pygame,time,os,sys,Menú
from pygame.locals import *
pygame.init()
pygame.event.pump()
anchoTotal= 600
largoTotal= 800
def juego():
	
	areaTotal = (largoTotal,anchoTotal)
	ventana = pygame.display.set_mode((areaTotal))
	pygame.display.set_caption('P U N T A J E S')
	ruta = os.getcwd()
	os.chdir(ruta)
	fuente_elegida = pygame.font.SysFont('nanumbarungothic', 20)
	fondo1 = pygame.draw.rect(ventana,(205,255,200),(0,0,largoTotal,anchoTotal),0)
	indice=25
	
	archivo= open('ListaDePuntajes.log','r')
	cadena= archivo.read()
	lista = cadena.split('@\n')
	tamaño = len(lista)
	if tamaño > 28:
		rango= range(tamaño-29,tamaño)
	else:
		rango= range(0,tamaño)
	for i in rango:
		renglon = fuente_elegida.render(lista[i][:20]+lista[i][32:], True, pygame.Color("black"))
		renglon_rect = renglon.get_rect()
		ventana.blit(renglon,(50,indice))
		indice+=20
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					pygame.display.set_mode((300, 550))
					Menú.juego()
			
def main(args):
    juego()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
