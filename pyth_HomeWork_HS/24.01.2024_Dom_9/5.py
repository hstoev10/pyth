# 5. Използване на библиотеката os за взаимодействие с
# операционната система:
# Задача: Използвайте os за намиране на
# текущата работна директория и промяна на директорията.

import os

# Намиране на текущата работна директория
current_directory = os.getcwd()
print("Текуща работна директория:", current_directory)

# Промяна на директорията (пример: промяна на директорията на рабоата)
new_directory = "/path/to/new/directory"
os.chdir(new_directory)

# Повторно намиране на текущата работна директория след промяна
current_directory_after_change = os.getcwd()
print("Текуща работна директория след промяна:", current_directory_after_change)
