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
        expected_output = self.expected_output
        with StringIO(self.input_text) as fake_input, StringIO() as fake_output:
            sys.stdin = fake_input
            sys.stdout = fake_output
            main()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_main_invalid_input(self):
        # тестуємо поведінку функції main() при отриманні невалідного вводу.
        expected_output = self.expected_output
        with StringIO(self.input_text) as fake_input, StringIO() as fake_output:
            sys.stdin = fake_input
            sys.stdout = fake_output
            main()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_error_message_in_stderr(self):
         # тест, що помилка пишеться в stderr
         with StringIO('1234') as fake_input, StringIO() as fake_error:
            sys.stdin = fake_input
            sys.stderr = fake_error
            try:
                main()
            except SystemExit:
                pass
            self.assertIn("Помилка: Вхідні данні можуть містити тільки ASCII символи.\n", fake_error.getvalue())

    def test_exit_code_on_error(self):
        # тест на коди завершення
        with StringIO('1234') as fake_input, StringIO() as fake_error:
            sys.stdin = fake_input
            sys.stderr = fake_error
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 1)
            self.assertIn("Помилка: Вхідні данні можуть містити тільки ASCII символи.\n", fake_error.getvalue())


if __name__ == "__main__":
    unittest.main()
