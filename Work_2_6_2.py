a = int(input('Введите число: '))#Вводим значение a
lis = []# создаем пустой список
for i in range(1, a+1):# цикл от 1 до а+1
    for j in range(1, i+1):# цикл от 1 до i+1
        lis.append(i)# заносим в список значение i
print(*lis[:a])# вывод результата