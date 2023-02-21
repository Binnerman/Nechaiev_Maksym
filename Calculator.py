try:
    first = float(input('Введіть перше число:'))
except ValueError:
        try:
            first = float(input('Підходить тільки числове значення:'))
        except ValueError:
            print('Я так рахувати не вмію!')
            quit()

act = input('Вкажіть математичну дію на вибір: "+" "-" "*" "/" "^"\n Ваш вибір:')

try:
    second = float(input('Введіть друге число:'))
except ValueError:
        try:
            second = float(input('Підходить тільки числове значення:'))
        except ValueError:
            print('Я так рахувати не вмію!')
            quit()

if act == '+':
    result = first + second
elif act == '-':
    result = first - second
elif act == '*':
    result = first * second
elif act == '/':
    result = first / second
elif act == "^":
    result = first ** second
else:
    pass

try:
    print(result)
except NameError:
    print("Неправильно обрана дія")
    quit()
