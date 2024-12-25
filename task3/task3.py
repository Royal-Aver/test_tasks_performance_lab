import json
import sys

from docx import Document


def converts_doc_file_to_json(doc_file: str, json_file: str):
    """Конвертирует содержимое .docx файла в JSON."""
    doc = Document(doc_file)
    text = "\n".join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip())

    data = json.loads(text)

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Файл {doc_file} успешно преобразован в {json_file}")


def converts_json_to_dict(json_file: str):
    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)
        print(f"Файл {json_file} успешно преобразован в словарь")
        return data


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
