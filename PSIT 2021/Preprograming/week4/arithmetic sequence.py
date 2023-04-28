"""arithmetic sequence"""
def main():
    '''ab'''
    num = int(input())
    num2 = int(input())
    num3 = int(input())
    if num3 < 0:
        num2 = int(num2) - 1
    else:
        num2 = int(num2) + 1
    for i in range(num, int(num2), num3):
        print(i)
main()
