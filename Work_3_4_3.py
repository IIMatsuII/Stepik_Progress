
count, a1, b1, c1, = 0, 0, 0, 0
with open('D:/GitHub/dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        line = line.strip().split(';')
        a, b, c = int(line[1]), int(line[2]), int(line[3])
        print((a+b+c)/3)
        count += 1
        a1 += a
        b1 += b
        c1 += c
print((a1/count), (b1/count), (c1/count))
