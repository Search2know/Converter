import unittest
from io import StringIO
from unittest.mock import patch
from converter import converter

class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_conversion(self):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            converter('25 C')
            expected_output = 'Conversion result: 25.0°C = 77.0°F\nConversion result: 25.0°C = 298.15°K\n'
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_fahrenheit_conversion(self):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            converter('77 F')
            expected_output = 'Conversion result: 77.0°F = 25.0°C\nConversion result: 77.0°F = 298.15°K\n'
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_kelvin_conversion(self):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            converter('298.15 K')
            expected_output = 'Conversion result: 298.15°K = 25.0°C\nConversion result: 298.15°K = 77.0°F\n'
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '_converter__':
    unittest.main()
