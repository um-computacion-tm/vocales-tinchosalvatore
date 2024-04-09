import unittest

def contar_vocales(mi_string):
    resultado = {}
    mi_string = mi_string.lower()
    for letra in mi_string:
        if letra in 'aeiou':
            if letra not in resultado:
                  resultado[letra] = 0
            resultado[letra] += 1
    return resultado

class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzzz')
        self.assertEqual (resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales('cas')
        self.assertEqual (resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual (resultado, {'a': 2})

    def test_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual (resultado, {'e': 2})

    def test_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual (resultado, {'e':1, 'a':1})        

    def test_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual (resultado, {'a': 3, 'o': 1})

    def test_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual (resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})


unittest.main()