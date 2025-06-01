# підготовка

```python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Запуск сервера

```python
python manage.py runserver 8001
```

# Перевірка результату

- Відкрити http://127.0.0.1:8001/admin/
- Увійти суперкористувачем
- Будуть "Категорії для публікацій" та "Статті"
- Створити кілька категорій та статей для тестування