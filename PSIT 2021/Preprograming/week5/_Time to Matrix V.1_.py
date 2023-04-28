'''Time to Matrix V.1'''
def main():
    '''ab'''
    matrix = []
    row = []
    size = input()
    where = input()
    for _ in range(int(size[0])):
        for _ in range(int(size[2])):
            var = int(input())
            row.append(var)
        matrix.append(row)
        row = []
    print('result = %d'%matrix[int(where[0])-1][int(where[2])-1])
    for i in matrix:
        print(str(i).replace(',', ''))
main()
