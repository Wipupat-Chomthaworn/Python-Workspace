'''[Midterm] BTSMRT'''
def main():
    '''main'''
    day = input()
    age = float(input())
    height = float(input())
    cond1 = age < 14 and height < 90
    cond2 = day == 'Children Day' and age < 14 and height <= 140
    cond3 = day == 'Senior Day' and age >= 60
    if cond1 or cond2 or cond3:
        print('FREE')
    else:
        print('PAY')
main()
