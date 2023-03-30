
# value_list = ["d", "h", "d", "r"]
# value_list = [1, 23, 4, 5, 6]
# print(value_list)
# value_set = set(value_list)
# print(value_set)
# value_set = set()
# val_set_1 = {1, 2, 3}
# val_set_2 = {11, 2, 31, 3}
#
# result = val_set_2.difference(val_set_1) # мінусує всі уікальні ПОРЯДОК ВАЖЛИВИЙ
# print(result)
#
# result = val_set_1.intersection(val_set_2) # виводить лише спільні значення
# print(result)


res = False

if len(text.replace(" ", "")) == 0:
    res = True
else:
    if text[0].isdecimal():
        res = True
        if text.replace(" ", "").isdecimal():
            res = True
    if text.isalpha():
        if text.isupper():
            res = True
        if text.islower():
            res = False
        else:
            res = False



