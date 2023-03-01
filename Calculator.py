first = 0
second = 0
act = 0
result = ""
again = "Так"

while again == "Так":
    try:
        first = float(input('Введіть перше число:'))
    except ValueError:
        try:
            first = float(input('Підходить тільки числове значення:'))
        except ValueError:
            print('Я так рахувати не вмію!')
            quit()
    act = input('Вкажіть математичну дію на вибір: "+" "-" "*" "/" "^"\nВаш вибір:')
    if act != '+' or '-' or '*' or '/':
        print('введи тільки пропоновану дію')

    try:
        second = float(input('Введіть друге число:'))
    except ValueError:
        try:
            second = float(input('Підходить тільки числове значення:'))
        except ValueError:
            print('Я так рахувати не вмію!')
            quit()

    try:
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
            print("Неправильно обрана дія")
    except ArithmeticError:
        print("На нуль ділити не можна - всесвіт сколлапсується!")

    print(result)
    again = input("Якщо бажаєте продовжити напишіть 'Так':")


