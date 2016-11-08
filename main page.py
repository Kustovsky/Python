import random
points = 0
WORDS = ("сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
# начало игры
print("Добро пожаловать в игру 'Анаграммы'")
print("Отгадайте слово, в нем", len(word), "букв")
#call = input("Хотите ли узнать наличие буквы? 1.Да 2.Нет")
points = 4
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != word and guess != "":
    print("K сожалению. вы неправы.")
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == word:
    print("Дa. именно так! Вы отгадали!\n")
    points += 1
print("Cnacибo за игру. Вы набрали ", points, "очков")
input("\n\nHaжмитe Enter. чтобы выйти.")