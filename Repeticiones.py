#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Data.Imagen import Imagen2
"""
Identifica si existe una letra o silaba que sea igual pero que tenga el mismo numero de cuadrante asignado
por lo tanto en caso de arrastrar por ejemplo cualquier letra 'a' seria correcta para el algoritmo por mas que la posicion
de la mismo no corresponda siendo que otra no seleccionada corresponde
"""
def repeticiones(Coordenadas_cuadrantes,activos,indice,obj):
	for i in activos:
		if i.nombre == obj.nombre and Coordenadas_cuadrantes.index(i.posFinal) == indice:
			return i
	
