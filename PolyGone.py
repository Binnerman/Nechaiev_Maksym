# 1) У вас є рядок my_string = '0123456789'.
# Згенерувати цілі числа (тип int) від 0 до 99 та роздрукувати їх.
# Завдання потрібно виконати через цикл у циклі (див. приклад нижче) та наведення типів.
# Генерування через range або інші "фішки" можна в якості альтернативного вирішення, але спершу через цикл у циклі))
#
#
# #####################################################

my_string_1 = "0123456789"
my_string_2 = "0123456789"
for symb_1 in my_string_1:      # перебирається всі елементи з my_string_2 для елемента "1" з my_string_1
    for symb_2 in my_string_2:  # перебирається всі елементи з my_string_2 для елемента "2" з my_string_1
        print(symb_1 + symb_2)  # складає символи з першої та другої строки

# my_str = '0123456789'
# length = len(my_str) - 1
# #print(length)
# x = int(my_str[0:1])
# print(x)
# y = int(my_str[1:2])
# print(y)

# while x < length:
#     y += 1
#     while y == length:
#         x += 1
#         y += 1
#         print(my_str[x:y])

# length = len(s)
# start = 0
#
# while start < length:
#     search = s.find(ch, start)
#     print(ch, search)
#     if search is not False:
#         start = int(search) + 1
#     else:
#         break