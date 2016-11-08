import random
LIST = ["меч", "кольчуга", "щит", "целебное снадобье", "список", "нечто неизвестное", "орыуарпуоыа"]
count = len(LIST)
while count > 0:
    count -= 1
    word = random.choice(LIST)
    print(word)
    LIST.remove(word)