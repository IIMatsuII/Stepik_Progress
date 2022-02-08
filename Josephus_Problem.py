n, k = int(input()), int(input())
count = list(range(1, n+1))
out = 0

for _ in range(n-1):
    start = out % len(count)
    out = (start + k - 1)%len(count)
    count.remove(count[out])
print(*count)