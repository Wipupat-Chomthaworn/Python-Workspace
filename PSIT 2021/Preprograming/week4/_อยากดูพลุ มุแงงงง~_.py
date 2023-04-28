'''อยากดูพลุ มุแงงงง~'''
def main():
    '''ab'''
    num = input()
    length = len(num)
    for i in range(length):
        for j in range(length):
            # if i+1 == length and j+1 == length:
            if i+j == length-1:
                print(num[j], end=" ")
                print(" 3", end="   ")
        print()
main()