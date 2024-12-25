"""
Программа определяет положение точек относительно окружности.
"""
import sys
import math


def get_coordinates_of_circle_center_and_radius(file_path: str) -> tuple:
    """Получаю координаты центра окружности и его радиус."""
    with open(file_path, encoding="utf-8") as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
        return x, y, radius


def get_coordinates_points(file_path: str) -> list:
    """Возвращает интервалы кругового массива."""
    points_list = []
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            x, y = map(float, line.split())
            points_list.append((x, y))
    return points_list


def get_points_positions(circle: tuple, points: list):
    """Возвращает данные о положении точек относительно окружности."""
    x_center, y_center, radius = circle

    for x, y in points:
        distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)

        if distance > radius:
            print(2)
        elif distance < radius:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Введите 2 название двух файлов")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_data = get_coordinates_of_circle_center_and_radius(circle_file)

    points_data = get_coordinates_points(points_file)

    get_points_positions(circle_data, points_data)
