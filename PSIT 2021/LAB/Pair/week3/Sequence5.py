"""Sequence V"""
def main():
    """main func"""
    num = int(input())
    keep = 0
    for _ in range(num//7+1):
        for _ in range(7):
            keep += 1
            last = num-keep+1
            if last >= 1:
                print(last, end=" ")
        print()
main()
