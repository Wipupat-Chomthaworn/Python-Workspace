"""main"""
def main():
    """main"""
    start = None
    pev = None
    ans = ''
    while True:
        num = int(input())
        if num == -1:
            break
        if start == None:
            start = num
            pev = num
            continue

        else:
            if pev != num-1:
                if start == pev:
                    ans += '%d, '%(start)
                else:
                    ans += '%d-%d, '%(start, pev)
                start = num
                pev = num
            else:
                pev = num
    if start != None:
        if start == pev:
            ans += '%d, '%(start)
        else:
            ans += '%d-%d, '%(start, pev)
    # print(ans)
    print(ans.strip(", "))
main()
