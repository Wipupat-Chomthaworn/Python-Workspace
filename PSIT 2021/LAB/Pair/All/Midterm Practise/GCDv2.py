"""GCD_v2"""

def main():
    """main function"""
    num1 = float(input())
    num2 = float(input())
    while num2 != 0:
        num1, num2 = num2, num1%num2
    print(int(num1))
main()
