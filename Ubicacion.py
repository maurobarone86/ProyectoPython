#!/usr/bin/env python
# -*- coding: utf-8 -*-
def ubicacion(coordX,coordY,listaL,listaI):
	"""
	Modulo exclusivo para ser usar en Come Vocales
	Devuelve el objeto imagen en caso de una imagen activa o una la Letra en el caso de click sobre una letra
	en el caso de click sobre un sector de la pantalla sin objetos la funcion devuelve None
	"""
	pos=None
	if coordX >= 100 and coordX <=180:
		if coordY >= 75 and coordY <= 155:
			pos=0
			
		elif coordY >= 425 and coordY <= 505:
			pos=3
			
	if coordX >= 550 and coordX <= 630:
		if coordY >= 75 and coordY <= 155:
			pos=2
			
		elif coordY >= 425 and coordY <= 505:
			pos=5
			
	if coordX >= 325 and coordX <=405:
		if coordY >= 75 and coordY <= 155:
			pos=4
			
		elif coordY >= 425 and coordY <= 505:
			pos=1
					
	if coordY >= 250 and coordY <=300:
		if coordX >= 250 and coordX <= 300:
			pos=6
			
		elif coordX >= 350 and coordX <= 400:
			pos=7
			
		elif coordX >= 450 and coordX <= 500 :
			pos=8
	if pos != None and listaI != []:
		lista = []
		for i in listaI:
			lista.extend([i.cuadrante])
		if pos in lista:
			indice = lista.index(pos)
			return listaI[indice]
		else:
			lista = []
			for i in listaL:
				lista.extend([i.spriteLetra.cuadrante])
			if pos in lista:
				indice = lista.index(pos)
				return listaL[indice]
