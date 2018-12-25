# Что тебе нужно
- [Python 3](https://www.python.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- Должен работать pip
- virtualenv
- Django
- [Git (можно с GitBash)](https://git-scm.com/download/win)

## Как работать с pip
```bash
pip install Django  # установить Django последней версии
pip freeze  # выводит на экран установленные зависимости
```

## Как работать с virtualenv
### Установка
```bash
pip install virtualenv 
```

### Создание виртуального окружения
```bash
virtualenv venv
# для линукса: 
# virtualenv -p python3 venv
```

### Активация виртуального окружения
```bash
venv\Scripts\activate.bat
# for linux
# source venv/bin/activate
```

### requirement.txt
Это файл с перечисленными зависимостями.

Зафиксировать зависимости в файл.
```bash
pip freeze > requirements.txt
```

Установить зависимости.
```bash
pip install -r requirements.txt
```

## manage.py
### Запуск сервера (сайта, etc whatever)
```bash
python manage.py runserver
```

## Git
- команды настройки
- init
- status
- add
- commit
- push
- pull
- fetch
- checkout
- rm
- (пока хватит с тебя)

## TODO:
- Разобраться с __init__.py: что такое пакет и зачем он нужен?
- Изучить материалы с сайта [DjangoGirls](https://tutorial.djangogirls.org/ru/)
- Git basic commands