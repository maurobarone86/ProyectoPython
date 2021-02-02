#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este juego fue creado por Scotto Laura Sofia
"""
# Importaciones
import pygame, sys, os, random, bisect, copy, json, time,platform,logging,Menú, unicodedata
from random import shuffle
from pygame.locals import *
from Data.ProporcionalCUESL import proporcional
from Data.CargaPuntaje import cargarPuntaje

# import pdb; pdb.set_trace()

# Inicializaciones
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
pygame.init()

# Paleta de colores
colores = {'violetaOscuro': (81, 45, 168), 'lila': (209, 196, 233), 'violeta': (103, 58, 183),
           'blanco': (255, 255, 255), 'cian': (0, 188, 212), 'casiNegro': (33, 33, 33), 'grisOscuro': (117, 117, 117),
           'gris': (189, 189, 189)}

# Inicializar pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption('EL ENTROMETIDO')

# Rellenar fondo
fondo = pygame.Surface((800, 500))
fondo.fill(colores['violeta'])
fondo_titulo = pygame.Surface((800, 100))
fondo_titulo.fill(colores['violetaOscuro'])
pantalla.blit(fondo, (0, 100))
pygame.display.flip()

# Variables
nomJuego = 'El Entrometido'
puntosObtenidos = 0
seisImagenes = []
lisImGuia=[None]
rectObj = [None]
lisTacho=[None]
verificador = [False, False,False,False,False,False]


class Imagen(pygame.sprite.Sprite):
	def __init__(self, palabra):
		super(Imagen, self).__init__()
		if proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + palabra + '.png'),100).get_alpha() is None:
			self.imagen = proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + palabra + '.png'),100).convert()
		else:
			self.imagen = proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + palabra + '.png'),100).convert_alpha()
		self.palabra = palabra
		self.imagen.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.imagen.get_rect()
		self.sonido = pygame.mixer.Sound('Data/Sonidos' + os.path.sep + palabra + '.ogg')
		self.inicial = self.palabra[0].lower()
		self.click = False
		self.pos = None
		self.correcto = False
	
	def proporcional_guiaImagen(self,valor):
		if proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + self.palabra + '.png'),valor).get_alpha() is None:
			self.imagen = proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + self.palabra + '.png'),valor).convert()
		else:
			self.imagen = proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + self.palabra + '.png'),valor).convert_alpha()
	
	def reproducir(self):
		self.sonido.play()
		
	def set_pos(self, x, y):
		'''
			Modifica la posicion
		'''
		self.pos = (x, y)
		
	def update(self, pantalla_base, rectObj, tacho):
		'''
		    Modifica la pantalla segun el movimiento del mouse,
		    o si se ubico correctamente
		'''
		cuadrado_violeta = pygame.Surface((100,100)).convert()
		cuadrado_violeta.fill(colores['violeta'])
		if self.click and not self.correcto:
			self.rect.center = pygame.mouse.get_pos()
			pantalla.blit(pantalla_base,(0,0))
			pantalla.blit(cuadrado_violeta,(self.pos[0],self.pos[1]))
			pantalla.blit(self.imagen,self.rect)
		else:
			if self.rect.colliderect(rectObj):
				if rectObj.collidepoint(pygame.mouse.get_pos()) and tacho.inicial != self.inicial:
					pantalla.blit(cuadrado_violeta,(self.pos[0],self.pos[1]))
					pantalla_base.blit(pantalla,(0,0))
					self.correcto=True
				elif rectObj.collidepoint(pygame.mouse.get_pos()) and tacho.inicial == self.inicial:
					incorrecto()


class Objetivo(pygame.sprite.Sprite):
	def __init__(self, inicial):
		super(Objetivo, self).__init__()
		self.inicial = inicial
		if proporcional(pygame.image.load('Data/Imagenes'+ os.path.sep +'tacho.png'),150).get_alpha() is None:
			self.imagen = proporcional(pygame.image.load('Data/Imagenes'+ os.path.sep +'tacho.png'),150).convert()
		else:
			self.imagen = proporcional(pygame.image.load('Data/Imagenes'+ os.path.sep +'tacho.png'),150).convert_alpha()
		self.imagen.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.imagen.get_rect()
		
	def move_rect(self,x,y):
		'''
			Mueve el rectangulo al punto x,y
		'''
		self.rect.move_ip(x,y)


class ImagenTexto(pygame.sprite.Sprite):
	def __init__(self):
		super(ImagenTexto, self).__init__()
		if pygame.image.load('Data/Imagenes'+ os.path.sep +'texto.png').get_alpha() is None:
			self.imagen = pygame.image.load('Data/Imagenes'+ os.path.sep +'texto.png').convert()
		else:
			self.imagen = pygame.image.load('Data/Imagenes'+ os.path.sep +'texto.png').convert_alpha()
		self.imagen.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.imagen.get_rect()


def titulo_juego():
    """Coloco título del juego"""
    fuente = pygame.font.Font("Data/tipografias" + os.path.sep + 'Barrio.ttf', 50)
    titulo = fuente.render(" EL ENTROMETIDO ", True, colores['lila'])
    titulo_rect = titulo.get_rect()
    titulo_rect.centerx = fondo_titulo.get_rect().centerx
    titulo_rect.centery = fondo_titulo.get_rect().centery
    fondo_titulo.blit(titulo, titulo_rect)
    pantalla.blit(fondo_titulo, (0, 0))
    pygame.display.flip()


def guardar_palabras():
    """ Funciòn que genera un archivo con la informacion de las imagenes a usar """
    palabras = ['abeja', 'auto', 'ave', 'avión', 'billetera', 'bota', 'café', 'calculadora', 'campana',
                'elefante', 'erizo', 'escalera', 'espejo', 'estrella', 'faro', 'flor', 'fuego', 'guantes',
                'hamburguesa', 'iglesia', 'igloo', 'iguana', 'imán', 'indio', 'lámpara', 'lápiz', 'lluvia', 'lombriz',
                'mariposa', 'mochila', 'moneda', 'nube', 'ojo', 'olla', 'oreja', 'oso', 'oveja', 'pasto', 'reloj',
                'rodillo', 'sillón', 'termómetro', 'tijera', 'torta', 'unicornio', 'urna', 'uvas']
    archivo = open("Data/palabras.txt", "w")
    json.dump(palabras, archivo)
    archivo.close()
    return palabras


def cargar_palabras():
    archivo = open("Data/palabras.txt", "r")
    palabras = json.load(archivo)
    archivo.close()
    return palabras
    
def cargar_palabrasGuia():
	archivo = open('Data/palabrasEntrometido.txt','r')
	palabrasGuia = json.load(archivo)
	archivo.close()
	return palabrasGuia

def seleccionar_palabra(palabras):
    sel = random.randrange(len(palabras))
    palsel = palabras[sel]
    del palabras[sel]
    return palsel

def tablero(palabras,palabrasGuia):
	"""Armo el tablero del juego"""
	# Inicio con el texto
	textoImagen = ImagenTexto()
	fondo.blit(textoImagen.imagen, (50, 50))
	pantalla.blit(fondo, (0, 100))
	# Sigo con la imagen guía
	cuadrado_violeta150 = pygame.Surface((150,150)).convert()
	cuadrado_violeta150.fill(colores['violeta'])
	letraGuia = random.choice(list(palabrasGuia))
	f = random.choice(palabrasGuia[letraGuia])
	palabrasGuia[letraGuia].remove(f)
	palabras.remove(f)
	nomGuiaImagen = f
	guiaImagen = Imagen(nomGuiaImagen)
	guiaImagen.proporcional_guiaImagen(150)
	lisImGuia[0]=guiaImagen
	fondo.blit(cuadrado_violeta150, (50, 300))
	fondo.blit(guiaImagen.imagen, (50, 300))
	pantalla.blit(fondo, (0, 100))
	# Sigo con las imágenes random
	cuadrado_violeta = pygame.Surface((100, 100)).convert()
	cuadrado_violeta.fill(colores['violeta'])
	if seisImagenes:
		del seisImagenes[:]
	for i in range(3):
		mismaLetra = random.choice(palabrasGuia[letraGuia])
		palabrasGuia[letraGuia].remove(mismaLetra)
		palabras.remove(mismaLetra)
		imml = Imagen(mismaLetra)
		seisImagenes.append(imml)
	cont = 0
	while cont != 3:
		distintaLetra = seleccionar_palabra(palabras)
		imdl = Imagen(distintaLetra)
		if imdl.inicial != guiaImagen.inicial:
			seisImagenes.append(imdl)
			cont += 1
	x = 500
	y = 50
	shuffle(seisImagenes)
	for a in seisImagenes:
		if a.inicial != guiaImagen.inicial:
			verificador[seisImagenes.index(a)] = True
	for a in seisImagenes:
		fondo.blit(cuadrado_violeta, (x, y))
		a.set_pos(x,y+100)
		fondo.blit(a.imagen, (x, y))
		pantalla.blit(fondo, (0, 100))
		if x == 500:
			x = 650
		elif x == 650:
			x=500
			y+=150
	# Termino con la imagen del tacho (la única que tiene Objetivo)
	tacho = Objetivo(nomGuiaImagen[0])
	tacho.move_rect(300,400)
	lisTacho[0]=tacho
	rectObj[0]=tacho.rect
	fondo.blit(tacho.imagen,(300, 300))
	pantalla.blit(fondo, (0, 100))
	
	copia = pantalla.copy()
	pygame.display.flip()
	return copia


def click_error(pantalla_base):
    fuente = pygame.font.Font('Data/tipografias' + os.path.sep + 'CaveatBrush.ttf', 40)
    mensaje = fuente.render('Arrastrá las imagenes intrusas al tacho', True, colores['cian'])
    mensaje_rect = mensaje.get_rect()
    mensaje_rect.centerx = fondo.get_rect().centerx
    mensaje_rect = mensaje_rect.move(0, 100)
    pantalla_base.blit(mensaje, mensaje_rect)
    pantalla.blit(pantalla_base, (0, 0))
    pygame.display.flip()
    return True


def rearmar(seisImagenes, verificador):
	fondo = pygame.Surface((800, 500))
	fondo.fill(colores['violeta'])
	fondo_titulo = pygame.Surface((800, 100))
	fondo_titulo.fill(colores['violetaOscuro'])
	pantalla.blit(fondo, (0, 100))
	pygame.display.flip()
	del seisImagenes[:]
	for i in verificador:
		i = False
	titulo_juego()
#	if not os.path.isfile("palabras.txt"):
	guardar_palabras()
	palabras = cargar_palabras()
	palabrasGuia = cargar_palabrasGuia()
	tablero(palabras,palabrasGuia)


def correcto():
    fuente = pygame.font.Font('Data/tipografias' + os.path.sep + 'CaveatBrush.ttf', 40)
    mensaje = fuente.render('¡Muy bien!', True, colores['cian'])
    mensaje_rect = mensaje.get_rect()
    mensaje_rect.centerx = fondo.get_rect().centerx
    mensaje_rect = mensaje_rect.move(0, 100)
    pantalla.blit(mensaje, mensaje_rect)
    pygame.display.flip()
    time.sleep(1)
    #pygame.quit()
    #sys.exit()


def incorrecto():
    fuente = pygame.font.Font('Data/tipografias' + os.path.sep + 'CaveatBrush.ttf', 40)
    mensaje = fuente.render('¡Te equivocaste!', True, colores['cian'])
    mensaje_rect = mensaje.get_rect()
    mensaje_rect.centerx = fondo.get_rect().centerx
    mensaje_rect = mensaje_rect.move(0, 100)
    pantalla.blit(mensaje, mensaje_rect)
    pygame.display.flip()
    time.sleep(1)
    cuadrado_violeta = pygame.Surface((800, 50)).convert()
    cuadrado_violeta.fill(colores['violeta'])
    pantalla.blit(cuadrado_violeta, (0, 100))


def juego():
	'''
		comienzo del juego
	'''
	global nomJuego
	global puntosObtenidos
	titulo_juego()
	if not os.path.isfile("Data/palabras.txt"):
		guardar_palabras()
	palabras = cargar_palabras()
	palabrasGuia = cargar_palabrasGuia()
	pantalla_base = tablero(palabras,palabrasGuia)
	col = 0
	fila = 0
	fila_IG=0
	col_IG=0
	c_e = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				if puntosObtenidos > 0:
					puntaje = [nomJuego,puntosObtenidos]
					cargarPuntaje(puntaje)
				pygame.quit()
				sys.exit()
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					if puntosObtenidos > 0:
						puntaje = [nomJuego,puntosObtenidos]
						cargarPuntaje(puntaje)
					pygame.display.set_mode((300, 550))
					Menú.juego()
			else:
				filas = [150, 250, 300, 400, 450, 550]#1 3 5
				columnas = [500, 600, 650, 750]#1 3
				filas_IG = [400,550]
				columnas_IG = [50,200]
				if event.type == pygame.MOUSEBUTTONDOWN:
					fila = bisect.bisect(filas,event.pos[1])
					col = bisect.bisect(columnas, event.pos[0])
					fila_IG =bisect.bisect(filas_IG,event.pos[1])
					col_IG =bisect.bisect(columnas_IG, event.pos[0])
					if fila == 0 or fila == 2 or fila == 4 or fila == 6 or col == 0 or col == 2 or col == 4:
						if fila_IG == 0 or fila_IG == 2 or col_IG == 0 or fila_IG == 2:
							c_e= click_error(pantalla_base)
					else:
						cuadrado_violeta = pygame.Surface((800, 50)).convert()
						cuadrado_violeta.fill(colores['violeta'])
						pantalla_base.blit(cuadrado_violeta, (0, 100))
						c_e = False
						if col == 1:
							if fila == 1:
								seisImagenes[0].click=True
							elif fila == 3:
								seisImagenes[2].click = True
							elif fila == 5:
								seisImagenes[4].click = True
						elif col == 3:
							if fila == 1:
								seisImagenes[1].click=True
							elif fila == 3:
								seisImagenes[3].click = True
							elif fila == 5:
								seisImagenes[5].click = True
					if fila_IG == 1 and col_IG == 1:
						lisImGuia[0].reproducir()
				elif event.type == pygame.MOUSEBUTTONUP:
					filaup = bisect.bisect(filas,event.pos[1])
					colup = bisect.bisect(columnas, event.pos[0])
					if not c_e:
						pantalla.blit(pantalla_base, (0, 0))  # devuelve las palabras a su lugar en caso erroneo. pb2 se va actualizando.
						if colup == 1:
							if filaup == 1:
								seisImagenes[0].reproducir()
							elif filaup == 3:
								seisImagenes[2].reproducir()
							elif filaup == 5:
								seisImagenes[4].reproducir()
						elif colup == 3:
							if filaup == 1:
								seisImagenes[1].reproducir()
							elif filaup == 3:
								seisImagenes[3].reproducir()
							elif filaup == 5:
								seisImagenes[5].reproducir()
					else:
						click_error(pantalla_base)
					for i in seisImagenes:
						i.click = False
		if col == 1:
			if fila == 1:
				seisImagenes[0].update(pantalla_base, rectObj[0], lisTacho[0])
				if seisImagenes[0].correcto:
					verificador[0]=False
			elif fila == 3:
				seisImagenes[2].update(pantalla_base, rectObj[0], lisTacho[0])
				if seisImagenes[2].correcto:
					verificador[2]=False
			elif fila == 5:
				seisImagenes[4].update(pantalla_base, rectObj[0], lisTacho[0])
				if seisImagenes[4].correcto:
					verificador[4]=False
		elif col == 3:
			if fila == 1:
				seisImagenes[1].update(pantalla_base, rectObj[0], lisTacho[0])
				if seisImagenes[1].correcto:
					verificador[1]=False
			elif fila == 3:
				seisImagenes[3].update(pantalla_base, rectObj[0], lisTacho[0])
				if seisImagenes[3].correcto:
					verificador[3]=False
			elif fila == 5:
				seisImagenes[5].update(pantalla_base, rectObj[0], lisTacho[0])
				if seisImagenes[5].correcto:
					verificador[5]=False
		if not True in verificador:
			correcto()
			puntosObtenidos += 6
			rearmar(seisImagenes,verificador)
			pantalla_base = pantalla.copy()
			col = 0
			fila = 0
			col_IG=0
			fila_IG=0
			c_e = False
		pygame.display.update()


def main(args):
    juego()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
