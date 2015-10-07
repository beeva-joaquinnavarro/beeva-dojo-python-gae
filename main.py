# -*- coding: utf-8 -*-
"""Módulo principal de la aplicación"""

from Simulacion import Simulacion
from Maleante import Maleante
from GeneradorSimulacionAleatoria import GeneradorSimulacionAleatoria


def crear_simulacion():
    """Crea una simulación determinista"""
    chivato1 = Maleante("Chivato 1", True, 1, 100, 100)
    maleante_amigo11 = Maleante("Maleante Amigo 1-1", False, 10, 30, 100)
    maleante_amigo12 = Maleante("Maleante Amigo 1-2", True, 2, 20, 100)
    chivato1.incluir_conocido(maleante_amigo11)
    chivato1.incluir_conocido(maleante_amigo12)
    chivato2 = Maleante("Chivato 2", True, 1, 100, 100)
    maleante_amigo21 = Maleante("Maleante Amigo 2-1", False, 4, 30, 100)
    maleante_amigo22 = Maleante("Maleante Amigo 2-2", False, 7, 40, 100)
    chivato2.incluir_conocido(maleante_amigo21)
    chivato2.incluir_conocido(maleante_amigo22)
    return Simulacion([chivato1, chivato2], 100)


def crear_simulacion_aleatoria():
    """Crea una simulacion aleatoria"""
    generador = GeneradorSimulacionAleatoria(3, 7, 2, 5, 0.1, 30, 10, 100)
    return generador.generar_simulacion()


def main():
    """Función principal"""
    sim = crear_simulacion_aleatoria()
    sim.ejecutar()

if __name__ == '__main__':
    main()
