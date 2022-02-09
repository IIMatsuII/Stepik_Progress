frist, second, three, fore = 0, 0, 0 ,0
for i in range(int(input("Введите количество циклов: "))):
    x,y = (map(int, input("Введите точки координат: ").split()))
    frist += x > 0 and y > 0
    second += x < 0 and y > 0
    three += x < 0 and y < 0
    fore += x > 0 and y < 0

print(f"Первая четверть: {frist}", f"Вторая четверть: {second}", f"Третья четверть: {three}", f"Четвертая четверть: {fore}", sep = "\n")