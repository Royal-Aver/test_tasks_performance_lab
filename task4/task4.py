"""
Программа вычисляет минимальное количество ходов для
приведения всех элементов списка к одному числу.
За один ход элемент может быть увеличен или уменьшен на 1.
"""
import sys


def convert_txt_in_list(path):
    """Преобразует содержимое текстового файла в список чисел."""
    with open(path, encoding="utf-8") as file:
        nums = [int(num.strip()) for num in file]
        return nums


def min_moves_to_equal_elements(nums: list):
    """Вычисляет минимальное количество ходов для приведения
       всех элементов списка к одному числу."""
    nums.sort()
    median = nums[len(nums) // 2]
    count = 0

    for num in nums:
        if num < median:
            count += median - num
        elif num > median:
            count += num - median

    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Введите путь до файла!")
        sys.exit(1)

    file_path = sys.argv[1]

    list_nums = convert_txt_in_list(file_path)
    min_num_of_moves = min_moves_to_equal_elements(list_nums)
    print(min_num_of_moves)
