"""
Class Person
    __init__
    name:str
    surname:str
    data:str = False
API:
    retrieve_data -> method
        OK
        404
        
        True if data successfully obtained else False
"""

try:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
except Exception as error:
    raise error


import unittest
from person import Person
from unittest.mock import patch


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Person("Andrea", "Miranda")
        return super().setUp()

    def test_person_attr_name_has_correct_value(self):
        self.assertEqual(self.p1.name, "Andrea")

    def test_person_attr_name_is_string(self):
        self.assertIsInstance(self.p1.name, str)

    def test_person_attr_surname_is_string(self):
        self.assertIsInstance(self.p1.surname, str)

    def test_person_attr_data_starts_false(self):
        self.assertFalse(self.p1.data)

    def test_retrieve_data_success_ok(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.retrieve_data(), "CONNECTED")
            self.assertTrue(self.p1.data)

    def test_retrieve_data_failed_404(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.retrieve_data(), "ERROR 404")
            self.assertFalse(self.p1.data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
