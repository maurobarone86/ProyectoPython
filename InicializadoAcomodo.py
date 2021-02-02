#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame,sys,os,random,time,copy,json,os.path
def inicializadoAcomodo(elegidos,list_coord,Coordenadas_cuadrantes,opcion):
	"""
	Inicializa los valores y las posiciones las letras y las silabas segun la opcion en sus 
	respectivos cuadrantes
	"""
	activos = []
	coord = list(Coordenadas_cuadrantes.copy())
	indice=0
	indice1=1
	indice2=4
	iniSilabas= coord[51:66]
	iniLetras= coord[66:]
	for i in elegidos:
		i.spriteImagen.setPosicion(Coordenadas_cuadrantes[indice])
		if opcion == 'L':
			for y in range(0,len(i.listaSpriteLetras)):
				elem = random.choice(iniLetras)
				iniLetras.remove(elem)
				i.listaSpriteLetras[y].setPosicion(elem,list_coord[indice1][y][0])
				activos.extend([i.listaSpriteLetras[y]])
			indice1+=1
		else:
			for y in range(0,len(i.listaSpriteSilabas)):
				elem1 = random.choice(iniSilabas)
				iniSilabas.remove(elem1)
				i.listaSpriteSilabas[y].setPosicion(elem1,list_coord[indice2][y][0])
				activos.extend([i.listaSpriteSilabas[y]])
			indice2+=1
		indice+=1
	return activos
	
