import unittest
from celsiusTofarenheit import CelsiueToFarenheit

class Testando(unittest.TestCase):

    def test_successo(self):
        celsius = 41.0
        fahrenheitEsperado = 105.8

        c = CelsiueToFarenheit()
        fahrenheitResultado = c.convert(celsius)

        self.assertEqual(fahrenheitEsperado, fahrenheitResultado)

    def test_conversao_errada(self):
        celsius = 41.0
        fahrenheitEsperado = 105.8
        fahrenheitResultado = 106

        self.assertEqual(fahrenheitResultado, fahrenheitEsperado)


