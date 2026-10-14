import random
import string


class Password:
    def __init__(self, *char_sets):
        
        if not char_sets:
            raise ValueError("Нужен хотя бы один набор")

        for s in char_sets:
            if not s:
                raise ValueError("Набор не пустой")

        self.char_sets = list(char_sets)
        self.all_chars = "".join(char_sets)

    def generate(self, length):
        if length < len(self.char_sets):
            raise ValueError(
                f"Длина пароля должна быть не меньше {len(self.char_sets)} "
                f"(по одному символу из каждого набора)"
            )
        
        password_chars = [random.choice(s) for s in self.char_sets]
        remaining = length - len(password_chars)
        password_chars += [random.choice(self.all_chars) for _ in range(remaining)]
        random.shuffle(password_chars)

        return "".join(password_chars)

if __name__ == "__main__":
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"

    pwd_gen = Password(lower, upper, digits, special)

    print("Сгенерированные пароли:")
    for _ in range(5):
        print(" ", pwd_gen.generate(12))

    print("\nПроверка: в каждом пароле есть символ из каждого набора")
    ok = True
    for _ in range(1000):
        p = pwd_gen.generate(16)
        if not (any(c in lower for c in p) and
                any(c in upper for c in p) and
                any(c in digits for c in p) and
                any(c in special for c in p)):
            ok = False
            print("Ошибка в пароле:", p)
            break
    print("Все проверки пройдены!" if ok else "Обнаружены ошибки!")
