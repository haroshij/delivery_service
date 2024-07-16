# Номер посылки с решениеме на Яндекс.Контесте:
# 116147007.

# Импортируем stdin для более быстрого считывания вводимых данных.
from sys import stdin


def main(data: tuple[int], limit: int) -> int:
    """
    Функция для вычисления минимального количества платформ,
    необходимых для перевозки роботов.
    """

    # Чтобы применить метод двух указатлей, отсортируем роботы по весу.
    data.sort()

    # Счётчик платформ, необходимых для перевозки.
    platform_count = 0

    # Указатели, которые будут двигаться навстречу друг другу из разных концов.
    left = 0
    right = len(data) - 1

    # Внутри цикла двигаем указатели навстречу друг другу:
    # двигаем два указателя, если оба робота помещаются на платформу,
    # двигаем правый указатель, показывающий на тяжёлого робота,
    # в случае, если оба робота не помещаются на платформу.
    while left <= right:
        if data[left] + data[right] <= limit:
            left += 1
        platform_count += 1
        right -= 1

    return platform_count  # Возвращаем необходимое количество платформ.


if __name__ == '__main__':

    # Считываем вводимые данные: вес роботов в одной строке,
    # Максимальный допустимый вес на платформе - во второй.
    data = list(map(int, stdin.readline().rstrip().split()))
    limit = int(stdin.readline().rstrip())

    result = main(data, limit)   # Записываем результат выполнения функции.
    print(result)  # Выводим результат на экран.
