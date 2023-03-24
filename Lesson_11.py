# Всі пункти є частиною одного завдання, тому можна використовувати функції кілька разів та не дублювати код.
# Якщо хочете, можете використовувати дефолтні значення та анотацію типів.

import os
main_dir = "C:/Users/Admin/PycharmProjects/Nechaiev_Maksym/Task_11"
test_path = "Test_fold"
test_file = "Test_file.txt"

# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))

def dictdiration(path):
    dir = os.listdir(path)
    dict = {
        'filenames': [],
        'dirnames': [],
    }
    for i in dir:
        if os.path.isdir(os.path.join(path, i)):
            dict['dirnames'].append(i)
        else:
            dict['filenames'].append(i)

    return dict

# print(dictdiration(main_dir))

# 2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.


# def dictsortion(path, sortling = True):
#     sorting = dictdiration(path)
#     if sortling:
#         sorting['filenames'].sort()
#         sorting['dirnames'].sort()
#     else:
#         sorting['filenames'].sort(reverse=True)
#         sorting['dirnames'].sort(reverse=True)
#
#     return sorting
#
# print(dictsortion(main_dir , False))


# 3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.


def dictupdation(path, new_path):
    dict = dictdiration(path)
    if os.path.splitext(new_path)[1] != "":
        dict['filenames'].append(new_path)
    else:
        dict['dirnames'].append(new_path)

    return dict

print(dictupdation(main_dir, test_file))


# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та ім'я директорії.
# Функція перевіряє відповідність отриманого словника та реальної файлової системи в отриманій папці та,
# якщо треба, створює потрібні папки та порожні файли, відповідно до структури словника.


#                                       (Ні-ні, нема часу, вибачте)
