'''[Recommend] Run Length Decoding'''
def main():
    '''main func'''
    var = input()
    # length = len(var)//2
    # num = var[0:-1:2]
    # alpha = var[1::2]
    a_str = ""
    b = ""
    for i in var:
        if i.isnumeric():
            a_str += i
        else:
            b += i*int(a_str)
            a_str = ""
    print(b)
    # for i in range(length):
    #     print(int(num[i])*alpha[i], end="")
main()
