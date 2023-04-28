"""Key"""
def main():
    """Main"""
    var1 = input()
    sumvar = 0
    for i in var1:
        sumvar += int(i)
    var = int(var1[10:13])*10
    ans = sumvar+var
    if ans < 1000:
        print(ans+1000)
    elif len(str(ans)) > 4:
        print(str(ans)[-4:])
    else:
        print(ans)
main()
