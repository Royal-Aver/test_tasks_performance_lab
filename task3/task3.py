"""
Программа считывает данные из файла docx
и заполняет словарь данными их другого словаря.
"""
import json
import sys

from docx import Document


def converts_doc_file_to_json(doc_file: str, json_file: str):
    """Конвертирует содержимое .docx файла в JSON."""
    doc = Document(doc_file)
    text = "\n".join(
        paragraph.text for paragraph
        in doc.paragraphs if paragraph.text.strip())

    data = json.loads(text)

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Файл {doc_file} успешно преобразован в {json_file}")


def converts_json_to_dict(json_file: str):
    """Конвертирует содержимое .json файла в dict"""
    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)
        print(f"Файл {json_file} успешно преобразован в словарь")
        return data


def create_report_dict(test_dict: dict, values: dict):
    """Наполняет словарь tests данными из словаря values"""
    for test in test_dict:
        # Обновляем значение текущего теста в tests_dict
        if test['id'] in values:
            test['value'] = values[test['id']]

        # Если есть вложенные тесты, обновляем их
        if 'values' in test:
            create_report_dict(test['values'], values)

    return test_dict


def convert_report_dict_to_json(report: dict):
    """Конвертирует содержимое dict в JSON файл."""
    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

    print("Данные записаны в report.json")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Введите 3 аргумента!")
        sys.exit(1)

    values_doc = sys.argv[1]
    tests_doc = sys.argv[2]
    report_json = sys.argv[3]

    values_json = "values.json"
    tests_json = "tests.json"

    converts_doc_file_to_json(values_doc, values_json)
    converts_doc_file_to_json(tests_doc, tests_json)

    values_dict = converts_json_to_dict(values_json)
    tests_dict = converts_json_to_dict(tests_json)

    values_map = {val["id"]: val["value"] for val in values_dict["values"]}

    report_dict = create_report_dict(tests_dict["tests"], values_map)

    convert_report_dict_to_json(report_dict)
