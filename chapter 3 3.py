import random
number = random.randint(1, 100)
guess = int(input("Ваш вариант: "))
tries = 1
while guess != number:
    if guess > number:
        print("Много")
    else:
        print("Мало")
    guess = int(input("Ваш вариант: "))
    tries += 1
    if tries > 10:
        break

if guess == number:
    print("Ты угадал! Это и правда", number, "Всего за ", tries, " попыток")
else:
    print("Ну ты и тупой.")