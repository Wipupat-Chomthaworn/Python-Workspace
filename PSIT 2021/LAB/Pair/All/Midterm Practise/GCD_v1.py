"""main"""
def main():
    """main"""
    var = int(input())
    lvar = []
    var2 = int(input())
    minvar = min(var, var2)
    if var == 0 or var2 == 0:
        print(max(var, var2))
    else:
        for i in range(1, minvar+1):
            if var % i == 0 and var2 % i == 0:
                lvar.append(i)
        print(max(lvar))
main()
