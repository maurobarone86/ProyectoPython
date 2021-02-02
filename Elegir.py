#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os,random
from pygame.locals import *
def elegir(cant,total):
	"""
	Elige la cantidad (cant) de numeros enteros de una sucesion de numeros enteros
	Esta diseñado para elegir aleatoriamente la cantidad de imagenes que pertencen a una vocal
	la lista de numeros devueltos seran los indices de las listas de Imagenes a seleccionar de una vocal
	"""
	random.seed()
	lista = range(total)
	eleg = list(random.sample(lista,cant))
	return eleg
