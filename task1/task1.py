"""
Программа реализует вывод пути, состоящего из
первых элементов кругового массива заданных интервалов.
"""
import sys


def creates_circular_array(len_num: int) -> str:
    """Создает строковое представление кругового массива."""
    circular_str = ""
    for num in range(1, len_num + 1):
        circular_str += str(num)
    return circular_str


def gets_intervals_of_circular_array(
        circular_array: str,
        len_intervals: int) -> list:
    """Возвращает интервалы кругового массива."""
    lst_intervals = []
    start_index = 0

    for _ in range(len(circular_array)):
        interval = ''.join(circular_array[
                           start_index:start_index + len_intervals])

        if len(interval) < len_intervals:
            interval += ''.join(circular_array[:len_intervals - len(interval)])

        lst_intervals.append(interval)

        start_index = (start_index + len_intervals - 1) % len(circular_array)

        if start_index == 0:
            break

    return lst_intervals


def gets_first_digits_of_items_list(lst_nums: list) -> int:
    """Возвращает строку начальных элементов интервалов."""
    lst = [num[0] for num in lst_nums]
    return int("".join(lst))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Введите 2 числа")
        sys.exit(1)

    try:
        len_arr = int(sys.argv[1])
        len_intervals = int(sys.argv[2])
        if len_arr <= 0 or len_intervals <= 0:
            raise ValueError("Числа должны быть положительными")
        if int(len_arr) < int(len_intervals):
            raise ValueError("Первое число должно быть больше второго")
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

    circular_array = creates_circular_array(len_arr)

    intervals_lst = gets_intervals_of_circular_array(
        circular_array, len_intervals)

    first_digits = gets_first_digits_of_items_list(intervals_lst)
    print(first_digits)
