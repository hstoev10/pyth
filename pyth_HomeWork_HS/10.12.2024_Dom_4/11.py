#Напишете програма, която генерира 100 текстови файла, които имена започват със случайни цифри
#между 1 и 9. След като сте ги генерирали създайте 9 папки наименовани с цифрите между 1 и 9 и
#преместете всички файлове започващи със сответната цифра в съответната папка и накрая
#принтирате на конзолата структурата която се е получила. При приключване на програмата
#изтрийте всички генерирани файлове и папки.

import os
import shutil
import random
import string

# Генериране на случайно име за файл
def generate_random_filename():
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(5)) + ".txt"

# Създаване на 100 файлове
for _ in range(100):
    filename = generate_random_filename()
    with open(filename, 'w') as file:
        file.write("Това е съдържание на файла.")

# Създаване на 9 папки
for digit in range(1, 10):
    folder_name = str(digit)
    os.makedirs(folder_name, exist_ok=True)

# Преместване на файловете в съответните папки
for filename in os.listdir():
    if filename.endswith(".txt"):
        first_digit = filename[0]
        shutil.move(filename, os.path.join(first_digit, filename))

# Принтиране на структурата
for digit in range(1, 10):
    folder_name = str(digit)
    files_in_folder = os.listdir(folder_name)
    print(f"Папка {folder_name}: {files_in_folder}")

# Изтриване на генерираните файлове и папки
for digit in range(1, 10):
    folder_name = str(digit)
    shutil.rmtree(folder_name)

print("Генерираните файлове и папки са изтрити.")
