#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os
from pygame.locals import *
from Data.Proporcional import proporcional2
from Data.Imagen import Imagen
class Letra():
	"""
	La clase Letra se define para cada Vocal posee una lista de clase Imagen que heredan los atributos de Sprite para colisiones.
	A su vez cada vocal tiene definida su propia Imagen y es agregada como unico elemento del grupo de Sprite
	"""
	def __init__(self,nombre,ruta,lista,carpImagenes,carpSonidos):
		self.nombre = nombre
		imagen = proporcional2(pygame.image.load(ruta),80).convert()
		self.spriteLetra = Imagen(imagen)
		self.lista_Sprite = []
		for i in lista:
			if (pygame.image.load(carpImagenes+'/'+i)).get_alpha() == None:
				imagen = proporcional2(pygame.image.load(carpImagenes+'/'+i),80).convert()
			else:
				imagen = proporcional2(pygame.image.load(carpImagenes+'/'+i),80).convert_alpha()
			nomSonido = carpSonidos+'/'+i[0:i.index('.')]+'.ogg'
			nuevaSprite = Imagen(imagen,nomSonido)
			self.lista_Sprite.extend([nuevaSprite])
		self.grupo_Sprite = pygame.sprite.Group(self.spriteLetra)
	def InicializarGrupo(self):
		self.grupo_Sprite = pygame.sprite.Group(self.spriteLetra)
	def getSpriteImagen(self):
		return self.spriteLetra.imagen
	def getLista_Sprite(self):
		return self.lista_Sprite
	def agregarAlGrupo(self,_sprite):
		self.grupo_Sprite.add(_sprite)
	def removerDelGrupo(self,_sprite):
		self.grupo_Sprite.remove(_sprite)

