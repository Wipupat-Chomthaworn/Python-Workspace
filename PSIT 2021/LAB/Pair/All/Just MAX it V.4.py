"""[Midterm] One For All"""
def main():
    """main"""
    num = int(input())
    for i in range(num):
        var = input()
        if i % 2 == 0:
            print('-'*i+var, end='')
        else:
            print('*'*i+var, end='')
main()
