"""main"""
def main():
    """main"""
    lopn = int(input())
    lopm = int(input())
    seta = set()
    setb = set()
    ans = set()
    for _ in range(lopn):
        seta.add(int(input()))
    for _ in range(lopm):
        setb.add(int(input()))
    ans = seta.difference(setb)
    print(*sorted(ans), sep=" ")
main()
