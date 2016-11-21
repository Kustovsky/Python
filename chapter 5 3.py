# Переводчик с гикского на русский
# Демонстрирует использование словарей
# geek = {"404": "Не знать. не владеть информацией.", "qwerty": "Первые 5 символов в верхнем ряду"}
# print(geek["404"])
# >>>Не знать. не владеть информацией.

# Кто твой батя
FAMILY = {"Виктор": "Александр",
          "Александр": "Николай",
          "Валера": "Даниил"}

choice = None
while choice != "0":
    print(
        '''
    Меню программы
    0 - Выход
    1 - Найти батю
    2 - Добавить пару
    3 - Изменить пару
    4 - Удалить пару
    '''
    )
    choice = input("Ваш выбор: ")
    print()

    # Выход
    if choice == "0":
        print("Bye")

    # Найти батю
    elif choice == "1":
        son = input("Чьего батю вы хотите найти? ")
        if son in FAMILY:
            batya = FAMILY[son]
            print("\n", son, " - ", batya)
        else:
            print("Твоя мать шлюха, а ты приемный")

    # Добавление пары
    elif choice == "2":
        son = input("Назовись : ")
        if son not in FAMILY:
            batya = input("Назови батю: ")
            FAMILY[son] = batya
            print("\nСын был добавлен в семью")
        else:
            print("\nТакой сын уже есть!")

    # Изменить пару
    elif choice == "3":
        son = input("Какую пару вы хотите переопределить? ")
        if son in FAMILY:
            batya = intput("Впишите батю: ")
            FAMILY[son] = batya
            print("\nСын", son, "переопределет")
        else:
            print("\nТакого сына пока нет. Добавь его.")

    # Удалить пару
    elif choice == "4":
        son = input("Какую пару вы хотите удалить? ")
        if son in FAMILY:
            del FAMILY[son]
            print("\nСын ", son, " удален")
        else:
            print("\nСына нет в базе")

    # Непонятный ввод
    else:
        print("В меню нет такого пункта")
    input("\n\nEnter чтобы выйти.")