# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.

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
# print(my_list)
# new_list = []
# a = [10, 20, 30, 40]
# for id, item in enumerate(my_list):
#     int(id) / 2
#     if int(id) % 2 > 0:
#         new_list.append((my_list[id]))
#     else:
#         x = (my_list[id][::-1])
#         new_list.append(x)
#
# print(new_list)


# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".

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
# new_list = []
#
# for a in my_list:
#     print(a)
#     if a[0] == "a":
#         new_list.append(a)
# print(new_list)

# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
#
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
# new_list = []
#
# for a in my_list:
#     print(a)
#     for aa in a:
#         if aa == "a":
#             new_list.append(a)
# # print(new_list)
# new_set = set(new_list)
# result = list(new_set)
# print(result)


# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]

my_list = [
    {"name": "John", "age": 32},
    {"name": "Jimm", "age": 17},
    {"name": "Jerry", "age": 84},
    {"name": "Jamal", "age": 17},
    {"name": "Jack", "age": 45},
]

# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.

# name_list = []
# age = my_list[0]["age"]
#
# for my_dict in my_list:
#     if my_dict["age"] < age:
#         name_list.clear()
#         age = my_dict["age"]
#     if my_dict["age"] == age:
#         name_list.append(my_dict["name"])
# print(name_list)


###### Вариант первый, рабочий, но не эффективный ######
# new_list =[]
# def get_age(dictionary):
#     return dictionary['age']
#
# # print(my_list)
# my_list.sort(key=get_age)
# # print(my_list)
# new_list.append(my_list[0]["name"])
# # print(new_list)
#
# for list in my_list:
#     if list.get("age") == my_list[0]["age"] and list.get("name") != my_list[0]["name"]:
#         new_list.append(list["name"])
# print(new_list)
########################################################


# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.


# name_list = []
# count = my_list[0]["name"].count('')
# print(count)
#
# for length in my_list:
#     if length["name"].count('') > count:
#         print(length["name"].count(''))
#         name_list.clear()
#         count = length["name"].count('')
#     if length["name"].count('') == count:
#         name_list.append(length["name"])
#
# print(name_list)


# в) Порахувати середню вік усіх людей із початкового списку.


# age_list = []
#
# for age in my_list:
#     age_list.append(age["age"])
# mid_age = sum(age_list) / len(age_list)
# print(mid_age)


# 5) Дано два словники my_dict_1 і my_dict_2.

my_dict_1 = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    7: "s",
}
my_dict_2 = {
    3: "e",
    4: "f",
    5: "g",
    6: "h",
}

# а) Створити список із ключів, які є в обох словниках.


### Работает, но меня осенило как проще.. ###
# key_list_1 = []
# key_list_2 = []
#
# for fkey in my_dict_1:
#     key_list_1.append(fkey)
# for skey in my_dict_2:
#     key_list_2.append(skey)
# result_list = list(set(key_list_1).intersection(set(key_list_2)))
# print(result_list)

### так что решение ниже ###

# key_list = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
# print(key_list)


# б) Створити список із ключів, які є у першому, але немає у другому словнику.


# key_list = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# print(key_list)


# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.


# new_dict = {}
# key_list = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# for key in key_list:
#     new_dict.update({key: my_dict_1[key]})
# print(new_dict)


# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# new_dict = my_dict_1.copy()
# for key, val in my_dict_2.items():
#     if new_dict.get(key):
#         new_dict[key] = [new_dict[key], val]
#     else:
#         new_dict[key] = val
# print(new_dict)




