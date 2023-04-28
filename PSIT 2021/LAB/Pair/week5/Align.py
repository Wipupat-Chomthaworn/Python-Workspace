"""Align"""
def main():
    """Main"""
    var1 = int(input())
    var2 = input().lower()
    var3 = input()
    rest = var1-len(var3)
    if var2 == 'left':
        print(var3.ljust(var1))
    elif var2 == 'right':
        print(var3.rjust(var1))
    elif var2 == 'center':
        if (var1-len(var3))%2 != 0:
            print(' '*(rest//2+1)+ var3)
            # ans = str(var3.center(var1, ' '))
            # print(' '+ans[:-1])
        else:
            print(var3.center(var1, ' '))
main()
