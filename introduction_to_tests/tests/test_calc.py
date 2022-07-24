""" Unit Test Examples """
from unittest import TestCase
import unittest

try:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
except Exception as error:
    raise error

from calc import soma


class TestCalc(TestCase):
    """Test class"""

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        """Test function"""
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        """Test Function"""
        x_y_outputs = (
            (10, 10, 20),
            (10, 20, 30),
            (-10, 10, 0),
            (10, 2.1, 12.1),
            (10.1, 1, 11.1),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, z = x_y_output
                self.assertEqual(soma(x, y), z)


unittest.main(verbosity=1)
