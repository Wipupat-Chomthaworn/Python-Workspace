"""Divide3Or5"""
def main():
    """Divide3Or5"""
    inp = int(input())
    keep = 0
    for i in range(1, inp+1):
        if i%3 == 0 or i%5 == 0:
            keep += i
    print(keep)
main()
