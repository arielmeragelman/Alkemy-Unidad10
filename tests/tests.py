import sys
import os
from typing import Type
import unittest


sys.path.append(os.path.abspath(os.path.join(os.getcwd(),"src")))
import calculadora

class PruebasCalculadora(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(calculadora.sumar(1, 2, 3, 4, 5), 15)

    def test_suma_negativos(self):
        self.assertEqual(calculadora.sumar(-1, -2, -3, -4, -5), -15)
        self.assertEqual(calculadora.sumar(1, 2, 3, -4, -5), -3)

    def test_resta_positivos(self):
        self.assertEqual(calculadora.restar(100, 1, 2, 3, 4, 5), 85)

    def test_resta_negativos(self):
        self.assertEqual(calculadora.restar(100, -1, -2, -3, -4, -5), 115)
        self.assertEqual(calculadora.restar(100, -100, -2, -3, -4, -5), -14)

    def test_producto_positivos(self):
        self.assertEqual(calculadora.multiplicar(2, 3, 4), 24)

    def test_producto_negativos(self):
        self.assertEqual(calculadora.multiplicar(-2, -3, -4), -24)
        self.assertEqual(calculadora.multiplicar(-1, -2, -3, -4), 24)

    def test_division_positivos(self):
        self.assertEqual(calculadora.dividir(100, 2, 2), 25)
        self.assertEqual(calculadora.dividir(2, 2, 2), 0.5)

    def test_division_negativos(self):
        self.assertEqual(calculadora.dividir(100, -2, 2), -25)
        self.assertEqual(calculadora.dividir(-2, 2), -1)
        self.assertEqual(calculadora.dividir(-2, 4), -0.5)
        self.assertEqual(calculadora.dividir(-2, -4), 0.5)

    def test_division_cero(self):
        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(100, 2, 0, 3)

    def test_valores_no_numericos(self):
        with self.assertRaises(TypeError):
            calculadora.sumar(1, 2, "3")
        with self.assertRaises(TypeError):
            calculadora.restar(1, 2, "3")
        with self.assertRaises(TypeError):
            calculadora.multiplicar(1, 2, "3")
        with self.assertRaises(TypeError):
            calculadora.dividir(1, 2, "3")


if __name__ == '__main__':
    unittest.main()
