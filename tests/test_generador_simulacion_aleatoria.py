# -*- coding: utf-8 -*-
"""Tests para la clase GeneradorSimulacionAleatoria"""

import unittest
from GeneradorSimulacionAleatoria import GeneradorSimulacionAleatoria


class TestGeneradorSimulacionAleatoria(unittest.TestCase):
    """Tests para la clase GeneradorSimulacionAleatoria"""

    def test_num_chivatos(self):
        """Prueba que genera el número correcto de chivatos conocidos"""
        min_chivatos = 3
        max_chivatos = 7
        simulacion = GeneradorSimulacionAleatoria(min_chivatos, max_chivatos,
                                                  2, 5, 0.1, 30, 10, 100).generar_simulacion()
        chivatos = simulacion.chivatos
        self.assertTrue(len(chivatos) >= min_chivatos)
        self.assertTrue(len(chivatos) <= max_chivatos)
        for chivato in chivatos:
            self.assertTrue(chivato.es_chivato)

    def test_num_contactos(self):
        """Prueba que cada chivato tiene el número correcto de contactos"""
        min_chivatos = 3
        max_chivatos = 7
        min_contactos = 1
        max_contactos = 10
        simulacion = GeneradorSimulacionAleatoria(min_chivatos, max_chivatos,
                                                  min_contactos, max_contactos,
                                                  0.1, 30, 10, 100).generar_simulacion()
        chivatos = simulacion.chivatos
        for chivato in chivatos:
            contactos = chivato.delatar_conocidos()
            self.assertTrue(len(contactos) >= min_contactos)
            self.assertTrue(len(contactos) <= max_contactos)

    def test_prob_chivato(self):
        """Prueba que se respeta (aproximadamente) la probabilidad de chivato entre contactos"""
        min_chivatos = 1
        max_chivatos = 5
        min_contactos = 100
        max_contactos = 300
        prob_chivato = 0.5
        simulacion = GeneradorSimulacionAleatoria(min_chivatos, max_chivatos,
                                                  min_contactos, max_contactos,
                                                  prob_chivato, 30, 10, 100).generar_simulacion()
        chivatos = simulacion.chivatos
        for chivato in chivatos:
            contactos = chivato.delatar_conocidos()
            num_chivatos = 0
            for maleante in contactos:
                if maleante.es_chivato:
                    num_chivatos += 1
            ratio = num_chivatos / float(len(contactos))
            self.assertAlmostEqual(ratio, prob_chivato, delta=0.1)

    def test_distancia(self):
        """Prueba que la distancia se genera correctamente"""
        distancia_max = 30
        simulacion = GeneradorSimulacionAleatoria(1, 5, 10, 30, 0.5, 30, distancia_max, 100).generar_simulacion()
        chivatos = simulacion.chivatos
        for chivato in chivatos:
            contactos = chivato.delatar_conocidos()
            for maleante in contactos:
                self.assertTrue(maleante.puntos_vida >= 1)
                self.assertTrue(maleante.puntos_vida <= distancia_max)

    def test_recompensa(self):
        """Prueba que la recompensa se genera correctamente"""
        recompensa_max = 100
        simulacion = GeneradorSimulacionAleatoria(1, 5, 10, 30, 0.5, 30, 30, recompensa_max).generar_simulacion()
        chivatos = simulacion.chivatos
        for chivato in chivatos:
            contactos = chivato.delatar_conocidos()
            for maleante in contactos:
                self.assertTrue(maleante.recompensa >= 1)
                self.assertTrue(maleante.recompensa <= recompensa_max)

    def test_puntos_vida(self):
        """Prueba que los puntos de vida se generan correctamente"""
        vida_max = 100
        simulacion = GeneradorSimulacionAleatoria(1, 5, 10, 30, 0.5, vida_max, 30, 50).generar_simulacion()
        chivatos = simulacion.chivatos
        for chivato in chivatos:
            contactos = chivato.delatar_conocidos()
            for maleante in contactos:
                self.assertTrue(maleante.puntos_vida >= 1)
                self.assertTrue(maleante.puntos_vida <= vida_max)


if __name__ == '__main__':
    unittest.main()
