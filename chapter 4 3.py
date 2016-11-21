import random
points = 3
WORDS = ("сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
print("Добро пожаловать в игру 'Анаграммы'")
print("Отгадайте слово, в нем", len(word), "букв")
call_1 = input("\nХотите ли узнать наличие буквы? (Да)\n")
if call_1 == "Да" or "да" and points > 0:
   points -= 1
   position = random.randrange(len(word))
   print(word[position])
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != word and guess != "":
   print("K сожалению. вы неправы.")
   guess = input("Попробуйте отгадать исходное слово: ")
if guess == word:
   print("Дa. именно так! Вы отгадали!\n")
   points += 1
   print("Cnacибo за игру. Вы набрали ", points, "очков")
input("\n\nHaжмитe Enter. чтобы выйти.")