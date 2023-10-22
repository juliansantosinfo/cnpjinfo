import logging
import random
import unittest

from PyFakeDados.cnpj import gerar_cnpj
from cnpjinfo import cnpjinfo, cnpjinfo_list

logging.basicConfig(level=logging.DEBUG)

class TestCnpjInfo(unittest.TestCase):
    def test_cnpjinfo(self):
        # Gera um CNPJ aleatório para teste
        cnpj = "05720854000166"

        # Chama a função cnpjinfo com o CNPJ aleatório
        result = cnpjinfo(cnpj)

        # Verifica se o resultado não é None (indicando que os dados foram recuperados)
        self.assertIsNotNone(result)

        # Verifica se o resultado é um dicionário (estrutura esperada dos dados do CNPJ)
        self.assertIsInstance(result, dict)
    
    def test_cnpjinfo_list(self):
        # Gera um CNPJ aleatório para teste
        cnpj_list = [ "05720854000166", "00623904000173", "15436940000103" ]

        # Chama a função cnpjinfo com o CNPJ aleatório
        result = cnpjinfo_list(cnpj_list)

        # Verifica se o resultado não é None (indicando que os dados foram recuperados)
        self.assertIsNotNone(result)

        # Verifica se o resultado é um dicionário (estrutura esperada dos dados do CNPJ)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
