# Просмотр логов

Проект тестировался на Python 3-11 и Django 4-2.
Взаимодействие с БД осуществляется посредством Django ORM, по умолчанию использует SQlite.
При необходимости использовать иную СУБД (PostgreSQL, MariaDB) необходимо переопределить переменную DATABASES в settings проекта, и доустановить необходимые модули.

Запус проекта:
<ol>
<li>Установка виртаульного окружение и необходимых зависимостей</li>
<li>Запуск проекта</li>
<li>Наполнение БД</li>
</ol>

### 1. Установка виртаульного окружение и необходимых зависимостей

```commandline
git clone https://github.com/Sambo312/log_parser.git
cd log_parser
```
В проекте мы полагаемся на классический venv.
```commandline
python3 -m venv venv
source venv/bin/activate
```
Обновляем pip
```bash
python -m pip install --upgrade pip
```
Устанавливаем зависимости
```commandline
pip install -r log_parser/requirements.txt
```

Можно определить переменные окружения (либо создать файл `local_settings.py` в котором их переопределить):
```bash
DJANGO_KEY=my_secret_key
RESPONSE_LIMIT=100
DEBAG=False
ALLOWED_HOSTS=127.0.0.1,127.0.0.2
```

### 2. Запуск проекта

Запуск осуществляется по классической схеме django:
```commandline
python3 log_parser/manage.py runserver
```
Обратите внимание, что в процессе может понадобиться запустить миграции

```commandline
python3 log_parser/manage.py migrate
```

### 3. Наполнение БД

Для наполнения БД создана менедж команда загрузки:
```commandline
python3 log_parser/manage.py log_upload --file `полный путь к файлу`
```
