"""Virus I"""
def main():
    """main func"""
    num = int(input())
    row = 1
    space = 3
    for i in range(1, num+1):
        keep = 0
        for j in range(1, num-i+1):
            print("  ", end=" ")
        for j in range(1, row+1):
            if j <= i:
                keep += 1
            else:
                keep -= 1
            print("%02d" %keep, end=" ")
        row = row+2
        space = space-1
        print()
main()
