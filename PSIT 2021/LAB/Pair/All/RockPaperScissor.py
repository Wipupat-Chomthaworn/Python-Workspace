"""main"""
def rock(pea, peb):
    """main2"""
    if pea > peb:
        print('A win %d-%d'%(pea, peb))
    elif pea < peb:
        print('B win %d-%d'%(peb, pea))
    else:
        print("DRAW %d"%(peb))
def main():
    """main"""
    var = input().lower()
    rou = 0
    pea = 0
    peb = 0
    keep = ''
    for i in var:
        rou += 1
        if rou%2 != 0:
            keep = i
        else:
            if keep == i:
                keep = ''
            elif keep == 'r' and i == 'p':
                peb += 1
                keep = ''
            elif keep == 's' and i == 'r':
                peb += 1
                keep = ''
            elif keep == 'p' and i == 's':
                peb += 1
            elif i == 'r' and keep == 'p':
                pea += 1
                keep = ''
            elif i == 's' and keep == 'r':
                pea += 1
                keep = ''
            elif i == 'p' and keep == 's':
                pea += 1
    rock(pea, peb)

main()
