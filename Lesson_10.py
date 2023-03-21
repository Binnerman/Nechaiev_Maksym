# Всі пункти зробити як окремі функції та їх виклики.

autors = "autors.txt"
domains = "domains.txt"
names = "names.txt"

# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).


# def domaination(name=domains):
#     with open(name, 'r') as my_file:
#         data = my_file.readlines()
#         my_list = []
#         for i in list(data):
#             x = i.replace(".", "").replace("\n", "")
#             my_list.append(x)

#     return my_list

# print(domaination())


# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"



# def surnamation(name=names):
#     with open(name, "r") as my_file:
#         data = my_file.readlines()
#         sur = []
#         for i in list(data):
#             x = i.split("\t")
#             sur.append(x[1])
#
#         return sur
#
# print(surnamation())


# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

#
# def dateination(name=autors):
#     with open(name, "r") as my_file:
#         data = my_file.readlines()
#         my_list = []
#         for i in list(data):
#             x = i.split(" - ")
#             if "\n" not in x[0]:
#                 y = {"date": x[0]}
#                 my_list.append(y)
#
#         return my_list
#
# # print(dateination())


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]

# from datetime import datetime
#
# x = '1st January 1919'
# x1 = x.replace("st", "")
# x2 = x1.replace(" ", "/")
# print(x2)
#
# f = datetime.strptime(x2, "%d/%B/%Y")
# d = datetime.strftime(f, "%d/%m/%Y")
# print(d)


# def dateination(name=autors):
#     from datetime import datetime
#     with open(name, "r") as my_file:
#         data = my_file.readlines()
#         my_list = []
#         for i in list(data):
#             x = i.split(" - ")
#             if "\n" not in x[0]:
#                 f = x[0].split()
#                 f[0] = f[0].replace("st", "").replace("th", "").replace("nd", "").replace("rd", "")
#                 date = "/".join(f)
#                 if date.split("/")[0].isdecimal():
#                     fdate = datetime.strptime(date, "%d/%B/%Y")
#                     f2date = fdate.strftime("%d/%m/%Y")
#                 else:
#                     fdate = datetime.strptime(date, "%B/%Y")
#                     f2date = fdate.strftime("%m/%Y")
#                 print(f2date)
#                 y = {"date_original": x[0], "date_modified": f2date, }
#                 my_list.append(y)
#
#         return my_list
#
# print(dateination())