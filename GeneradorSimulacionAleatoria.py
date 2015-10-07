# -*- coding: utf-8 -*-
"""Generador de simulaciones aleatorias"""

from Simulacion import Simulacion
from Maleante import Maleante
import random
import time


class GeneradorSimulacionAleatoria(object):
    """Generador de simulaciones aleatorias"""

    def __init__(self, min_chivatos_conocidos, max_chivatos_conocidos, min_contactos, max_contactos, prob_chivato,
                 max_vida, max_distancia, max_recompensa):
        self.min_chivatos_conocidos = min_chivatos_conocidos
        self.max_chivatos_conocidos = max_chivatos_conocidos
        self.min_contactos = min_contactos
        self.max_contactos = max_contactos
        self.prob_chivato = prob_chivato
        self.max_vida = max_vida
        self.max_distancia = max_distancia
        self.max_recompensa = max_recompensa

    def generar_simulacion(self):
        """Genera una simulación aleatoria"""
        random.seed(time.time())
        num_chivatos = random.randint(self.min_chivatos_conocidos, self.max_chivatos_conocidos)
        chivatos = list()
        for i in range(num_chivatos):
            nombre = "Chivato " + str(i)
            chivato = self.generar_maleante(nombre, True)
            num_contactos = random.randint(self.min_contactos, self.max_contactos)
            for j in range(num_contactos):
                es_chivato = random.random() >= (1 - self.prob_chivato)
                nombre_contacto = "Malote %d-%d" % (i, j)
                contacto = self.generar_maleante(nombre_contacto, es_chivato)
                chivato.incluir_conocido(contacto)
            chivatos.append(chivato)
        sim = Simulacion(chivatos, 7*24)
        return sim

    def generar_maleante(self, nombre, chivato):
        """Genera un maleante aleatorio"""
        distancia = random.randint(1, self.max_distancia)
        vida = random.randint(1, self.max_vida)
        recompensa = random.randint(1, self.max_recompensa)
        return Maleante(nombre, chivato, distancia, vida, recompensa)
