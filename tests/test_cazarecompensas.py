# -*- coding: utf-8 -*-
"""Tests para la clase Cazarecompensas"""

import unittest
from Cazarecompensas import Cazarecompensas
from Maleante import Maleante


class TestCazarecompensas(unittest.TestCase):
    """Tests para la clase Cazarecompensas"""

    def setUp(self):
        chivato1 = Maleante("Chivato 1", True, 1, 100, 100)
        self.maleante_amigo11 = Maleante("Maleante Amigo 1-1", False, 10, 1, 100)
        self.maleante_amigo12 = Maleante("Maleante Amigo 1-2", True, 2, 2, 100)
        chivato1.incluir_conocido(self.maleante_amigo11)
        chivato1.incluir_conocido(self.maleante_amigo12)
        chivato2 = Maleante("Chivato 2", True, 1, 100, 100)
        self.maleante_amigo21 = Maleante("Maleante Amigo 2-1", False, 4, 3, 100)
        self.maleante_amigo22 = Maleante("Maleante Amigo 2-2", False, 7, 4, 100)
        chivato2.incluir_conocido(self.maleante_amigo21)
        chivato2.incluir_conocido(self.maleante_amigo22)
        self.cazarecompensas = Cazarecompensas([chivato1, chivato2])

    def test_interrogar_chivatos(self):
        """Prueba que el cazarecompensas obtiene información de los chivatos"""
        objetivos = [self.maleante_amigo21, self.maleante_amigo22, self.maleante_amigo11]
        self.assertListEqual(self.cazarecompensas.interrogar_chivatos(), objetivos)

    def test_atacar_maleante(self):
        """Prueba el método atacar_maleante"""
        maleante = Maleante("Malote 1", False, 1, 3, 100)
        self.assertEqual(self.cazarecompensas.recompensa, 0)
        self.assertEqual(self.cazarecompensas.gastos, 0)
        ataques = self.cazarecompensas.atacar_maleante(maleante)
        self.assertEqual(maleante.puntos_vida, 0)
        self.assertEqual(len(ataques), 4)
        self.assertEqual(ataques[0].puntos_vida, 3)
        self.assertEqual(ataques[0].nombre_maleante, "Malote 1")
        self.assertEqual(ataques[1].puntos_vida, 2)
        self.assertEqual(ataques[1].nombre_maleante, "Malote 1")
        self.assertEqual(ataques[2].puntos_vida, 1)
        self.assertEqual(ataques[2].nombre_maleante, "Malote 1")
        self.assertEqual(ataques[3].puntos_vida, 0)
        self.assertEqual(ataques[3].nombre_maleante, "Malote 1")

    def test_atacar_maleantes(self):
        """Prueba el método atacar_maleantes"""
        maleante1 = Maleante("Malote 1", False, 1, 3, 100)
        maleante2 = Maleante("Malote 2", False, 10, 4, 200)
        self.assertEqual(self.cazarecompensas.recompensa, 0)
        self.assertEqual(self.cazarecompensas.gastos, 0)
        reporte = self.cazarecompensas.atacar_maleantes([maleante1, maleante2], 100)
        ataques = reporte.ataques
        self.assertEqual(maleante1.puntos_vida, 0)
        self.assertEqual(maleante2.puntos_vida, 0)
        self.assertEqual(self.cazarecompensas.recompensa, 300)
        self.assertEqual(self.cazarecompensas.gastos, 11)
        self.assertEqual(reporte.recompensa, 300)
        self.assertEqual(reporte.gastos, 11)
        self.assertEqual(len(ataques), 9)
        self.assertEqual(ataques[0].puntos_vida, 3)
        self.assertEqual(ataques[0].nombre_maleante, "Malote 1")
        self.assertEqual(ataques[1].puntos_vida, 2)
        self.assertEqual(ataques[1].nombre_maleante, "Malote 1")
        self.assertEqual(ataques[2].puntos_vida, 1)
        self.assertEqual(ataques[2].nombre_maleante, "Malote 1")
        self.assertEqual(ataques[3].puntos_vida, 0)
        self.assertEqual(ataques[3].nombre_maleante, "Malote 1")
        self.assertEqual(ataques[4].puntos_vida, 4)
        self.assertEqual(ataques[4].nombre_maleante, "Malote 2")
        self.assertEqual(ataques[5].puntos_vida, 3)
        self.assertEqual(ataques[5].nombre_maleante, "Malote 2")
        self.assertEqual(ataques[6].puntos_vida, 2)
        self.assertEqual(ataques[6].nombre_maleante, "Malote 2")
        self.assertEqual(ataques[7].puntos_vida, 1)
        self.assertEqual(ataques[7].nombre_maleante, "Malote 2")
        self.assertEqual(ataques[8].puntos_vida, 0)
        self.assertEqual(ataques[8].nombre_maleante, "Malote 2")

    def test_atrapar_maleantes(self):
        """Prueba el método atrapar_maleantes"""
        reporte = self.cazarecompensas.atrapar_maleantes(100)
        ataques = reporte.ataques
        self.assertEqual(self.cazarecompensas.recompensa, 300)
        self.assertEqual(self.cazarecompensas.gastos, 21)
        self.assertEqual(reporte.recompensa, 300)
        self.assertEqual(reporte.gastos, 21)
        self.assertEqual(len(ataques), 11)
        self.assertEqual(ataques[0].puntos_vida, 3)
        self.assertEqual(ataques[0].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[1].puntos_vida, 2)
        self.assertEqual(ataques[1].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[2].puntos_vida, 1)
        self.assertEqual(ataques[2].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[3].puntos_vida, 0)
        self.assertEqual(ataques[3].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[4].puntos_vida, 4)
        self.assertEqual(ataques[4].nombre_maleante, "Maleante Amigo 2-2")
        self.assertEqual(ataques[5].puntos_vida, 3)
        self.assertEqual(ataques[5].nombre_maleante, "Maleante Amigo 2-2")
        self.assertEqual(ataques[6].puntos_vida, 2)
        self.assertEqual(ataques[6].nombre_maleante, "Maleante Amigo 2-2")
        self.assertEqual(ataques[7].puntos_vida, 1)
        self.assertEqual(ataques[7].nombre_maleante, "Maleante Amigo 2-2")
        self.assertEqual(ataques[8].puntos_vida, 0)
        self.assertEqual(ataques[8].nombre_maleante, "Maleante Amigo 2-2")
        self.assertEqual(ataques[9].puntos_vida, 1)
        self.assertEqual(ataques[9].nombre_maleante, "Maleante Amigo 1-1")
        self.assertEqual(ataques[10].puntos_vida, 0)
        self.assertEqual(ataques[10].nombre_maleante, "Maleante Amigo 1-1")

    def test_atrapar_maleantes_limite(self):
        """Prueba el método atrapar_maleantes si un enemigo supera el límite de ataques y el siguiente no"""
        reporte = self.cazarecompensas.atrapar_maleantes(7)
        ataques = reporte.ataques
        self.assertEqual(self.cazarecompensas.recompensa, 200)
        self.assertEqual(self.cazarecompensas.gastos, 14)
        self.assertEqual(reporte.recompensa, 200)
        self.assertEqual(reporte.gastos, 14)
        self.assertEqual(len(ataques), 6)
        self.assertEqual(ataques[0].puntos_vida, 3)
        self.assertEqual(ataques[0].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[1].puntos_vida, 2)
        self.assertEqual(ataques[1].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[2].puntos_vida, 1)
        self.assertEqual(ataques[2].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[3].puntos_vida, 0)
        self.assertEqual(ataques[3].nombre_maleante, "Maleante Amigo 2-1")
        self.assertEqual(ataques[4].puntos_vida, 1)
        self.assertEqual(ataques[4].nombre_maleante, "Maleante Amigo 1-1")
        self.assertEqual(ataques[5].puntos_vida, 0)
        self.assertEqual(ataques[5].nombre_maleante, "Maleante Amigo 1-1")

    def test_atrapar_maleantes_no_rentables(self):
        """Prueba el método atrapar_maleantes cuando atrapar un enemigo no es rentable"""
        chivato = Maleante("Chivato 1", True, 1, 100, 100)
        maleante_amigo11 = Maleante("Maleante Amigo 1-1", False, 10, 1, 100)
        maleante_amigo12 = Maleante("Maleante Amigo 1-2", False, 20, 2, 10)
        chivato.incluir_conocido(maleante_amigo11)
        chivato.incluir_conocido(maleante_amigo12)
        cazarecompensas = Cazarecompensas([chivato])
        reporte = cazarecompensas.atrapar_maleantes(10)
        ataques = reporte.ataques
        self.assertEqual(cazarecompensas.recompensa, 100)
        self.assertEqual(cazarecompensas.gastos, 10)
        self.assertEqual(reporte.recompensa, 100)
        self.assertEqual(reporte.gastos, 10)
        self.assertEqual(len(ataques), 2)
        self.assertEqual(ataques[0].puntos_vida, 1)
        self.assertEqual(ataques[0].nombre_maleante, "Maleante Amigo 1-1")
        self.assertEqual(ataques[1].puntos_vida, 0)
        self.assertEqual(ataques[1].nombre_maleante, "Maleante Amigo 1-1")


if __name__ == '__main__':
    unittest.main()
