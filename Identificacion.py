#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os,random, time,copy
from pygame.locals import *
from Data.Imagen import cuadrante
def identificacion(posicion,activos,Coordenadas_cuadrantes):
	"""
	Identifica segun su posicion de cuadrante elegida por el modulo ubicacion
	si es una imagen activa para ser utilizada
	"""
	if posicion != None:
		lista=[]
		for i in activos:
			lista.extend([cuadrante(Coordenadas_cuadrantes,i.posIni)])
		if posicion in lista:
			i = lista.index(posicion)
			return activos[i]
	else:
		return None


