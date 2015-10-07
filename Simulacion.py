# -*- coding: utf-8 -*-
"""Clase que implementa la simulación de la Kata 1 del curso GAE"""
from Cazarecompensas import Cazarecompensas


class Simulacion(object):
    """Clase que implementa la simulación de la Kata 1 del curso GAE"""

    def __init__(self, chivatos, max_ataques):
        """Construye una simulación en base a una lista de chivatos con un máximo de ataques"""
        self.chivatos = chivatos
        self.max_ataques = max_ataques
        self.cazarecompensas = Cazarecompensas(chivatos)

    def ejecutar(self):
        """Ejecuta la simulación e imprime la planificación de la semana"""
        reporte = self.cazarecompensas.atrapar_maleantes(self.max_ataques)
        self.imprimir_reporte(reporte)

    def imprimir_reporte(self, reporte):
        """Imprime por pantalla el reporte de batalla"""
        # enemigos
        print "Voy a dar caza a los siguientes villanos:"
        print "Nombre - puntos de vida - recompensa"
        patron_enemigo_str = '%s - %d puntos de vida - %d euros'
        for enemigo in reporte.enemigos:
            print patron_enemigo_str % (enemigo.nombre, enemigo.puntos_vida_inicial, enemigo.recompensa)
        # ataques
        dias_de_la_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        patron_ataque_str = "%d H - %s %d pv"
        dia = 0
        hora = 0
        for ataque in reporte.ataques:
            if hora % 24 == 0:
                print dias_de_la_semana[dia % 7]
                dia += 1
            print patron_ataque_str % (hora % 24, ataque.nombre_maleante, ataque.puntos_vida)
            hora += 1
        print 'Ingresos: %d' % self.cazarecompensas.recompensa
        print 'Gastos: %d' % self.cazarecompensas.gastos
        print 'Beneficios: %d' % (self.cazarecompensas.recompensa - self.cazarecompensas.gastos)
