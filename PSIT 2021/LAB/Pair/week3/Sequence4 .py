"""Sequence IV"""
def main():
    """main func"""
    num = int(input())
    keep = 0
    for _ in range(num):
        for _ in range(num):
            keep += 1
            print(keep, end=" ")
        print()
main()
