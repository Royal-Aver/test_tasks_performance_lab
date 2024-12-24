"""
Программа определяет положение точки относительно окружности.
"""
import sys


def get_coordinates_of_circle_center_and_radius(file_path: str) -> tuple:
    """Получаю координаты центра окружности и его радиус."""
    with open(file_path, encoding="utf-8") as file:
        x, y = map(int, file.readline().split())
        radius = file.readline()
        return x, y, radius


def get_coordinates_points(file_path: str) -> list:
    """Возвращает интервалы кругового массива."""
    pass


def get_points_positions(circle: tuple, points: list):
    """Возвращает данные о положении точек относительно окружности."""
    pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Введите 2 название двух файлов")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_data = get_coordinates_of_circle_center_and_radius(circle_file)

    points_data = get_coordinates_points(points_file)

    points_positions = get_points_positions(circle_data, points_data)

    print(circle_file)
    print(points_file)