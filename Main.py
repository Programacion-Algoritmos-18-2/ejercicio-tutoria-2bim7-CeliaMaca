# Importamos las clases necesarias para poder ejecutar.
from archivo.miArchivo import *
from modelo.miModelo import *
from data import *

archivo = MiArchivo(nombre="archivo-datos-combinacion.txt")
operaciones = Operaciones()

# Obtenemos una lista con cada linea del archivo
lista = archivo.obtener_informacion()

# Creamos otra lista para guardar las Personas
listaPersonas = []

# Recorremos la lista 
for i in lista:
    lista[i].split(";")

    for elemento in lista[i]:
        persona = Persona(elemento[0], elemento[1], elemento[2])
        listaPersonas.append(persona)


# Creamos una lista para guardar las edades 
listaEdades = []
for persona in listaPersonas:
    listaEdades.append(persona.getEdad())


# Obtenemos la lista de edades ordenada
listaEdadesOrdenada = operaciones.merge_sort(listaEdades)