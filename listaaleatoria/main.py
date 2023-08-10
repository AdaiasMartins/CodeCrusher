import randrange, shuffle

def createBoard(l, c, u):
    list = [[randrange(0, u) for _ in range(c)] for _ in range(l)]
    return list

l = 6
c = 7
u = 6

list2d = createBoard(l, c, u)
for line in list2d:
    print(line)

