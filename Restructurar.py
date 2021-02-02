#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os,copy
from pygame.locals import *
anchoTotal= 600
largoTotal= 800
areaTotal = (largoTotal,anchoTotal)
ventana = pygame.display.set_mode((areaTotal))
areaTotal1 = (925,700)
ventana1 = pygame.display.set_mode((areaTotal1))
def restructurar(l_imagenes,l_elegidas,base,img=None,):
	"""
	Modulo diseñado para ser usado en Come Vocales
	restructura lo que se va a mostrar en pantalla
	puede ser usado de dos maneras posibles:
		-Mostrando todas las imagenes activas
		-Mostrando todas las imagenes activas menos una
	"""
	fondo1 = pygame.draw.rect(base,(200, 255, 255),(0,0,largoTotal,anchoTotal),0)
	for i in l_elegidas:
		i.spriteLetra.imprimir(ventana)
	aux = l_imagenes.copy()
	if img != None:
		aux.remove(img)
	for i in aux:
		i.imprimir(ventana)
def restructurar2(opcion,l_imagenes,base1,largo1,ancho1,Coordenadas_cuadrantes,elegidos,ubicados,img=None,):
	"""
	Modulo diseñado para ser usado en Acomodo y Formo
	restructura lo que se va a mostrar en pantalla
	puede ser usado de dos maneras posibles:
		-Creando los rectangulos de posicion y mostrando todas las imagenes de la lista de imagenes y la lista de ubicados
		-Creando los rectangulos de posicion y mostrando todas las imagenes de la lista de ubicados y la lista de imagenes menos una
	"""
	
	fondo2 = pygame.draw.rect(base1,(255,255,200),(0,0,largo1,ancho1),0)
	lista=[]
	for i in range(3,len(Coordenadas_cuadrantes)):
		if i >= 36 and i <= 65:
			if opcion=='S':
				rec = pygame.draw.rect(base1,(255,255,255),(Coordenadas_cuadrantes[i][0],Coordenadas_cuadrantes[i][1],50,50),0)
				rec1 = pygame.draw.rect(base1,(100,152,132),(Coordenadas_cuadrantes[i][0],Coordenadas_cuadrantes[i][1],50,50),1)
				lista.extend([rec])
				lista.extend([rec1])
		else:
			if opcion=='L':
				rec = pygame.draw.rect(base1,(255,255,255),(Coordenadas_cuadrantes[i][0],Coordenadas_cuadrantes[i][1],25,25),0)
				rec1 = pygame.draw.rect(base1,(100,152,132),(Coordenadas_cuadrantes[i][0],Coordenadas_cuadrantes[i][1],25,25),1)
				lista.extend([rec])
				lista.extend([rec1])
	if ubicados != []:
		for i in ubicados:
			i.imprimir(ventana1,i.posIni)
	for i in elegidos:
		i.spriteImagen.imprimir(ventana1,i.spriteImagen.posIni)
	aux = l_imagenes.copy()
	if img != None:
		aux.remove(img)
	for i in aux:
		i.imprimir(ventana1,i.posIni)	
		
