# 1) У вас є список my_list із значеннями типу int. Роздрукувати значення, які більше 100.
#    Завдання виконати за допомогою циклу for.

# my_list = [
#     14,
#     2324,
#     251,
#     32,
#     32135,
#     31,
#     25,
#     67,
#     976,
#     112,
#     331,
#     516,
# ]
# for hundred in my_list:
#     if hundred > 100:
#         print(hundred)
#     else:
#         pass

# 2) У вас є список my_list зі значеннями типу int і порожній список my_results. Додати в my_results ті значення,
#    які більше 100. Роздрукувати список my_results. Завдання виконати за допомогою циклу for.

# my_list = [
#     14,
#     2324,
#     251,
#     32,
#     32135,
#     31,
#     25,
#     67,
#     976,
#     112,
#     331,
#     516,
# ]
# my_results = []
#
# for hundred in my_list:
#     if hundred > 100:
#         my_results.append(hundred)
#     else:
#         pass
#
# print(my_results)

# 3) У вас є список my_list із значеннями типу int. Якщо my_list кількість елементів менше 2,
#    то в кінець додати значення 0. Якщо кількість елементів більша або дорівнює 2,
#    то додати суму останніх двох елементів. Кількість елементів у списку можна отримати за допомогою функції len(my_list)

my_list = [
    1,
    5,
]
ln = len(my_list)

if ln < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-2] + my_list[-1])

print(my_list)
