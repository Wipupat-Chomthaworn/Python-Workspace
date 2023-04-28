"""Sequence I"""
def main():
    """main func"""
    row = int(input())
    col = int(input())
    keep = 0
    for _ in range(row):
        for _ in range(col):
            var = 1
            keep += var
            print(keep, end=" ")
        print()
main()
