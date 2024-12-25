1. Склонируйте репозиторий на свой локальный компьютер:
git clone <URL_РЕПОЗИТОРИЯ>
cd <ИМЯ_ПРОЕКТА>

2. Создайте виртуальное окружение для изоляции зависимостей проекта:
python -m venv venv

3. Активируйте виртуальное окружение:
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

4. После активации виртуального окружения установите зависимости из файла requirements.txt:
pip install -r requirements.txt

5. Для запуска task1 введите в консоли:
python task1/task1.py <аргумент1> <аргумент2>
Например:
python task1/task1.py 5 4
