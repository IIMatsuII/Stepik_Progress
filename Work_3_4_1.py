inf = open('D:/GitHub/dataset_3363_2.txt', 'r')
s1 = inf.readline()
s2 = inf.readline()
inf.close()

with open('D:/GitHub/dataset_3363_2.txt') as inf:
    s = inf.readline().strip()
def rep(symbol, iter): return symbol*int(iter)
i = 0
while i < len(s):
    iter = ''
    if s[i].isalpha():
        symbol = s[i]
        i += 1
        while s[i].isdigit():
            iter += s[i]
            if i == len(s) - 1: break
            i += 1
        print(rep(symbol, iter), end='')