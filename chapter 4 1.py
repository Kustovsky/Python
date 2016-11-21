#Считалка
print("Считаем: ")
x = int(input('X='))
y = int(input('Y='))
z = int(input('Z='))
for i in range(x, y, z):
    print(i, end= " ")