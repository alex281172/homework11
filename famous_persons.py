import random


def get_random_person():

    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                     'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                     'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                     'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}


    names, date = random.choice(list(FAMOUS_PEOPLE.items()))
    return names, date


def get_person_and_question():

    names, date = get_random_person()

    answer = input(f'Когда родился {names} ')

    if answer == date:
        print('Верно')
    else:
        print('Неверно')


if __name__ == '__main__':
    print('Проверка фукцнии', get_random_person())