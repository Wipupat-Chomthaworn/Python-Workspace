"""main"""
def main():
    """main"""
    wit = int(input())
    sit = int(input())
    look = int(input())
    run1 = int(input())
    wit2 = int(input())
    sit2 = int(input())
    run2 = int(input())
    look2 = int(input())
    day = 0
    kwit = 0
    ksit = 0
    klook = 0
    krun = 0
    while True:
        day += 1
        kwit += wit2
        ksit += sit2
        klook += look2
        krun += run2
        # print(kwit, ksit, klook, krun)
        if kwit >= wit and ksit >= sit and klook >= look and krun >= run1:
            break
    print(day)
main()
