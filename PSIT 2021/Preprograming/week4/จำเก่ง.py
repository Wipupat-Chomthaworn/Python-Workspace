"""จำเก่ง"""
def main():
    '''ab'''
    var_1 = (input()).lower()
    keep = ''
    num = 0
    endf = ''
    while True:
        if var_1.isalpha():
            keep += var_1+','
        var_1 = (input()).lower()
        if var_1 == ('end'):
            endf = input().lower()
            num = keep.count(endf)
            print(num)
            break
main()
