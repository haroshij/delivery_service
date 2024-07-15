# Номер посылки с решениеме на Яндекс.Контесте:
# 116125549.

# Импортируем stdin для более быстрого считывания вводимых данных.
from sys import stdin


def main(data: tuple[int], limit: int) -> int:
    """
    Функция для вычисления минимального количества платформ,
    необходимых для перевозки роботов.
    """

    # Множество номеров (индексов) роботов:
    # в данном множестве будем фиксировать индексы тех роботов,
    # для которых уже определено решение, будут ли они
    # погружены парами, или по одному.
    nums_using_robots = set()

    # Счётчик платформ, необходимых для перевозки.
    platform_count = 0

    def robot_selection(data: tuple[int], limit: int) -> int:
        """
        Вспомогательная функция, перебирающая всех роботов
        и определяющая, какие из них можно погрузить вместе.
        """

        # Объявляем переменный, которые будем брать из внешней функции.
        nonlocal nums_using_robots
        nonlocal platform_count

        # Вспомогательный словарь для поиска пар роботов.
        pair_dict = dict()

        for index in range(len(data)):  # Перебираем все индексы роботов
            # Если для данного робота ещё не определена платформа,
            if index not in nums_using_robots:
                # то, смотрим, не равен ли он текущей грузоподъёмности.
                if data[index] == lmt:
                    nums_using_robots.add(index)
                    platform_count += 1
                # Если нет, то пробуем подобрать пару.
                # Если пара уже есть, то:
                elif data[index] in pair_dict:
                    # добавляем индексы.
                    nums_using_robots.add(index)
                    nums_using_robots.add(pair_dict[data[index]])
                    platform_count += 1  # Увеличиваем счётчик платформ.
                    del pair_dict[data[index]]  # Удаляем пару из словаря.
                # Если подходящей пары нет, то ищем пару для него.
                else:
                    pair_dict[lmt - data[index]] = index

    # С помощью вспомогательной функции, выберем
    # максимально подходящие под грузоподъёмность пары.
    for lmt in range(limit, 0, -1):
        robot_selection(data, limit)

    return platform_count


if __name__ == '__main__':

    # Считываем вводимые данные: вес роботов в одной строке,
    # Максимальный допустимый вес на платформе - во второй.
    data = tuple(map(int, stdin.readline().rstrip().split()))
    limit = int(stdin.readline().rstrip())

    result = main(data, limit)   # Записываем результат выполнения функции.
    print(result)  # Выводим результат на экран.
