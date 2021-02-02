#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os
from pygame.locals import *


def proporcional(imag):
    """
    Acomoda la imagen png a valores proporcionales sin deformar la imagen dentro del rectangulo asignado de 80 x 80
    """
    medidas = imag.get_rect()
    ancho = medidas[2]
    alto = medidas[3]
    coef = None
    if ancho >= alto:
        nue_ancho=100
        nue_alto=(alto*100)/ancho
    else:
        nue_alto=100
        nue_ancho=(ancho*100)/alto
    nue_imag = pygame.transform.scale(imag,(int(nue_ancho),int(nue_alto)))
    return nue_imag
