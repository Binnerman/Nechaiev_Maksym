# 1.+ Дано ціле число (int). Визначити скільки нулів у цьому числі.


# my_int = int(input('Give me a number: '))
# result = str(my_int).count("0")
# print(result)


# 2.+ Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі


# my_int = int(input('Give me a number: '))
# result = 1
# x = 0
# while x == 0:
#     my_int = my_int / 10
#     y = my_int % 10
#     print(y)
#     if y != 0:
#         x += 1
#     else:
#         result += 1
# print(result)


# 3.+ Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.


# my_list_1 = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
# ]
# my_list_2 = [
#     10,
#     20,
#     30,
#     40,
#     50,
#     60,
# ]
# my_result = []
#
# for i in my_list_1[1::2]:
#     my_result.append(i)
# for j in my_list_2[1::2]:
#     my_result.append(j)
# print(my_result)


# 4.+ Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]


# my_list = [
#     1,
#     2,
#     3,
#     4,
# ]
# x = my_list.pop(0)
# new_list = my_list
# my_list.insert(-1, x)
# print(new_list)


# 5.+ Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)


# my_list = [
#     1,
#     2,
#     3,
#     4,
# ]
# x = my_list.pop(0)
# my_list.reverse()
# my_list.insert(0, x)
# my_list.reverse()
#
# print(my_list)


# 6.+ Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)


# my_str = "43 більше ніж 34, але менше ніж 56."
# result = 0
# num_list = []
# num = ''
#
# my_list = my_str.split(" ")
# print(my_list)
# for word in my_list:
#     # print(word)
#     for symb in word:
#         print(symb)
#         if symb.isdigit():
#             num = num + symb
#             print(num)
#         else:
#             if num != '':
#                 num_list.append(int(num))
#                 num = ''
#         if num != '':
#             num_list.append(int(num))
#
#
# print(num_list)


# my_str = "43 більше ніж a34faf, але менше ніж 56."
# num_list = []
# result = 0
# num = ''
# for char in my_str:
#     if char.isdigit():
#         num = num + char
#     else:
#         if num != '':
#             num_list.append(int(num))
#             num = ''
# if num != '':
#     num_list.append(int(num))
#
# print(num_list)
#
# for n in num_list:
#     result += n
#
# print(result)

# my_list = my_str.split(", ")
# # print(my_list)
# my_str1 = " ".join(my_list)
# # print(my_str1)
#
# my_list1 = my_str1.split(".")
# # print(my_list1)
# my_str2 = " ".join(my_list1)  # И по этому принципу все знаки добавлять заманаешься, но с тем что есть работает."
# # print(my_str2)
#
# my_list = my_str2.split(" ")
# print(my_list)
# ln = len(my_list)
# # print(ln)
#
# for i in range(ln):
#     x = my_list.pop()
#     # print(x)
#     if x.isdigit():
#         result += int(x)
# print(result)


# 7.+ Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.


# my_list = [    #2,4,1,5,3,9,0,7]
#     10,
#     60,
#     40,
#     70,
#     90,
#     20,
#     30,
#     80,
#     20,
#     70,
#     0,
#     50,
#     30,
#     60,
# ]
#
# ln = len(my_list) - 1
# count = 0
#
# for ind in range(1, ln):
#     # print(ind)
#     num = my_list[ind]
#     # print(num)
#     pre = my_list[ind - 1]
#     # print("pre = ", pre)
#     nex = my_list[ind + 1]
#     # print("nex = ", nex)
#     if num > pre + nex:
#         print(num)
#         count += 1
#
# print("Count = ", count)


# 8.+ Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list. -

# my_list = [
#     1,
#     2,
#     3,
#     "11",
#     "22",
#     33,
#     "24"
# ]
# new_list = []
#
# for i in my_list:
#     if type(i) == str:
#         new_list.append(i)
#
# print(new_list)



# string = list(input('String: '))
# new_string = []
#
# for symbol in string:
#     if not symbol.isdigit():
#         new_string.append(symbol)
#
# new_string = ''.join(new_string).strip()
#
# print(new_string)




# 9.+ Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

# my_str = input("Give me something: ")
# my_set = set(my_str)
# my_list = list(my_set)
# print(my_list)

# 10.+ Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

# my_str_1 = input("Give me something first: ")
# my_str_2 = input("Give me something second: ")
# my_set_1 = set(my_str_1)
# my_set_2 = set(my_str_2)
# my_set = my_set_1.intersection(my_set_2)
# my_list = list(my_set)
# print(my_list)

# 11.+ Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу

# my_str_1 = "aaaasdf1"   #input("Give me something first: ")
# my_str_2 = "asdfff2"   #input("Give me something second: ")
#
# my_set_1 = set(my_str_1)
# my_set_2 = set(my_str_2)
#
# for o in my_str_1:
#     count = 0
#     for j in my_str_2:
#         if j == o:
#             count += 1
#     if count > 2:
#         my_set_1.discard(o)
#
# for o in my_str_2:
#     count = 0
#     for j in my_str_1:
#         if j == o:
#             count = count + 1
#     if count > 2:
#         my_set_2.discard(o)
#
# my_set = my_set_1.intersection(my_set_2)
# my_list = list(my_set)
# print(my_list)
