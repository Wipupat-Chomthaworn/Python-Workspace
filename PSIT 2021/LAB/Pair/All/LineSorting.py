"""LineSorting"""

def main():
    """LineSorting"""
    numx, lst = int(input()), []
    for _ in range(numx):
        text = str(input())
        lst.append(text)
    lst.sort(key=len)
    print(*(lst), sep="\n")
main()
