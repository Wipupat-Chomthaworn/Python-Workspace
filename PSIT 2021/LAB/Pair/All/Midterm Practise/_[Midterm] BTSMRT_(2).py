'''[Midterm] BTSMRT'''
def main():
    '''main'''
    day = input().lower()
    age = float(input())
    heights = float(input())
    if day == "children day":
        if age <= 14 and heights <= 140:
            print('FREE')
        else:
            print('PAY')
    elif day == "senior day":
        if age >= 60:
            print('FREE')
        else:
            print('PAY')
    else:
        if age <= 14 and heights < 90:
            print('FREE')
        else:
            print('PAY')
main()
