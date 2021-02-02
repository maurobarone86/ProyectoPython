#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os,random, copy
from pygame.locals import *
from Data.Elegir import elegir
def seleccion(lista,elegidas,imagenes_activas,posible,comb,p):
	"""
	Elige lo mas aleatoriamente las posibilidades de eleccion de las imagenes
	esta diseñada para calcular si la eleccion no es posible por falta de imagenes
	"""
	posible[0]=False
	random.seed()
	combinaciones = comb.copy()
	elegidas = random.sample(lista,3)
	tamaños=[len(elegidas[0].getLista_Sprite()),len(elegidas[1].getLista_Sprite()),len(elegidas[2].getLista_Sprite())]
	eleccion = list(random.sample(combinaciones,1))
	while not posible[0] and len(combinaciones) > 0:
		if tamaños[0] >= eleccion[0][0] and tamaños[1] >= eleccion[0][1] and tamaños[2] >= eleccion[0][2]:
			posible[0] = True
		else:
			combinaciones.remove(eleccion[0])
			if len(combinaciones) > 0:
				eleccion = list(random.sample(combinaciones,1))
	if posible[0]:
		for i in range(3):
			if eleccion[0][i] > 0:
				elect = elegir(eleccion[0][i],tamaños[i])
				for y in elect:
					imagenes_activas.extend([elegidas[i].getLista_Sprite()[y]])
					elegidas[i].agregarAlGrupo(elegidas[i].getLista_Sprite()[y])
		indice=0
		for i in imagenes_activas:
			i.setPosicion(p[indice],indice)
			indice+=1
		for i in elegidas:
			i.spriteLetra.setPosicion(p[indice],indice)
			indice+=1
	return elegidas
