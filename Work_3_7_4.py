n = int(input())
position = [0,0]
for i in range(n):
    cmd = input()
    ls = cmd.split()
    if ls[0] == "север":
        position[1] += int(ls[1])
    elif ls[0] == "запад":
        position[0] += int(ls[1])
    elif ls[0] == "юг":
        position[1] += int(ls[1])
    elif ls[0] == "восток":
        position[0] += int(ls[1])

print(position[0], position[1])