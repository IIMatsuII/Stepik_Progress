know = set()
unknown = set()

for _ in range(int(input())):
    know.add(input().strip().lower())

for _ in range(int(input())):
    for word in input().strip().lower().split():
        if word not in know:
            unknown.add(word)

for word in unknown:
    print(word)