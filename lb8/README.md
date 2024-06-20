Лабораторна робота №8: JSON
___
Мета роботи:
Мета цієї лабораторної роботи полягає в практичному освоєнні роботи з JSON даними в мовах програмування. Завдання покликані навчити основам парсингу JSON файлів, трансформації даних, валідації структури JSON файлів, роботи з вкладеними JSON структурами та оновлення даних у JSON файлах.
___
Опис завдання:
Task 1: JSON Parsing and Data Retrieval
Objective: Parse a JSON file and return a list of names of individuals above a certain age.

Task 2: Data Transformation and JSON Serialization
Objective: Transform a list of dictionaries into a JSON string and write it to a file.

Task 3: JSON Schema Validation
Objective: Validate JSON files against a given schema.

Task 4: Nested JSON Data Handling
Objective: Extract specific information from a complex nested JSON structure.

Task 5: Updating JSON Data
Objective: Update certain fields in a JSON file based on given criteria.
___
Виконання роботи:
```Python
import json


def task1(file_path, age_threshold):
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above_threshold = [entry['name'] for entry in data if entry['age'] > age_threshold]
    return names_above_threshold


def task2(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            try:
                json.load(file)
            except json.JSONDecodeError:
                invalid_files.append(file_path)
    return invalid_files


def task4(file_path, key):
    def _extract_values(obj, key):
        values = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    values.append(v)
                elif isinstance(v, (dict, list)):
                    values.extend(_extract_values(v, key))
        elif isinstance(obj, list):
            for item in obj:
                values.extend(_extract_values(item, key))
        return values

    with open(file_path, 'r') as file:
        data = json.load(file)
    values = _extract_values(data, key)
    return values


def task5(file_path, category, update_function):
    with open(file_path, 'r+') as file:
        data = json.load(file)
        for item in data:
            if item.get('category') == category:
                update_function(item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def increase_price(item):
    if 'price' in item:
        item['price'] += 10

```

___
Результати:
```Python
["John Doe", "Jane Smith", "Alice Johnson"]

[
    {"name": "John Doe", "age": 25, "city": "New York"},
    {"name": "Jane Smith", "age": 30, "city": "San Francisco"}
]

["invalid_data1.json", "invalid_data2.json"]

["123 Main St", "456 Elm St"]

[
    {"name": "Product1", "category": "electronics", "price": 110},
    {"name": "Product2", "category": "electronics", "price": 220}
]

```
___
Висновки:
Виконання цієї лабораторної роботи дозволило мені глибше ознайомитися з основними техніками роботи з JSON даними, які є надзвичайно важливими в сучасній розробці програмного забезпечення, та дало можливість практично застосувати теоретичні знання з роботи з JSON даними. Виконана робота сприяла розвитку розуміння структурованих даних та підвищенню рівня професійної компетенції у цьому питанні. 
___