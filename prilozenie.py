import argparse
import string

from lb5pass import Password


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
        description='Генератор паролей с гарантированным включением '
                    'символов из каждого выбранного набора',
        epilog='Пример: python password_app.py -n 3 -l 12 -d -u -v'
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
        help='использовать прописные английские буквы (A-Z)'
    )
    parser.add_argument(
        '-w', '--lowercase',
        action='store_true',
        help='использовать строчные английские буквы (a-z)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='подробный вывод (наборы и параметры)'
    )
    return parser


def collect_char_sets(args):
    explicit = args.digits or args.uppercase or args.lowercase
    char_sets = []

    if args.digits or not explicit:
        char_sets.append(string.digits)
    if args.uppercase or not explicit:
        char_sets.append(string.ascii_uppercase)
    if args.lowercase or not explicit:
        char_sets.append(string.ascii_lowercase)

    return char_sets


def main():
    parser = build_parser()
    args = parser.parse_args()

    char_sets = collect_char_sets(args)
    if args.length < len(char_sets):
        parser.error(
            f'длина пароля ({args.length}) должна быть не меньше числа '
            f'выбранных наборов символов ({len(char_sets)})'
        )

    password_gen = Password(*char_sets)

    if args.verbose:
        names = []
        explicit = args.digits or args.uppercase or args.lowercase
        if args.digits or not explicit:
            names.append('цифры')
        if args.uppercase or not explicit:
            names.append('прописные')
        if args.lowercase or not explicit:
            names.append('строчные')

        print(f'Наборы символов: {", ".join(names)}')
        print(f'Объединённый алфавит ({len(password_gen.all_chars)} симв.): '
              f'{password_gen.all_chars}')
        print(f'Количество паролей: {args.number}')
        print(f'Длина пароля: {args.length}')
        print('-' * 50)

    for i in range(1, args.number + 1):
        pwd = password_gen.generate(args.length)
        if args.verbose:
            print(f'Пароль #{i}: {pwd}')
        else:
            print(pwd)


if __name__ == '__main__':
    main()
