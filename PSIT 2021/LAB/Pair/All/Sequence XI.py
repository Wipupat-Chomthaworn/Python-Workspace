"""Virus I"""
def main():
    """main func"""
    num = int(input())
    keep = (2*num)-1
    low = 0
    high = keep - 1
    value = low+1
    scale = [[0 for i in range(keep)] for j in range(keep)]
    for i in range(num):
        for j in range(low, high+1):
            scale[i][j] = value
        for j in range(low+1, high+1):
            scale[j][i] = value
        for j in range(low+1, high):
            scale[j][high] = value
        for j in range(low+1, high+1):
            scale[high][j] = value
        low = low+1
        high = high-1
        value = value+1
    for i in range(keep):
        for j in range(keep):
            print("%02d" %scale[i][j], end=" ")
        print()
main()
