#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def guardar_palabras():
	palabras = {'a':['abeja','auto','ave','avión'],'e':['elefante','erizo','escalera','espejo','estrella'],'i':['iglesia','igloo','iguana','imán','indio'],'l':['lámpara','lápiz','lluvia','lombriz'],'o':['ojo','olla','oreja','oso','oveja']}
	archivo = open("palabrasEntrometido.txt", "w")
	json.dump(palabras, archivo)
	archivo.close()                  
	return palabras

def cargar_palabras():
	archivo = open("palabrasEntrometido.txt", "r")
	palabras = json.load(archivo)
	archivo.close()    
	print(json.dumps(palabras, sort_keys=True, indent=4))              
	return palabras

guardar_palabras()
cargar_palabras()


