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


def dateination(name=autors):
    with open(name, "r") as my_file:
        data = my_file.readlines()
        my_list = []
        for i in list(data):
            x = i.split(" - ")
            if "\n" not in x[0]:
                y = {"date": x[0]}
                my_list.append(y)

        return my_list

print(dateination())
