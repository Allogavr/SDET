import random
import allure


@allure.step("Генерация Post Code из 10 цифр")
def generate_post_code():
    """Генерировать случайный Post Code из 10 цифр"""
    post_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    allure.attach(post_code, name="Generated Post Code", attachment_type=allure.attachment_type.TEXT)
    return post_code


@allure.step("Генерация First Name из Post Code: {post_code}")
def generate_first_name_from_post_code(post_code):
    """
    Преобразует Post Code в First Name согласно правилам::
    1. Разбить Post Code на двузначные числа (5 чисел)
    2. Каждое число преобразовать в букву английского алфавита (0-25, 26->0, и т.д.)

    Пример: 0001252667 = abzap (00->a, 01->b, 25->z, 26->a, 67->p)
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    first_name = ''

    # Разбиваем на двузначные числа
    for i in range(0, 10, 2):
        two_digit_num = int(post_code[i:i + 2])
        # Получаем букву по модулю 26
        letter_index = two_digit_num % 26
        first_name += alphabet[letter_index]

    allure.attach(first_name, name="Generated First Name", attachment_type=allure.attachment_type.TEXT)
    return first_name


@allure.step("Поиск клиента с длиной имени, ближайшей к среднему: {names}")
def find_customer_closest_to_average_length(names):
    """
    Найти клиента, у которого длина имени ближе всего к среднему арифметическому длин всех имен

    Пример: ['Albus', 'Neville', 'Voldemort'] -> длины [5, 7, 9] -> среднее 7 -> удаляем 'Neville'
    """
    if not names:
        return None

    # Получаем длины имен
    lengths = [len(name) for name in names]
    allure.attach(str(lengths), name="Name Lengths", attachment_type=allure.attachment_type.TEXT)

    # Вычисляем среднее арифметическое
    average_length = sum(lengths) / len(lengths)
    allure.attach(str(average_length), name="Average Length", attachment_type=allure.attachment_type.TEXT)

    # Находим имя с длиной, ближайшей к среднему
    closest_name = min(names, key=lambda name: abs(len(name) - average_length))
    allure.attach(closest_name, name="Customer to Delete", attachment_type=allure.attachment_type.TEXT)

    return closest_name
