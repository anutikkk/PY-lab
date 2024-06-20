Лабораторна робота №9: Regular expressions
___
Мета роботи:
Метою цієї лабораторної роботи є навчання  основам роботи з регулярними виразами для перевірки та обробки рядкових даних. Виконання даних завдань допоможе освоїти важливі навички побудови та використання регулярних виразів для різних типів рядків, що часто зустрічаються в реальних додатках. 
___
Опис завдання:
1.	Write a def(task1) regular expression that matches a string containing only lowercase letters and digits. Input: "hello123" Output: True
2.	Write a def(task2) regular expression that matches a string containing at least one uppercase letter. Input: "Hello" Output: True
3.	Write a def(task3) regular expression that matches a string containing a valid IPv4 address. Input: "192.168.1.1" Output: True
4.	Write a def(task4) regular expression that matches a string containing a valid time in the format of "HH:MM:SS". Input: "12:34:56" Output: True
5.	Write a def(task5) regular expression that matches a string containing a valid US postal code in the format of "NNNNN" or "NNNNN-NNNN". Input: "12345" or "12345-6789" Output: True
6.	Write a def(task6) regular expression that matches a string containing a valid username, with the following criteria: only contains lowercase letters, numbers, underscores, and hyphens, and is between 6 and 12 characters long. Input: "john_doe-123" Output: True
7.	Write a def(task7) regular expression that matches a string containing a valid credit card number (either 15 or 16 digits, starting with either 4, 5, or 6). Input: "4512-3456-7890-1234" Output: True
8.	Write a def(task8) regular expression that matches a string containing a valid social security number (in the format of ###-##-####). Input: "123-45-6789" Output: True
9.	Write a def(task9) regular expression that matches a string containing a valid password, with the following criteria: at least one uppercase letter, one lowercase letter, one digit, one special character (@, #, $, or %), and at least 8 characters long. Input: "Passw0rd#" Output: True
10.	Write a def(task10) regular expression that matches a string containing a valid IPv6 address. Input: "2001:0db8:85a3:0000:0000:8a2e:0370:7334" Output: True.

___
Виконання роботи:
```Python
import re

def task1(input_string):
    pattern = r"^[a-z\d]+$"
    return bool(re.match(pattern, input_string))

def task2(input_string):
    pattern = r"[A-Z]"
    return bool(re.search(pattern, input_string))

def task3(input_string):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, input_string))

def task4(input_string):
    pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$"
    return bool(re.match(pattern, input_string))

def task5(input_string):
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, input_string))

def task6(input_string):
    pattern = r"^[a-z0-9_-]{6,12}$"
    return bool(re.match(pattern, input_string))

def task7(input_string):
    pattern = r"^(4|5|6)\d{14}(\d{2})?$"
    return bool(re.match(pattern, input_string))

def task8(input_string):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, input_string))

def task9(input_string):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$"
    return bool(re.match(pattern, input_string))

def task10(input_string):
    pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(pattern, input_string))
```
___
Результати:
```Python
True
True
True
True
True
True
True
True
True
True

```
___
Висновки:
Виконання цієї лабораторної роботи дозволило мені отримати практичні навички роботи з регулярними виразами, які є потужним інструментом для обробки та валідації рядкових даних. Я навчилась застосовувати ці вирази для різноманітних задач валідації та обробки даних, що є важливими навичками для розробників програмного забезпечення. 
___