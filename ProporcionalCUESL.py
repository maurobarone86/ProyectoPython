#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os
from pygame.locals import *
def proporcional(imag,valor):
	"""
	Acomoda la imagen png a valores proporcionales sin deformar la imagen dentro del rectangulo asignado de valor x valor
	"""
	medidas = imag.get_rect()
	ancho = medidas[2]
	alto = medidas[3]
	coef = None
	if ancho >= alto:
		nue_ancho=valor
		nue_alto=(alto*valor)/ancho
	else:
		nue_alto=valor
		nue_ancho=(ancho*valor)/alto
	nue_imag = pygame.transform.scale(imag,(int(nue_ancho),int(nue_alto)))
	return nue_imag
