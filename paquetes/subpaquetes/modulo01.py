# -*- coding: utf-8 -*-
#importamos los modulos completos
import bucles as b
#Importacion del modulo 1
import paquetes.modulo01 as cosa
import paquetes.subpaquetes.modulo01 as hola

print cosa.CONSTANTE_1

#importar solo la funcionalidad que nos interesa
from paquetes.modulo02 import funcion01 as adios   
from paquetes.modulo02 import funcion01 as hola

from flask import Flask

print esto.adios()

#importar primero, los modulos propios de Python, segundo importar los de tercero y finalmente importar los modulos de nuestra aplicacion
#Entre importacion y importacion dejar una linea en blanco
#al finalizar las importaciones dos lineas en blanco
