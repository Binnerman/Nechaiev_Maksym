# Для завданнь 1-7 за основу можете взяти код із попередніх ДЗ.
#
# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.
#
# my_list = [
#     "asd",
#     "qwe",
#     "zxc",
#     "ryt",
#     "fgh",
#     "vbn",
#     "uoi",
#     "jlk",
#     "nnb",
# ]
#
# def task_1(my_list):
#     new_list = []
#     for id, item in enumerate(my_list):
#         int(id) / 2
#         if int(id) % 2 > 0:
#             new_list.append((my_list[id]))
#         else:
#             x = (my_list[id][::-1])
#             new_list.append(x)
#     return new_list
#
# print(task_1(my_list))


# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".


# my_list = [
#     "asd",
#     "qwe",
#     "zxc",
#     "ryt",
#     "agh",
#     "vbn",
#     "uoi",
#     "jak",
#     "nna",
# ]

# def task_2 (my_list):
#     new_list = []
#     for a in my_list:
#         if a[0] == "a":
#             new_list.append(a)
#
#     return new_list
#
# print(task_2(my_list))


# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.


# my_list = [
#     "asd",
#     "qwe",
#     "zxc",
#     "ryt",
#     "agh",
#     "vbn",
#     "uoi",
#     "jak",
#     "nna",
# ]

# def task_3 (my_list):
#     new_list = []
#     for a in my_list:
#         for aa in a:
#             if aa == "a":
#                 new_list.append(a)
#     result = list(set(new_list))
#
#     return result
#
# print(task_3(my_list))


# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі
#    числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.

# my_list = [
#     "34",
#     1,
#     2,
#     3,
#     "11",
#     "22",
#     33,
#     "24"
# ]

# def task_4 (my_list):
#     new_list = []
#     for i in my_list:
#         if type(i) == str:
#             new_list.append(i)
#
#     return new_list
#
# print(task_4(my_list))


# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.


# my_str = input("Give me something: ")

# def task_5 (my_str):
#     my_list = list(set(my_str))
#
#     return my_list
#
# print(task_5(my_str))


# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.


# my_str_1 = input("Give me something first: ")
# my_str_2 = input("Give me something second: ")
#
# def task_6 (my_str_1, my_str_2):
#     my_list = list(set(my_str_1).intersection(set(my_str_2)))
#     return my_list
#
# print(task_6(my_str_1, my_str_2))


# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.


# # my_str_1 = input("Give me something first: ")
# # my_str_2 = input("Give me something second: ")

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"

# def task_7 (my_str_1, my_str_2):
#     my_set_1 = set(my_str_1)
#     my_set_2 = set(my_str_2)
#     for o in my_str_1:
#         count = 0
#         for j in my_str_2:
#             if j == o:
#                 count += 1
#         if count > 2:
#             my_set_1.discard(o)
#     for o in my_str_2:
#         count = 0
#         for j in my_str_1:
#             if j == o:
#                 count = count + 1
#         if count > 2:
#             my_set_2.discard(o)
#     my_list = list(my_set_1.intersection(my_set_2))
#     return my_list
#
# print(task_7(my_str_1, my_str_2))


# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.

import random
import string
def mailation ():
    name = random.choice(["king", "miller", "kean", "bryan", "malfoi", "gustav", "jimbei"])
    dom = random.choice(["net", "com", "ua", "dou", "info", "org", "su", "biz"])
    num = random.randint(100, 999)
    e_mail = ""
    rn = random.randint(5, 7)
    for i in range(0, rn):
        e_mail += e_mail.join(random.choice(string.ascii_lowercase))
    mail = f"{name}.{num}@{e_mail}.{dom}"

    return mail

print(mailation())


# Приклад використання функції:
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
#
# Відповідь: miller.249@sgdyyur.com
