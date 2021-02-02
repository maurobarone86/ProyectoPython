#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este juego fue creado por Scotto Laura Sofia
"""
import pygame, os, sys, random, bisect, json, time,platform,logging,Menú
from pygame.locals import *
from Data.CargaPuntaje import cargarPuntaje
from Data.ProporcionalCUESL import proporcional

pygame.init()
pygame.event.pump()
pygame.mixer.pre_init(44100, -16, 2, 1024)


class Imagen(pygame.sprite.Sprite):
    '''
		Inicializa una imagen especifica con la palabra pasada
	'''

    def __init__(self, palabra):
        super(Imagen, self).__init__()
        self.palabra = palabra
        if proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + palabra + '.png'),200).get_alpha() == None:
            self.imagen = proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + palabra + '.png'),200).convert()
        else:
            self.imagen = proporcional(pygame.image.load('Data/Imagenes' + os.path.sep + palabra + '.png'),200).convert_alpha()
        self.imagen.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.imagen.get_rect()
        self.sonido = pygame.mixer.Sound('Data/Sonidos' + os.path.sep + palabra + '.ogg')

    def reproducir(self):
        '''
			Reproduce el sonido de la imagen
		'''
        self.sonido.play()


class Objetivo(pygame.sprite.Sprite):
    '''
		Inicializa un rectangulo blanco, borde gris,
		con la palabra pasada como dato, sin proyectarse
	'''

    def __init__(self, x, palabra):
        super(Objetivo, self).__init__()

        def set_cuadrado():
            x = pygame.Surface((200, 50))
            x.fill(colores['blanco'])
            return x

        self.cuadrado = set_cuadrado()
        self.borde = pygame.draw.rect(self.cuadrado, colores['gris'], (0, 0, 200, 50), 5)
        self.rect = self.cuadrado.get_rect()
        self.palabra = palabra

    def move_rect(self, x, y):
        '''
			Mueve el rectangulo al punto x,y
		'''
        self.rect.move_ip(x, y)


class Palabra(pygame.sprite.Sprite):
    '''
		Inicializa un rectangulo blanco, borde gris,
		con la palabra en el centro
	'''

    def __init__(self, x, palabra):
        super(Palabra, self).__init__()

        def set_cuadro(palabra):
            x = pygame.Surface((200, 50)).convert()
            x.fill(colores['blanco'])
            fuente = pygame.font.Font("Data/tipografias" + os.path.sep + 'OpenSans.ttf', 30)
            titulo = fuente.render(palabra, True, colores['casiNegro'])
            titulo_rect = titulo.get_rect()
            titulo_rect.centerx = x.get_rect().centerx
            x.blit(titulo, titulo_rect)
            borde = pygame.draw.rect(x, colores['gris'], (0, 0, 200, 50), 5)
            pygame.display.update()
            return x

        self.palabra = palabra
        self.cuadro = set_cuadro(palabra)
        self.rect = self.cuadro.get_rect()
        self.click = False
        self.pos = None
        self.correcto = False

    def set_pos(self, x, y):
        '''
			Modifica la posicion
		'''
        self.pos = (x, y)

    def update(self, pantalla_base2, tresRectObj, tresObjetivos):
        '''
			Modifica la pantalla segun el movimiento del mouse,
			o si se ubico correctamente
		'''
        cuadrado_violeta = pygame.Surface((200, 50)).convert()
        cuadrado_violeta.fill(colores['violeta'])
        
        if self.click and not self.correcto:
            self.rect.center = pygame.mouse.get_pos()
            pantalla.blit(pantalla_base2, (0, 0))  # no genera arrastre de la imagen
            pantalla.blit(cuadrado_violeta,
                          (self.pos[0], self.pos[1] + 100))  # dibuja cuadrado violeta donde esta la palabra que corro
            pantalla.blit(self.cuadro, self.rect)  # dibuja la imagen moviendose
        else:
            l = list(filter(lambda x: self.rect.colliderect(x), tresRectObj))
            if l:
                ob = obtener_objetivo(l[0], tresObjetivos)
                if l[0].collidepoint(pygame.mouse.get_pos()) and ob.palabra == self.palabra:
                    pantalla.blit(cuadrado_violeta, (
                    self.pos[0], self.pos[1] + 100))  # mantiene dibujado el cuadrado violeta en caso de ser correcto
                    pantalla.blit(self.cuadro, l[0])  # pega la palabra en la posicion correcta
                    pantalla_base2.blit(pantalla, (0, 0))  # guarda la posicion de las palabras
                    self.correcto = True
                    
                elif l[0].collidepoint(pygame.mouse.get_pos()) and ob.palabra != self.palabra:
                    incorrecto()


# paleta de colores
colores = {'violetaOscuro': (81, 45, 168), 'lila': (209, 196, 233), 'violeta': (103, 58, 183),
           'blanco': (255, 255, 255), 'cian': (0, 188, 212), 'casiNegro': (33, 33, 33), 'grisOscuro': (117, 117, 117),
           'gris': (189, 189, 189)}

# Inicializar pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption('CADA UNA EN SU LUGAR')

# rellenar fondo
fondo = pygame.Surface((800, 500))
fondo.fill(colores['violeta'])
fondo_titulo = pygame.Surface((800, 100))
fondo_titulo.fill(colores['violetaOscuro'])
pantalla.blit(fondo, (0, 100))
pygame.display.flip()
tresImagenes = []
tresObjetivos = []
tresRectObj = []
tresPalabras = [0, 0, 0]
nomJuego= 'Cada Una En su Lugar'
puntosObtenidos= 0

def obtener_objetivo(rec, tresOb):
    '''
		Devuelve el Objetivo que se encuentra en ese rectangulo
	'''
    for i in tresOb:
        if rec == i.rect:
            aux = i
    return aux


def titulo_juego():
    '''
		Coloco título del juego
	'''
    fuente = pygame.font.Font("Data/tipografias" + os.path.sep + 'Barrio.ttf', 50)
    titulo = fuente.render(" CADA UNA EN SU LUGAR ", True, colores['lila'])
    titulo_rect = titulo.get_rect()
    titulo_rect.centerx = fondo_titulo.get_rect().centerx
    titulo_rect = titulo_rect.move(0, 25)
    fondo_titulo.blit(titulo, titulo_rect)
    pantalla.blit(fondo_titulo, (0, 0))
    pygame.display.flip()


def cargar_palabras():
    '''
		Carga las palabras desde un archivo
	'''
    archivo = open("Data/palabras.txt", "r")
    palabras = json.load(archivo)
    archivo.close()
    return palabras


def tablero(palabras):
	'''
		Armo el tablero del juego
	'''
	
	y = 50
	x = 50
	if tresImagenes:
		del tresImagenes[:]
	for i in range(3):
		sel = random.randrange(len(palabras))
		palsel = palabras[sel]
		del palabras[sel]
		im = Imagen(palsel)
		tresImagenes.append(im)
	
	for a in tresImagenes:
		o = Objetivo(x, a.palabra)
		o.move_rect(x, y + 325)
		tresRectObj.append(o.rect)
		tresObjetivos.append(o)
		cuadrado_violeta = pygame.Surface((200, 200)).convert()
		cuadrado_violeta.fill(colores['violeta'])
		fondo.blit(cuadrado_violeta, (x, y))
		fondo.blit(a.imagen, (x, y))
		fondo.blit(o.cuadrado, (x, y + 225))
		pantalla.blit(fondo, (0, 100))
		x += 250
	copia = pantalla.copy()
	pygame.display.flip()
	return copia


def imprimir_palabras():
    '''
		Pone los rectangulos con palabras de forma
		random en el tablero
	'''
    lis = [50, 300, 550]
    x = 50
    y = 50
    for b in tresImagenes:
        p = Palabra(x, b.palabra)
        d = random.randrange(len(lis))
        if (len(lis) != 1):
            while lis[d] == x:
                d = random.randrange(len(lis))
        if lis[d] == 50:
            tresPalabras[0] = p
        elif lis[d] == 300:
            tresPalabras[1] = p
        else:
            tresPalabras[2] = p
        p.set_pos(lis[d], y + 350)
        fondo.blit(p.cuadro, p.pos)
        pantalla.blit(fondo, (0, 100))
        del lis[d]
        x += 250
    pygame.display.flip()


def click_error(pantalla_base2):
    '''
		Imprime error
	'''
    fuente = pygame.font.Font('Data/tipografias' + os.path.sep + 'CaveatBrush.ttf', 40)
    mensaje = fuente.render('Debes arrastras las palabras a su respectiva imagen', True, colores['cian'])
    mensaje_rect = mensaje.get_rect()
    mensaje_rect.centerx = fondo.get_rect().centerx
    mensaje_rect = mensaje_rect.move(0, 100)
    pantalla_base2.blit(mensaje, mensaje_rect)
    pantalla.blit(pantalla_base2, (0, 0))
    pygame.display.flip()
    return True


def rearmar(tresImagenes, tresObjetivos, tresRectObj, tresPalabras):
    '''
		Arma una nueva partida
	'''
    fondo = pygame.Surface((800, 500))
    fondo.fill(colores['violeta'])
    fondo_titulo = pygame.Surface((800, 100))
    fondo_titulo.fill(colores['violetaOscuro'])
    pantalla.blit(fondo, (0, 100))
    pygame.display.flip()
    del tresImagenes[:]
    del tresObjetivos[:]
    del tresRectObj[:]
    for i in range(3):
        tresPalabras[i] = 0
    titulo_juego()
    palabras = cargar_palabras()
    tablero(palabras)
    imprimir_palabras()


def correcto():
    '''
		Imprime 'muy bien'
	'''
    fuente = pygame.font.Font('Data/tipografias' + os.path.sep + 'CaveatBrush.ttf', 40)
    mensaje = fuente.render('¡Muy bien!', True, colores['cian'])
    mensaje_rect = mensaje.get_rect()
    mensaje_rect.centerx = fondo.get_rect().centerx
    mensaje_rect = mensaje_rect.move(0, 100)
    pantalla.blit(mensaje, mensaje_rect)
    pygame.display.flip()
    time.sleep(1)


def incorrecto():
    '''
		Imprime 'te equivocaste'
	'''
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
	palabras = cargar_palabras()
	tablero(palabras)
	imprimir_palabras()
	pantalla_base2 = pantalla.copy()
	col = 0
	fila = 0
	c_e = False
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
					pygame.display.set_mode((300, 550))
					Menú.juego()
			else:
				filas = [500, 550]
				columnas = [50, 250, 300, 500, 550, 750]
				fil_im = [150, 350]
				if event.type == pygame.MOUSEBUTTONDOWN:
					fila = bisect.bisect(filas, event.pos[1])
					col = bisect.bisect(columnas, event.pos[0])
					filim = bisect.bisect(fil_im, event.pos[1])
					if fila == 0 or fila == 2 or col == 0 or col == 2 or col == 4 or col == 6:
						c_e = click_error(pantalla_base2)
					else:
						cuadrado_violeta = pygame.Surface((800, 50)).convert()
						cuadrado_violeta.fill(colores['violeta'])
						pantalla_base2.blit(cuadrado_violeta, (0, 100))
						c_e = False
						if col == 1:
							tresPalabras[0].click = True
						elif col == 3:
							tresPalabras[1].click = True
						else:
							tresPalabras[2].click = True
					if filim != 0 and filim != 2 and col != 0 and col != 2 and col != 4 and col != 6:
						if col == 1:
							tresImagenes[0].reproducir()
						elif col == 3:
							tresImagenes[1].reproducir()
						else:
							tresImagenes[2].reproducir()
				elif event.type == pygame.MOUSEBUTTONUP:
					if not c_e:
						pantalla.blit(pantalla_base2, (0, 0))  # devuelve las palabras a su lugar en caso erroneo', pb2 se va actualizando.
					else:
						click_error(pantalla_base2)
					for i in tresPalabras:
						i.click = False
		if col == 1 and fila == 1:
			tresPalabras[0].update(pantalla_base2, tresRectObj, tresObjetivos)
		elif col == 3 and fila == 1:
			tresPalabras[1].update(pantalla_base2, tresRectObj, tresObjetivos)
		elif col == 5 and fila == 1:
			tresPalabras[2].update(pantalla_base2, tresRectObj, tresObjetivos)
		if tresPalabras[0].correcto and tresPalabras[1].correcto and tresPalabras[2].correcto:
			correcto()
			puntosObtenidos+= 3
			rearmar(tresImagenes, tresObjetivos, tresRectObj, tresPalabras)
			pantalla_base2 = pantalla.copy()
			col = 0
			fila = 0
			c_e = False
		pygame.display.update()


def main(args):
    juego()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