def ubicacion2(coordX,coordY,indice):
	"""
	Modulo deseñado para ser usado en Acomodo y Formo
	Devuelve el objeto imagen en caso de una imagen activa
	o None en el caso de sector vacio
	"""
	pos=None
	if coordY >= 275 and coordY <=300:
		if coordX >= 25 and coordX < 50:     pos=3
		elif coordX >= 50 and coordX < 75:   pos=4
		elif coordX >= 75 and coordX < 100:  pos=5
		elif coordX >= 100 and coordX < 125: pos=6
		elif coordX >= 125 and coordX < 150: pos=7
		elif coordX >= 150 and coordX < 175: pos=8
		elif coordX >= 175 and coordX < 200: pos=9
		elif coordX >= 200 and coordX < 225: pos=10
		elif coordX >= 225 and coordX < 250: pos=11
		elif coordX >= 250 and coordX < 275: pos=12
		elif coordX >= 275 and coordX <= 300:pos=13
		elif coordX >= 325 and coordX < 350: pos=14
		elif coordX >= 350 and coordX < 375: pos=15
		elif coordX >= 375 and coordX < 400: pos=16
		elif coordX >= 400 and coordX < 425: pos=17
		elif coordX >= 425 and coordX < 450: pos=18
		elif coordX >= 450 and coordX < 475: pos=19
		elif coordX >= 475 and coordX < 500: pos=20
		elif coordX >= 500 and coordX < 525: pos=21
		elif coordX >= 525 and coordX < 550: pos=22
		elif coordX >= 550 and coordX < 575: pos=23
		elif coordX >= 575 and coordX <= 600:pos=24
		elif coordX >= 625 and coordX < 650: pos=25
		elif coordX >= 650 and coordX < 675: pos=26
		elif coordX >= 675 and coordX < 700: pos=27
		elif coordX >= 700 and coordX < 725: pos=28
		elif coordX >= 725 and coordX < 750: pos=29
		elif coordX >= 750 and coordX < 775: pos=30
		elif coordX >= 775 and coordX < 800: pos=31
		elif coordX >= 800 and coordX < 825: pos=32
		elif coordX >= 825 and coordX < 850: pos=33
		elif coordX >= 850 and coordX < 875: pos=34
		elif coordX >= 875 and coordX <= 900:pos=35
	elif coordY >= 325 and coordY <= 375:
		if coordX >= 25 and coordX < 75:     pos=36
		elif coordX >= 75 and coordX < 125:  pos=37
		elif coordX >= 125 and coordX < 175: pos=38
		elif coordX >= 175 and coordX < 225: pos=39
		elif coordX >= 225 and coordX <= 275:pos=40
		elif coordX >= 325 and coordX < 375: pos=41
		elif coordX >= 375 and coordX < 425: pos=42
		elif coordX >= 425 and coordX < 475: pos=43
		elif coordX >= 475 and coordX < 525: pos=44
		elif coordX >= 525 and coordX <= 575:pos=45
		elif coordX >= 625 and coordX < 675: pos=46
		elif coordX >= 675 and coordX < 725: pos=47
		elif coordX >= 725 and coordX < 775: pos=48
		elif coordX >= 775 and coordX < 825: pos=49
		elif coordX >= 825 and coordX <= 875:pos=50
	elif coordY >= 450 and coordY <= 500:
		if coordX >= 75 and coordX < 125:    pos=51
		elif coordX >= 125 and coordX < 175: pos=52
		elif coordX >= 175 and coordX < 225: pos=53
		elif coordX >= 225 and coordX < 275: pos=54
		elif coordX >= 275 and coordX < 325: pos=55
		elif coordX >= 325 and coordX < 375: pos=56
		elif coordX >= 375 and coordX < 425: pos=57
		elif coordX >= 425 and coordX < 475: pos=58
		elif coordX >= 475 and coordX < 525: pos=59
		elif coordX >= 525 and coordX < 575: pos=60
		elif coordX >= 575 and coordX < 625: pos=61
		elif coordX >= 625 and coordX < 675: pos=62
		elif coordX >= 675 and coordX < 725: pos=63
		elif coordX >= 725 and coordX < 775: pos=64
		elif coordX >= 775 and coordX <= 825:pos=65
	elif coordY >= 550 and coordY <=575:
		if coordX >= 50 and coordX < 75:     pos=66
		elif coordX >= 75 and coordX < 100:  pos=67
		elif coordX >= 100 and coordX < 125: pos=68
		elif coordX >= 125 and coordX < 150: pos=69
		elif coordX >= 150 and coordX < 175: pos=70
		elif coordX >= 175 and coordX < 200: pos=71
		elif coordX >= 200 and coordX < 225: pos=72
		elif coordX >= 225 and coordX < 250: pos=73
		elif coordX >= 250 and coordX < 275: pos=74
		elif coordX >= 275 and coordX < 300: pos=75
		elif coordX >= 300 and coordX < 325: pos=76	
		elif coordX >= 325 and coordX < 350: pos=77
		elif coordX >= 350 and coordX < 375: pos=78
		elif coordX >= 375 and coordX < 400: pos=79
		elif coordX >= 400 and coordX < 425: pos=80
		elif coordX >= 425 and coordX < 450: pos=81
		elif coordX >= 450 and coordX < 475: pos=82
		elif coordX >= 475 and coordX < 500: pos=83
		elif coordX >= 500 and coordX < 525: pos=84
		elif coordX >= 525 and coordX < 550: pos=85
		elif coordX >= 550 and coordX < 575: pos=86
		elif coordX >= 575 and coordX < 600: pos=87
		elif coordX >= 600 and coordX < 625: pos=88
		elif coordX >= 625 and coordX < 650: pos=89
		elif coordX >= 650 and coordX < 675: pos=90
		elif coordX >= 675 and coordX < 700: pos=91
		elif coordX >= 700 and coordX < 725: pos=92
		elif coordX >= 725 and coordX < 750: pos=93
		elif coordX >= 750 and coordX < 775: pos=94
		elif coordX >= 775 and coordX < 800: pos=95
		elif coordX >= 800 and coordX < 825: pos=96
		elif coordX >= 825 and coordX < 850: pos=97
		elif coordX >= 850 and coordX <= 875:pos=98
	indice[0]=pos	
	
			
			
		
		
