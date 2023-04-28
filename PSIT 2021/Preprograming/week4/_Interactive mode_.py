'''Interactive mode'''
# def pri():
#     '''Pyramid'''
#     if var.count('print') > 0:
#         print('>>> print("%s")')
#         print(var)
# def intt():
#     '''Pyramid'''
#     if var.count('int') > 0:
#         print('>>> int("%s")')
#         print(var)
def main():
    '''ab'''
    excit = ''
    var = ''
    keep = ''
    def pri(var1):
        '''Pyramid'''
        if var1.count('print') > 0:
            print('>>> print("%s")'%(var1))
            print(var1)
        elif var1.count('intput') > 0:
            print('>>> intput(%s)'%(var1))
            print(var1)
        elif var1.count('int') > 0:
            print('>>> int(%s)'%(var1))
            print(var1)
        elif keep.count(var1) == 0:
            print("NameError: name '%s' is not defined"%(var1))
    while True:
        var = input()
        excit = var
        keep += ','+var
        pri(var)
        if excit.count('exit()') <= 0:
            break
main()
