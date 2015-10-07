# -*- coding: utf-8 -*-
"""Módulo Cazarecompensas. Incluye la clase Cazarecompensas, ReporteMision y Ataque"""


class Cazarecompensas(object):
    """Clase que modela un Cazarecompensas"""

    def __init__(self, chivatos):
        self.mis_chivatos = chivatos
        self.recompensa = 0
        self.gastos = 0

    def atrapar_maleantes(self, max_ataques):
        """Inicia la búsqueda de Maleantes. Devuelve la lista de ataques necesarios.

        Parte de una lista de chivatos de los que obtener información.
        Por cada chivato, se obtiene una lista de maleantes.
        Se combinan las listas de maleantes, filtrando los que sean chivatos.
        Se ordenan por distancia y se capturan en orden creciente."""
        objetivos = self.interrogar_chivatos()
        return self.atacar_maleantes(objetivos, max_ataques)

    def interrogar_chivatos(self):
        """Obtiene una lista de Maleantes (no chivatos) interrogando a los chivatos conocidos"""
        maleantes = []
        for chivato in self.mis_chivatos:
            maleantes += [m for m in chivato.delatar_conocidos() if not m.es_chivato]
        maleantes.sort(key=lambda x: x.distancia)
        return maleantes

    def atacar_maleantes(self, maleantes, max_ataques):
        """Lleva a cabo el ataque a cada maleante, combinando la lista de objetos Ataque necesarios"""
        reporte = ReporteMision()
        ataques_gastados = 0
        for m in maleantes:
            ataques_a_realizar = self.atacar_maleante(m)
            if ataques_gastados + len(ataques_a_realizar) <= max_ataques and m.recompensa > m.distancia:
                reporte.incluir_ataques(ataques_a_realizar)
                ataques_gastados += len(ataques_a_realizar)
                reporte.incluir_enemigo(m)
                self.gastos += m.distancia
                reporte.incrementar_gastos(m.distancia)
                self.recompensa += m.recompensa
                reporte.incrementar_recompensa(m.recompensa)

        return reporte

    def atacar_maleante(self, maleante):
        """Realiza el ataque a un Maleante concreto"""
        ataques = list()
        ataques.append(Ataque(maleante.nombre, maleante.puntos_vida))
        while maleante.puntos_vida > 0:
            maleante.puntos_vida -= 1
            ataques.append(Ataque(maleante.nombre, maleante.puntos_vida))
        return ataques


class ReporteMision(object):
    """Clase que modela el reporte de la misión"""

    def __init__(self):
        self.ataques = list()
        self.recompensa = 0
        self.gastos = 0
        self.enemigos = list()

    def incluir_enemigo(self, maleante):
        self.enemigos.append(maleante)

    def incluir_ataques(self, ataques):
        self.ataques += ataques

    def incrementar_recompensa(self, recompensa):
        self.recompensa += recompensa

    def incrementar_gastos(self, gastos):
        self.gastos += gastos


class Ataque(object):
    """Clase que modela un ataque de un Cazarecompensas a un Maleante"""

    def __init__(self, nombre_maleante, puntos_vida):
        self.nombre_maleante = nombre_maleante
        self.puntos_vida = puntos_vida
