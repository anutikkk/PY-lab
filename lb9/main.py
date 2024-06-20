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
