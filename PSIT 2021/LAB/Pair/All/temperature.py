"""temperature"""
def main():
    """main function"""
    tem = float(input())
    type1 = input()
    type2 = input()
    if type1 == 'C':
        cel = tem
        fah = tem*(9/5) + 32
        kel = tem + 273.15
        ran = kel * (9/5)
    elif type1 == 'F':
        fah = tem
        cel = (tem - 32)/ (9/5)
        kel = cel + 273.15
        ran = kel * (9/5)
    elif type1 == 'K':
        kel = tem
        cel = tem - 273.15
        fah = cel * (9/5) + 32
        ran = tem * (9/5)
    elif type1 == 'R':
        ran = tem
        kel = tem / (9/5)
        cel = kel - 273.15
        fah = cel*(9/5) + 32

    if type2 == 'F':
        print('%.2f'%fah)
    elif type2 == 'K':
        print('%.2f'%kel)
    elif type2 == 'R':
        print('%.2f'%ran)
    elif type2 == 'C':
        print('%.2f'%cel)
    else:
        print('%.2f'%tem)
main()
