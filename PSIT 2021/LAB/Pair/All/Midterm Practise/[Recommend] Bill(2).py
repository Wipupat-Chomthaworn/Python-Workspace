"""main"""
def main():
    """main"""
    var = int(input())
    ser = var*10/100
    if ser < 50:
        ser = 50
    elif ser > 1000:
        ser = 1000
    else:
        ser = var*10/100
    tax = (var+ser)*7/100
    print('%.2f'%(var+ser+tax))
main()
