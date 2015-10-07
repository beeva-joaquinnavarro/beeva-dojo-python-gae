# -*- coding: utf-8 -*-
"""Clase que modela un Maleante (puede ser chivato o no)"""


class Maleante(object):
    """Clase que modela un Maleante (puede ser chivato o no)"""

    def __init__(self, nombre, chivato, distancia, puntos_vida, recompensa):
        self.nombre = nombre
        self.es_chivato = chivato
        self.distancia = distancia
        self.puntos_vida = puntos_vida
        self.puntos_vida_inicial = puntos_vida
        self.recompensa = recompensa
        self._conocidos = []

    def incluir_conocido(self, maleante):
        """Añade un Maleante a la lista de conocidos"""
        self._conocidos.append(maleante)

    def delatar_conocidos(self):
        """Si es un chivato, devuelve la lista de sus conocidos"""
        if not self.es_chivato:
            raise LabiosSellados()
        return self._conocidos


class LabiosSellados(Exception):
    """Excepción al pedir información a un maleante no chivato"""
    pass
