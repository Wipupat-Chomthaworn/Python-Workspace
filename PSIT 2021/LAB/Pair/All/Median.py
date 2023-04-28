""""Median"""
def main():
    """Median"""
    num = int(input())
    number = [int(input()) for i in range(num)]
    number.sort()
    if num % 2 != 0:
        med = number[(num//2)]
    else:
        med = ((number[(num//2)])+(number[(num//2-1)]))/2
    print("%.1f"%med)
main()
