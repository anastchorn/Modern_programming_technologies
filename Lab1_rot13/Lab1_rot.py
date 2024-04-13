import sys

def rot13(text):
    # реалізуємо алгоритм шифрування ROT13, який переставляє літери на 13 позицій в алфавіті.
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def main():
     # функція main читає вхідні дані, застосовує шифрування і виводить результат. Також обробляє помилки та виводить їх у стандартний потік помилок
    try:
        sys.stdout.write("Введіть текст для шифрування та натисніть Enter: ")
        sys.stdout.flush()
        input_text = sys.stdin.readline().strip()
        if not input_text.isascii() or any(char.isdigit() for char in input_text):
            raise ValueError("Вхідні данні можуть містити тільки ASCII символи.")
        encrypted_text = rot13(input_text)
        sys.stdout.write("Зашифрований текст: " + encrypted_text + '\n')
    except Exception as e:
        sys.stderr.write("Помилка: {}\n".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
