numbers = [int(n) for n in input().split()]
conter = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        conter += 1
print(conter)