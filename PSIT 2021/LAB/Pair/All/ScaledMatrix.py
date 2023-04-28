"""main"""
def matric():
    """main"""
    varm = int(input())
    varn = int(input())
    lst = []
    lst2 = []
    for _ in range(varm):
        for _ in range(varn):
            var = float(input())
            if var >= 0 and var <= 1:
                lst2.append(var)
        lst.append(lst2)
        lst2 = []
    for i in lst:
        print(*i, sep=" ")
matric()
