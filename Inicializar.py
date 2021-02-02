#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os,random, time,copy
from pygame.locals import *
from Data.Letra import Letra
def Inicializar(lista):
	"""
	Inicializa los grupos de Sprite de cada vocal
	"""
	for i in lista:
		i.InicializarGrupo()
