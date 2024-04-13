import unittest
from io import StringIO
import sys
from Lab1_rot import rot13, main

class TestRot13Cipher(unittest.TestCase):
    def setUp(self):
        self.input_text = 'Hello, World!'
        self.expected_output = 'Uryyb, Jbeyq!'
        self.incorrect_input = '1234'
        self.expected_error_message = "Помилка: Вхідні данні можуть містити тільки ASCII символи.\n"

    def test_rot13_with_uppercase(self):
        # тест тількі на великі літери
        self.assertEqual(rot13('ABC'), 'NOP')

    def test_rot13_with_only_punctuation(self):
        # тест тільки з розділовими знаками
        self.assertEqual(rot13('!@#$%'), '!@#$%')


    def test_rot13_with_punctuation(self):
        # тест на текст з розділовими знаками
        self.assertEqual(rot13('Hello, World!'), 'Uryyb, Jbeyq!')


    def test_rot13_with_empty_string(self):
         # тест на порожній рядок
        self.assertEqual(rot13(''), '')

    def test_rot13_with_long_text(self):
      # тест на обробку довгого тексту
      long_text = 'A' * 10000
      expected_output = 'N' * 10000
      self.assertEqual(rot13(long_text), expected_output)

    def test_main_valid_input(self):
        # тестуємо поведінку функції main() при отриманні валідного вводу
     expected_output = f"Введіть текст для шифрування та натисніть Enter: Зашифрований текст: {self.expected_output}\n"
     with StringIO(self.input_text) as fake_input, StringIO() as fake_output:
        sys.stdin = fake_input
        sys.stdout = fake_output
        main()
        self.assertEqual(fake_output.getvalue(), expected_output)


    def test_main_invalid_input(self):
        # тестуємо поведінку функції main() при отриманні невалідного вводу.
     expected_output = "Введіть текст для шифрування та натисніть Enter: Зашифрований текст: " + self.expected_output + '\n'
     with StringIO(self.input_text) as fake_input, StringIO() as fake_output:
        sys.stdin = fake_input
        sys.stdout = fake_output
        main()
        self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
