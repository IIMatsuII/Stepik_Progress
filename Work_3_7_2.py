s = str(input())
q = []

for i in range(len(s)):
    si = s[i]
    q.append(si)

w = []
n = str(input())

for j in range(len(s)):
    sj = n[j]
    w.append(sj)

p = {}
for pi in range(len(s)):
    keys = s[pi]
    p[keys] = 0

j_1 = 0
for i in range(0, len(q)):
    keys = q[i]
    while j_1 < len(w):
        bj = w[0]
        if keys in p:
            p[keys] = bj
        w.remove(bj)
        break
c = []
si = str(input())

for si1 in range(0, len(si)):
    ci = si[si1]
    c.append(ci)

co = []
for ci in range(0, len(c)):
    if c[ci] in p:
        cco = c[ci]
        pco = p[cco]
        co.append(pco)

d = []
di = str(input())

for sj1 in range(0, len(di)):
    dj = di[sj1]
    d.append(dj)

do = []

for di in range(0, len(d)):
    for key in p:
        pkey = key
        if p.get(key) == d[di]:
            ddo = pkey
            do.append(ddo)

for i in range(0, len(co)):
    print(co[i], end = '')
print()

for j in range(0, len(do)):
    print(do[j], end = '')
