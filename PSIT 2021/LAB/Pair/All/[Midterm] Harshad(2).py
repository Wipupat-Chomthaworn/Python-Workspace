"""[MID]harshard(2stars)"""
def harshard():
    """FUNC harshard"""
    check = 0
    for _ in range(0, 10):
        data = abs(int(input()))
        for i in str(data):
            check += int(i)
        if check == 0:
            print("No")
        elif int(data) % check == 0:
            print("Yes")
        else:
            print("No")
        check = 0
harshard()
