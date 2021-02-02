#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este juego fue creado por Barone Mauro César
"""
#importaciones
import pygame,sys,os,random,time,copy,json,os.path,datetime,time,platform,logging,Menú
from pygame.locals import *
from Data.Letra import Letra
from Data.Imagen import Imagen
from Data.Elegir import elegir
from Data.Inicializar import Inicializar
from Data.Seleccion import seleccion
from Data.Proporcional import proporcional2
from Data.Restructurar import restructurar
from Data.Ubicacion import ubicacion
from Data.CargaPuntaje import cargarPuntaje
def juego():
	#Inicializaciones
	pygame.mixer.pre_init(44100,-16,2,1024)
	pygame.mixer.init()
	pygame.init()
	#area de variables y constantes
	nomJuego= 'Come Vocales'
	puntosObtenidos= 0
	anchoTotal= 600
	largoTotal= 800
	lista_comb= [[0,6,0],[0,0,6],[6,0,0],[5,1,0],[5,0,1],[4,1,1],[4,2,0],[4,0,2],[3,2,1],[3,1,2],[3,0,3],[3,3,0],[2,2,2],[2,1,3],[2,3,1],[2,4,0],[2,0,4],[1,5,0],[1,0,5],[1,3,2],[1,2,3],[1,4,1],[1,1,4]]
	areaTotal = (largoTotal,anchoTotal)
	p= [(100,75),(325,425),(550,75),(100,425),(325,75),(550,425),(250,250),(350,250),(450,250)]
	ventana = pygame.display.set_mode((areaTotal))
	fuente_elegida = pygame.font.SysFont('nanumbarungothic', 40)
	muyBien = fuente_elegida.render("¡Muy Bien!", True, pygame.Color("red"))
	teEquivocaste = fuente_elegida.render("¡Te Equivocaste!", True, pygame.Color("red"))
	muyBien_rect = muyBien.get_rect()
	muyBien_rect.centerx = ventana.get_rect().centerx
	teEquivocaste_rect = teEquivocaste.get_rect()
	teEquivocaste_rect.centerx = ventana.get_rect().centerx
	pygame.display.set_caption('   C  O  M  E     V  O  C  A  L  E  S')
	Reloj= pygame.time.Clock()
	fondo = pygame.draw.rect(ventana,(255, 255, 255),(0,0,largoTotal,anchoTotal),0)
	ruta = os.getcwd()
	os.chdir(ruta)
	carp_imagenes = ruta+'/Data/Imagenes'
	carp_letras = ruta+'/Data/Letras'
	carp_sonidos = ruta+'/Data/Sonidos'
	#Se levantan los datos desde los archivos json
	Imagen1=open('Data/ListaDeImagenes.txt','r')
	Sonido1=open('Data/ListaDeSonidos.txt','r')
	Letra1=open('Data/ListaDeLetras.txt','r')
	datos1=json.load(Imagen1)
	datos2=json.load(Sonido1)
	datos3=json.load(Letra1)
	Imagen1.close()
	Sonido1.close()
	Letra1.close()
	lista_imagenes = datos1['I']
	lista_sonidos = datos2['S']
	lista_letras = datos3['L']
	imagenes_activas = []
	letras_elegidas = []
	posible = []
	posible.extend([True])
	pres = False
	# Se generan las letras, se levantan los datos y se forman las letras
	indice=0
	for i in lista_letras:
		vocal= i[0].lower()
		lista = list(filter(lambda _dir: _dir[0] == vocal, lista_imagenes))
		lista_letras[indice] = Letra(vocal.upper(),carp_letras+'/'+i,lista,carp_imagenes,carp_sonidos)
		indice+=1
	# Se seleccionan las imagenes y las letras 
	elegidas =  seleccion(lista_letras,letras_elegidas,imagenes_activas,posible,lista_comb,p)
	# se muetran en la pantalla
	restructurar(imagenes_activas,elegidas,ventana)
	pygame.display.flip()
	obj1=None
	#Bucle principal del juego
	while True and posible[0]:
		for event in pygame.event.get():
			if event.type == QUIT:
				if puntosObtenidos > 0:
					puntaje=[nomJuego,puntosObtenidos]
					cargarPuntaje(puntaje)
				pygame.quit()
				sys.exit()
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					if puntosObtenidos > 0:
						puntaje=[nomJuego,puntosObtenidos]
						cargarPuntaje(puntaje)
					pygame.display.set_mode((300, 550))
					Menú.juego()
			if event.type == MOUSEMOTION:
				if pres:
					#Mientras el boton es presionado se capturan las movimientos del mouse y se
					#arrastra la imagen
					restructurar(imagenes_activas,elegidas,ventana,obj1)
					ventana.blit(obj1.imagen,(event.pos[0]-25,event.pos[1]-25))
			if event.type == MOUSEBUTTONUP:
				pres = False
				posicion2=[]
				obj2 = ubicacion(event.pos[0],event.pos[1],elegidas,imagenes_activas)
				if obj2 in imagenes_activas:
					#si se hace clik sobre un imagen se activa el sonido
					obj2.ReproducirSonido(Reloj)
				posicion3=[]
				obj = ubicacion(event.pos[0],event.pos[1],elegidas,imagenes_activas)
				if (obj1 in imagenes_activas) and (obj in elegidas):
					#Si se suelta la imagen sobre la vocal indicada se chequea la colision entre
					#la imagen capturada y la vocal y ademas tiene que estar en el grupo de colision
					listaColisiones = pygame.sprite.spritecollide(obj1, obj.grupo_Sprite, False)
					if obj1 in listaColisiones and obj.spriteLetra in listaColisiones:
						#Una vez detectada la colision apropiada
						puntosObtenidos+=1
						pygame.mixer.Sound('Data/Sonidos' + os.path.sep +'124912__greencouch__ploep5.aiff').play()
						Reloj.tick(5)
						imagenes_activas.remove(obj1)
						obj.removerDelGrupo(obj1)
					else:
						ventana.blit(teEquivocaste,teEquivocaste_rect)
						pygame.display.flip()
						time.sleep(2)
						#se mantiene el cartel por 2 segundos
				#sea que se obtuvo el resutado o no se restructura las imagenes
				restructurar(imagenes_activas,elegidas,ventana)
			if event.type == MOUSEBUTTONDOWN:
				posicion1=[]
				obj1 = ubicacion(event.pos[0],event.pos[1],elegidas,imagenes_activas)
				if obj1 in imagenes_activas:
					#Si el boton del mouse fue presionando sobre una de las imagenes se captura la misma
					pres = True
			if imagenes_activas==[]:
				ventana.blit(muyBien,muyBien_rect)
				pygame.display.update()
				time.sleep(2)
				#se renuevan las imagenes activas, se inicializa y se vuelve a elegir
				Inicializar(lista_letras)
				elegidas =  seleccion(lista_letras,letras_elegidas,imagenes_activas,posible,lista_comb,p)
				restructurar(imagenes_activas,elegidas,ventana)		
			pygame.display.flip()	
def main(args):
	juego()
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))       

				        
        
            
            







