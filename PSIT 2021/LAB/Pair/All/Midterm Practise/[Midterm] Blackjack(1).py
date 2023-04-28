"""[Midterm] Blackjack"""
def main():
    """main"""
    num = int(input())
    keep = 0
    keepvar = ''

    for _ in range(num):
        var = input()
        keepvar += var
        if var in ("J", "Q", "K"):
            keep += 10
        elif var == "A":
            pass
        else:
            keep += int(var)
    acecounter = keepvar.count("A")

    if acecounter == 3:
        keep = 13
    elif acecounter == 2:
        if keep + 12 > 21:
            keep += 2
        else:
            keep += 12
    elif acecounter == 1:
        if keep +11 > 21:
            keep += 1
        else:
            keep += 11
    print(keep)
main()
