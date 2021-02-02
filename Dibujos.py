#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os,random, time,copy
from pygame.locals import *
from Data.Proporcional import proporcional2
from Data.Imagen import Imagen2
class Dibujo():
	"""
	Clase exclusiva de Acomodo y Formo
	define la estrategia y logica del juego
	posee una imagen y las listas de letras y silabas que la forman en el orden en que se construye
	para despues ser asignados por posicion a los cuadrantes
	"""
	def __init__(self,listaLetras,listaSilabas,carp_imagenes,carp_letras,carp_silabas,nombre):
		self.nombre= nombre
		if (pygame.image.load(carp_imagenes+nombre.lower()+'.png')).get_alpha() == None:
			imagen = proporcional2(pygame.image.load(carp_imagenes+nombre.lower()+'.png'),200).convert()
		else:
			imagen = proporcional2(pygame.image.load(carp_imagenes+nombre.lower()+'.png'),200).convert_alpha()
		self.spriteImagen = Imagen2(imagen)
		self.listaSpriteLetras=[]
		self.listaSpriteSilabas=[]
		for i in listaLetras:
			_Sprite = Imagen2(proporcional2(pygame.image.load(carp_letras+i),25).convert(),i)
			self.listaSpriteLetras.extend([_Sprite])
		for i in listaSilabas:
			_Sprite1 = Imagen2(proporcional2(pygame.image.load(carp_silabas+i),50).convert(),i)
			self.listaSpriteSilabas.extend([_Sprite1])
			
		
	

