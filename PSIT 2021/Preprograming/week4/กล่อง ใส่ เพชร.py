'''กล่อง ใส่ เพชร'''
def main():
    sth = int(input())
    for o in range(sth):
        row = o + 1
        for _ in range(sth - o - 1):
            print(" ", end="  ")
        for _ in range(o + 1):
            print(row, end=" ")
            row = row-1
        if o > 0:
            for _ in range(o - 1):
                print(" ", end=" ")
            for _ in range(o + 1):
                row = row + 1
                print(row, end=" ")
        print()

    for o in range(1, sth):
        row = sth - o
        for _ in range(o):
            print(" ", end="  ")
        for _ in range(sth - o):
            print(row, end=" ")
            row = row - 1
        if o < (sth - 1):
            for _ in range(sth - o - 2):
                print(" ", end=" ")
            for _ in range(sth - o):
                row = row + 1
                print(row, end=" ")
        print()
main()