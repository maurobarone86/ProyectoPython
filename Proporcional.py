#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os
from pygame.locals import *
def proporcional2(imag,num):
	"""
	Acomoda la imagen png a valores proporcionales sin deformar la imagen dentro del rectangulo asignado de numero x numero
	
	"""
	medidas = imag.get_rect()
	ancho = medidas[2]
	alto = medidas[3]
	coef = None
	if ancho >= alto:
		coef = ancho/num
	else:
		coef = alto/num
	nue_ancho = ancho/coef
	nue_alto = alto/coef
	nue_imag = pygame.transform.scale(imag,(int(nue_ancho),int(nue_alto)))
	return nue_imag
