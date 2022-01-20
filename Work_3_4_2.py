#Открываем файл и читаем содержимое
inf = open('D:/GitHub/dataset_3363_3.txt', 'r')
s1 = inf.readline()
s2 = inf.readline()
inf.close()
#открывем фаил и выполняем программу при закрытии ответ перезапишится на другой файл
with open('D:/GitHub/dataset_3363_3.txt') as inf, open('D:/GitHub/MostPopularWord.txt','w') as out:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    out.write(result_word +' ' + str(maxc))

