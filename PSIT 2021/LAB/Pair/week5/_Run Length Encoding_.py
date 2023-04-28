'''Run Length Encoding'''
def printalp(num, var2):
    print('%d%s'%(num+1, var2), end='')
def main():
    """main function"""
    var = input()
    keep = 0
    last = ''
    for i in range(len(var)):
        if var[i] == last:
            keep += 1
        elif var[i] == last or i == len(var)-1:
            print(printalp(keep, var[i]))
            keep = 0
        last = var[i]
    # print('%d%s'%(keep+1, var[i]), end='')
main()