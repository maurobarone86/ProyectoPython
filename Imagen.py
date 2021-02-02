#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os,random, time,copy
from pygame.locals import *
class Imagen(pygame.sprite.Sprite):
	"""
	Clase exclusiva de el juego Come Vocales
	La clase Imagen hereda los Atributos de Sprite
	define su rectangulo para las colisiones del metodo spritecollide que funciona con rectangulos
	define su sonido para ser emitido y el metodo que lo reproduce
	"""
	def __init__(self,image,sonido=None,transparente=True):
		super().__init__()
		self.imagen = image
		if transparente:
			self.imagen.set_colorkey(self.imagen.get_at((0, 0)))
		self.rect = self.imagen.get_rect()
		self.sonido = sonido
		self.posicion = None
		self.cuadrante = None
	def setPosicion(self,pos,cuadrante):
		self.posicion= pos
		self.cuadrante = cuadrante
	def getPosicion(self):
		return self.posicion
	def imprimir(self,base):
		posicion = self.getPosicion()
		if posicion !=None:
			i = base.blit(self.imagen,posicion)
	def ReproducirSonido(self,reloj):
		s = pygame.mixer.Sound(self.sonido)
		s.play()
		reloj.tick(30)
class Imagen2(pygame.sprite.Sprite):
	"""
	clase exclusiva del Juego Acomodo y Formo
	Define sus atributos posicion inicial y final, su medodo de impresion
	y un metodo cuadrante que devuelve le cuadrante en que esta ubicado segun sus coordenadas
	
	"""
	def __init__(self,image,nombre=None,transparente=True,posIni=None,posFinal=None):
		super().__init__()
		if nombre != None:
			self.nombre = nombre[0:nombre.index('.')]
		else:
			self.nombre = None
		self.imagen = image
		if transparente:
			self.imagen.set_colorkey(self.imagen.get_at((0, 0)))
		self.rect = self.imagen.get_rect()
		self.posIni = posIni
		self.posFinal = posFinal
	def imprimir(self,base,pos):
		if pos != None:
			i = base.blit(self.imagen,pos)
	def setPosicion(self,posIni,posFinal=None):
		self.posIni = posIni
		self.posFinal = posFinal
def cuadrante(Coordenadas_cuadrantes,coor):
	if coor in Coordenadas_cuadrantes:
		return Coordenadas_cuadrantes.index(coor)
