import argparse


def positive_int(value):
    """Проверка: целое число >= 1."""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' не является целым числом")
    if ivalue < 1:
        raise argparse.ArgumentTypeError(
            f"значение должно быть >= 1, получено {ivalue}"
        )
    return ivalue


def length_int(value):
    """Проверка: целое число >= 5."""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' не является целым числом")
    if ivalue < 5:
        raise argparse.ArgumentTypeError(
            f"длина должна быть >= 5, получено {ivalue}"
        )
    return ivalue


def build_parser():
    parser = argparse.ArgumentParser(
        prog='password-generator',
        description='Генератор паролей с настраиваемым алфавитом (интерфейс)',
        epilog='Пример: python3 programa.py -n 3 -l 12 -d -u'
    )
    parser.add_argument(
        '-n', '--number',
        type=positive_int,
        default=1,
        help='количество генерируемых паролей (>= 1, по умолчанию 1)'
    )
    parser.add_argument(
        '-l', '--length',
        type=length_int,
        default=10,
        help='длина каждого пароля (>= 5, по умолчанию 10)'
    )
    parser.add_argument(
        '-d', '--digits',
        action='store_true',
        help='использовать цифры (0-9)'
    )
    parser.add_argument(
        '-u', '--uppercase',
        action='store_true',
        help='использовать заглавные английские буквы (A-Z)'
    )
    parser.add_argument(
        '-w', '--lowercase',
        action='store_true',
        help='использовать строчные английские буквы (a-z)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='подробный вывод параметров'
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    print('Разобранные параметры командной строки:')
    print(f'  number    = {args.number}')
    print(f'  length    = {args.length}')
    print(f'  digits    = {args.digits}')
    print(f'  uppercase = {args.uppercase}')
    print(f'  lowercase = {args.lowercase}')
    print(f'  verbose   = {args.verbose}')

    explicit = args.digits or args.uppercase or args.lowercase
    used = []
    if args.digits or not explicit:
        used.append('цифры')
    if args.uppercase or not explicit:
        used.append('прописные')
    if args.lowercase or not explicit:
        used.append('строчные')

    if args.verbose:
        print(f'  наборы символов: {", ".join(used)}')


if __name__ == '__main__':
    main()
