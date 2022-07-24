"""
TDD - Test Driven Development
Red
First Part > Create the test and see it failing
Green
Second Part > Create the test and see it passing
Refactor
Third Part > Improve the code
"""
import unittest

from black import out

try:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
except Exception as error:
    raise error

from bacon_eggs import bacon_and_eggs


class TestBaconAndEggs(unittest.TestCase):
    """Test"""

    def test_bacon_and_eggs(self):
        """Test Function"""
        with self.assertRaises(AssertionError):
            bacon_and_eggs("")

    def test_bacon_and_eggs_must_return_bacon_and_eggs_must_if_input_is_multiple_of_3_and_5(
        self,
    ):
        inputs = (15, 30, 45, 60)
        output = "Bacon and Eggs"

        for inp in inputs:
            with self.subTest(input=inp, output=output):
                self.assertEqual(
                    bacon_and_eggs(inp),
                    output,
                    msg=f'"{inp}" does not return "{output}" ',
                )

    def test_bacon_and_eggs_must_return_starving_if_input_is_NOT_a_multiple_of_3_and_5(
        self,
    ):
        inputs = (2, 4, 8, 16)
        output = "Starving"

        for inp in inputs:
            with self.subTest(input=inp, output=output):
                self.assertEqual(
                    bacon_and_eggs(inp),
                    output,
                    msg=f'"{inp}" does not return "{output}" ',
                )

    def test_bacon_and_eggs_must_return_Bacon_if_input_is_a_multiple_of_3_and_not_5(
        self,
    ):
        inputs = (3, 6, 9, 12)
        output = "Bacon"

        for inp in inputs:
            with self.subTest(input=inp, output=output):
                self.assertEqual(
                    bacon_and_eggs(inp),
                    output,
                    msg=f'"{inp}" does not return "{output}" ',
                )

    def test_bacon_and_eggs_must_return_Eggs_if_input_is_only_a_multiple_of_5_and_not_3(
        self,
    ):
        inputs = (5, 10, 20, 25)
        output = "Eggs"

        for inp in inputs:
            with self.subTest(input=inp, output=output):
                self.assertEqual(
                    bacon_and_eggs(inp),
                    output,
                    msg=f'"{inp}" does not return "{output}" ',
                )


unittest.main(verbosity=2)
