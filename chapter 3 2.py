import random
print("Бросаем монетку сто раз\n")
input("Нажми ENTER, чтобы начать")
i = 100
while i > 0:
    coin = random.randrange(2)
    if coin == 0:
        print("Орел")
    else:
        print("Решка")
    i -= 1