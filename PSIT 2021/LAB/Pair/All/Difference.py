"""Difference"""
def main():
    """Difference"""
    num1 = int(input())
    num2 = int(input())
    in_num1 = set()
    in_num2 = set()
    for _ in range(num1):
        in_num1.add(int(input()))
    for _ in range(num2):
        in_num2.add(int(input()))
    ans = in_num1 - in_num2
    print(*sorted(ans), sep=" ")
main()
