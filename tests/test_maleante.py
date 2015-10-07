# -*- coding: utf-8 -*-
"""Tests para la clase Maleante"""

import unittest
from Maleante import Maleante
from Maleante import LabiosSellados


class TestMaleante(unittest.TestCase):
    """Tests para la clase Maleante"""

    def test_incluir_conocido(self):
        """Test para el método incluir_conocido"""
        maleante = Maleante("Maleante 1", False, 1, 100, 100)
        self.assertListEqual(maleante._conocidos, [])
        maleante_amigo = Maleante("Maleante Amigo 1", False, 1, 100, 100)
        maleante.incluir_conocido(maleante_amigo)
        self.assertListEqual(maleante._conocidos, [maleante_amigo])
        maleante_amigo2 = Maleante("Maleante Amigo 2", False, 1, 100, 100)
        maleante.incluir_conocido(maleante_amigo2)
        self.assertListEqual(maleante._conocidos, [maleante_amigo, maleante_amigo2])

    def test_delatar_conocidos_chivato(self):
        """Test para el método delatar_conocidos"""
        chivato = Maleante("Maleante 1", True, 1, 100, 100)
        maleante_amigo = Maleante("Maleante Amigo 1", False, 1, 100, 100)
        chivato.incluir_conocido(maleante_amigo)
        maleante_amigo2 = Maleante("Maleante Amigo 2", False, 1, 100, 100)
        chivato.incluir_conocido(maleante_amigo2)
        self.assertListEqual(chivato.delatar_conocidos(), [maleante_amigo, maleante_amigo2])

    def test_delatar_conocidos_no_chivato(self):
        """Prueba que se lanza excepción al pedir información a un maleante no chivato"""
        johnny_labios_sellados = Maleante("Maleante 1", False, 1, 100, 100)
        maleante_amigo = Maleante("Maleante Amigo 1", False, 1, 100, 100)
        johnny_labios_sellados.incluir_conocido(maleante_amigo)
        maleante_amigo2 = Maleante("Maleante Amigo 2", False, 1, 100, 100)
        johnny_labios_sellados.incluir_conocido(maleante_amigo2)
        self.assertRaises(LabiosSellados, johnny_labios_sellados.delatar_conocidos)

if __name__ == '__main__':
    unittest.main()
