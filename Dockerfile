#  Устанавливаем базовый образ
FROM python:3

# Создаем рабочую директорию
WORKDIR /habits_app

# Копируем в рабочую директорию файл с зависимостями проекта
COPY requirements.txt .

# Выполняем команду установки зависимостей проекта
RUN pip install -r requirements.txt

# Копируем проект в контейнер
COPY . .