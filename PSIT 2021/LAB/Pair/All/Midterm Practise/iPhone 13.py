"""iPhone 13"""
def main():
    """main func"""
    var = input()
    i13 = 29900
    pro = 38900
    promax = 42900
    if var == 'iPhone 13 mini':
        print(i13)
    elif var == 'iPhone 13':
        print(pro)
    elif var == 'iPhone 13 Pro':
        print(promax)
    elif var == 'iPhone 13 Pro Max':
        print(promax*2)
    else:
        print(25900)
main()
