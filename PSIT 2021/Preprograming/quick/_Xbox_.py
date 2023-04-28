'''Xbox'''
def main():
    '''ab'''
    per = int(input())
    for row in range(per):
        if abs(row) > 0:
            print('*', end=' ')
        else:
            print()
        for col in range(per):
            if row == 1 or col == 1:
                print('*', end=' ')
            if row == col:
                print('*', end=' ')
            else:
                print(' ', end =' ')
            
# main()
# # abs(row) == abs(col) or 
