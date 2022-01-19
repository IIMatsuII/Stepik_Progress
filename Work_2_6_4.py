m = []
while True:
    n = int(input()).split()
    if n[0] == "end":
        break
    else:
        m.append(n)
for i in range(len(m)):
    x = ""
    for j in range(len(m[i])):
        a = int(m[i-1][j])
        if i == len(m) - 1:
            b = int(m[0][j])
        else:
            b = int(m[i+1][j])
        c = int(m[i][j-1])
        if j == len(m[i]) - 1:
            d = int(m[i][0])
        else:
            d = int(m[i][j+1])
        s = a+b+c+d
        x+=str(s)+' '
    print(x.strip())