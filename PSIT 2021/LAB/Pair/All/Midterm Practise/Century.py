"""main"""
def main():
    """main"""
    ans = 0
    for _ in range(int(input())):
        var = input()
        typ = var[:5].strip().upper()
        year = int(var[4:].strip())
        if typ == "B.E.":
            year -= 543
        # print(year)
        ans = int(year) // 100
        if int(year) % 10 != 0 or int(year) % 100 != 0 or int(year) == 0:
            ans += 1
        if year < 0:
            print('ERROR')
        else:
            print(ans)

main()
