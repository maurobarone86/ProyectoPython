#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame,sys,os,time,os.path,datetime,time,platform,logging

def cargarPuntaje(puntaje):
	ruta = os.getcwd()
	os.chdir(ruta)
	fichero_log = ruta+os.path.sep+'ListaDePuntajes.log'
	if not (os.path.exists(fichero_log)):
		logging.basicConfig(level=logging.DEBUG,format='%(asctime)s : %(levelname)s : %(message)s',filename = fichero_log,filemode = 'w',)
	else:
		logging.basicConfig(level=logging.DEBUG,format='%(asctime)s : %(levelname)s : %(message)s',filename = fichero_log,filemode = 'a',)
	logging.info('Juego: '+puntaje[0]+', Puntos: '+str(puntaje[1])+'@')
	
