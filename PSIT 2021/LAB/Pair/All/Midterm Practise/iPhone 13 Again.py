"""iPhone 13"""
def main():
    """main func"""
    var = input().lower()
    sto = input().lower()
    mini1 = 37900 * (sto == "512 gb") + 29900 * (sto == "256 gb") \
            + 25900 * (sto == "128 gb")
    i131 = 41900 * (sto == "512 gb") + 33900 * (sto == "256 gb") \
           + 29900 * (sto == "128 gb")
    pro1 = 50900 * (sto == "512 gb") + 42900 * \
           (sto == "256 gb") + 38900 * (sto == "128 gb") \
           + (sto == "1 tb") * 58900
    promax1 = 54900 * (sto == "512 gb") + 46900 * \
              (sto == "256 gb") + 42900 * (sto == "128 gb") + \
              (sto == "1 tb") * 62900
    chex = (sto == "512 gb") + (sto == "256 gb") + (sto == "128 gb") + (sto == "1 tb")
    if chex == 0:
        print("Not Available")
    else:
        if var == 'iphone 13 mini':
            if sto == "1 tb":
                print("Not Available")
            else:
                print(mini1)
        elif var == 'iphone 13':
            if sto == "1 tb":
                print("Not Available")
            else:
                print(i131)
        elif var == 'iphone 13 pro':
            print(pro1)
        elif var == 'iphone 13 pro max':
            print(promax1)
        else:
            print("Not Available")
main()
