'''หมอลำซิ่ง Academia'''
def main():
    '''ab'''
    corr = input()
    point = 0
    result = 0
    for i in range(len(corr)):
        if corr[i] == '1':
            point += 1
            result = max(result, point)
        else:
            point = 0
    if result <= 1:
        print('Rank D')
    elif result == 2:
        print('Rank C')
    elif result == 3:
        print('Rank B')
    elif result == 4:
        print('Rank A')
    elif result == 5:
        print('Rank S')
    elif result >= 6:
        print('Rank SSS')
main()
