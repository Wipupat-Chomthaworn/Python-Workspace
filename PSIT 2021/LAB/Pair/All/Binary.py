"""main"""
def main():
    """main"""
    var = int(input())
    varx = 0
    keep = ''
    for i in range(10, -1, -1):
        varx = 2**(i)
        if var - varx >= 0:
            keep += '1'
            var -= varx
        else:
            keep += '0'
    print(keep[keep.find('1'):])
main()
