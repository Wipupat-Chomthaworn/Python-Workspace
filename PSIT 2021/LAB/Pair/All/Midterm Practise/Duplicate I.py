"""main"""
def main():
    """main"""
    varm = int(input())
    setm = set()
    setn = set()
    varn = int(input())
    for _ in range(varm):
        setm.add(input())
    for _ in range(varn):
        setn.add(input())
    dup = sorted(list(setm.intersection(setn)), reverse=True)
    if len(dup) > 0:
        for i in dup:
            print(i)
    else:
        print('Nope')

main()
