"""main"""
def main():
    """main"""
    keep = int(input())
    print('+++%s-'%keep, end='')
    while True:
        keep += 1
        var = int(input())
        if var == -1:
            break
        if var == keep:
            keep = var
            print('+++%s'%keep)
        else:
            keep = var
            print('+++%s'%var, end='')

main()
