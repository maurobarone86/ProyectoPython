#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este juego fue creado por Barone Mauro César
"""
#importaciones
import pygame,sys,os,random,time,copy,json,os.path,datetime,time,platform,logging,Menú

from pygame.locals import *
from Data.Dibujos import Dibujo
from Data.Imagen import Imagen2
from Data.Imagen import cuadrante
from Data.Proporcional import proporcional2
from Data.Restructurar import restructurar2
from Data.Ubicacion import ubicacion2
from Data.InicializadoAcomodo import inicializadoAcomodo
from Data.Identificacion import identificacion
from Data.Repeticiones import repeticiones
from Data.CargaPuntaje import cargarPuntaje
def juego():
	#Inicializaciones
	pygame.init()
	#area de variables y constantes
	nomJuego= 'Acomodo y Formo'
	puntosObtenidos= 0
	anchoTotal= 700
	largoTotal= 925
	Reloj= pygame.time.Clock()
	areaTotal = (largoTotal,anchoTotal)
	Coordenadas_cuadrantes= [(50,50),(350,50),(650,50),(25,275),(50,275),(75,275),(100,275),(125,275),(150,275),(175,275),(200,275),(225,275),(250,275),(275,275),(325,275),(350,275),(375,275),(400,275),(425,275),(450,275),(475,275),(500,275),(525,275),(550,275),(575,275),(625,275),(650,275),(675,275),(700,275),(725,275),(750,275),(775,275),(800,275),(825,275),(850,275),(875,275),(25,325),(75,325),(125,325),(175,325),(225,325),(325,325),(375,325),(425,325),(475,325),(525,325),(625,325),(675,325),(725,325),(775,325),(825,325),(75,450),(125,450),(175,450),(225,450),(275,450),(325,450),(375,450),(425,450),(475,450),(525,450),(575,450),(625,450),(675,450),(725,450),(775,450),(50,550),(75,550),(100,550),(125,550),(150,550),(175,550),(200,550),(225,550),(250,550),(275,550),(300,550),(325,550),(350,550),(375,550),(400,550),(425,550),(450,550),(475,550),(500,550),(525,550),(550,550),(575,550),(600,550),(625,550),(650,550),(675,550),(700,550),(725,550),(750,550),(775,550),(800,550),(825,550),(850,550)]
	list_cuad=[range(3),range(3,14),range(14,25),range(25,36),range(36,41),range(41,46),range(46,51),range(51,66),range(66,99)]
	list_coord=[[],[],[],[],[],[],[],[],[]]
	indice=0
	#Genero la lista de cuadrantes para ser usado en la inicializacion principal
	for i in list_cuad:
		for y in i:
			list_coord[indice].extend([[Coordenadas_cuadrantes[y]]])
		indice+=1
	ventana = pygame.display.set_mode((areaTotal))
	fuente_elegida = pygame.font.SysFont('nanumbarungothic', 40)
	pygame.display.set_caption(' A  C  O  M  O  D  O    Y    F  O  R  M  O')
	fondo = pygame.draw.rect(ventana,(0, 0, 0),(0,0,largoTotal,anchoTotal),0)
	ruta = os.getcwd()
	os.chdir(ruta)
	carp_imagenes = ruta+'/Data/Imagenes/'
	carp_letras = ruta+'/Data/Letras/'
	carp_silabas = ruta+'/Data/Silabas/'
	#Se levantan los datos desde los archivos json
	Imagen1=open('Data/ListaDeImagenes2.txt','r')
	Silabas1=open('Data/ListaDeSilabas2.txt','r')
	Letra1=open('Data/ListaDeLetras2.txt','r')
	datos1=json.load(Imagen1)
	datos2=json.load(Silabas1)
	datos3=json.load(Letra1)
	Imagen1.close()
	Silabas1.close()
	Letra1.close()
	lista_imagenes = datos1['I']
	lista_silabas = datos2['S']
	lista_letras = datos3['L']
	imagenes_elegidas = []
	imagenes_Totales=[]
	#Se crean las imagenes con la lista de letras y silabas en su correcto orden
	for y in lista_imagenes:
		imagen = y
		_dir = carp_imagenes+imagen
		nomImagen =imagen[0:imagen.index('.')].capitalize()
		lista = list(filter(lambda cadena:nomImagen.find(cadena[0:cadena.index('.')])>=0,lista_silabas))
		lista1=[]
		lista3 = [0,0,0,0,0,0,0,0,0,0,0]
		for i in lista:
			indice = nomImagen.find(i[0:i.index('.')])
			lista3[indice] = i
		rep = lista3.count(0)
		for i in range(0,rep):
			lista3.remove(0)
		if nomImagen == 'Termómetro':
			del lista3[len(lista3)-1]
		if nomImagen == 'Lámpara':
			lista3[0]='Lám.png'
		if nomImagen == 'Lombriz':
			lista3[1]='briz.png'
		for i in nomImagen:
			ref = i+'.png'
			if ref in lista_letras:
				lista1.extend([ref])
		dib = Dibujo(lista1,lista3,carp_imagenes,carp_letras,carp_silabas,nomImagen)
		imagenes_Totales.extend([dib])
	pres = False
	fuente_elegida = pygame.font.SysFont('nanumbarungothic', 40)
	muyBien = fuente_elegida.render("¡Muy Bien!", True, pygame.Color("red"))
	muyBien_rect = muyBien.get_rect()
	muyBien_rect.centerx = ventana.get_rect().centerx
	cartelSeleccion = fuente_elegida.render("S e l e c c i o n e   c o n   q u e   v a   a   j u g a r", True, pygame.Color("black"))
	cartelSeleccion_rect = cartelSeleccion.get_rect()
	cartelOpcionSilabas= fuente_elegida.render("S i l a b a s", True, pygame.Color("blue"))
	cartelOpcionSilabas_rect=cartelOpcionSilabas.get_rect()
	cartelOpcionLetras= fuente_elegida.render("L e t r a s", True, pygame.Color("red"))
	cartelOpcionLetras_rect=cartelOpcionLetras.get_rect()
	bucle=True
	fondo1 = pygame.draw.rect(ventana,(205,255,200),(0,0,largoTotal,anchoTotal),0)
	ventana.blit(cartelSeleccion,(50,100))
	rec = pygame.draw.rect(ventana,(0,0,0),(100,300,192,40),1)
	rec1 = pygame.draw.rect(ventana,(0,0,0),(550,300,165,40),1)
	ventana.blit(cartelOpcionSilabas,(100,300))
	ventana.blit(cartelOpcionLetras,(550,300))
	pygame.display.flip()
	#Se muestra el menu de eleccion de silaba o letra
	while bucle:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					pygame.display.set_mode((300, 550))
					Menú.juego()
			if event.type == MOUSEBUTTONDOWN:
				X = event.pos[0]
				Y = event.pos[1]
				if X >=100 and X<=292 and Y >=300 and Y <=340:
					opcion='S'
					bucle=False
				elif X >=550 and X<=715 and Y >=300 and Y <=340:
					opcion='L'
					bucle=False
			if bucle == False:
				pygame.mixer.Sound('Data/Sonidos/124912__greencouch__ploep5.aiff').play()
				Reloj.tick(5)
	#Eleccion de imagenes
	elegidos= random.sample(imagenes_Totales,3)
	#Inicializado
	activos = inicializadoAcomodo(elegidos,list_coord,Coordenadas_cuadrantes,opcion)
	ubicados=[]
	#Presentacion
	restructurar2(opcion,activos,ventana,largoTotal,anchoTotal,Coordenadas_cuadrantes,elegidos,ubicados)
	indice1=[]
	indice1.extend([None])
	indice2=[]
	indice2.extend([None])
	ubicados=[]
	obj1=None
	pygame.display.flip()
	while True:
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
					juego()
			if event.type == MOUSEMOTION:
				#Si se detecta el boton atretado
				if pres:
					if obj1 in activos:
						#Se muestran todos los objetos activos menos el que es arrastrado
						restructurar2(opcion,activos,ventana,largoTotal,anchoTotal,Coordenadas_cuadrantes,elegidos,ubicados,obj1)
						ventana.blit(obj1.imagen,(event.pos[0]-15,event.pos[1]-15))
				else:
					#Si se suelta el boton en un area no valida o no se arrastra 
					restructurar2(opcion,activos,ventana,largoTotal,anchoTotal,Coordenadas_cuadrantes,elegidos,ubicados)
			if event.type == MOUSEBUTTONUP:
				pres=False
				#chequeo que el arrastre sea de la posicion inicial a la posicion final valida
				ubicacion2(event.pos[0],event.pos[1],indice2)
				if indice2[0] != None and obj1 != None:
					obj=repeticiones(Coordenadas_cuadrantes,activos,indice2[0],obj1)
					if obj != None and Coordenadas_cuadrantes.index(obj.posFinal) == indice2[0]:
						#Si es correcto ingreso ubicados y egreso en activos
						puntosObtenidos+=1
						pygame.mixer.Sound('Data/Sonidos' + os.path.sep +'124912__greencouch__ploep5.aiff').play()
						Reloj.tick(5)
						activos.remove(obj)
						obj.posIni = obj.posFinal
						ubicados.extend([obj])
						restructurar2(opcion,activos,ventana,largoTotal,anchoTotal,Coordenadas_cuadrantes,elegidos,ubicados)
						obj=None
						obj1=None
			if event.type == MOUSEBUTTONDOWN:
				#si se mantine presionado sobre una imagen activa se la identifica y comienza el arrastre
				pres=False
				pygame.event.clear()
				obj1=None
				ubicacion2(event.pos[0],event.pos[1],indice1)
				obj1 = identificacion(indice1[0],activos,Coordenadas_cuadrantes)
				if obj1 in activos:
					pres = True
			if activos==[]:
				ventana.blit(muyBien,muyBien_rect)
				pygame.display.update()
				time.sleep(2)
				#se renuevan las imagenes activas, se inicializa y se vuelve a elegir
				elegidos= random.sample(imagenes_Totales,3)
				activos = inicializadoAcomodo(elegidos,list_coord,Coordenadas_cuadrantes,opcion)
				ubicados=[]
				restructurar2(opcion,activos,ventana,largoTotal,anchoTotal,Coordenadas_cuadrantes,elegidos,ubicados)		
			pygame.display.flip()	
def main(args):
	juego()
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))		

	
	

