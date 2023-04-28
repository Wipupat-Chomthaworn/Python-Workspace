"""prime"""

def main():
    """ifprime"""
    inp = int(input())
    prime = True
    if inp > 1:
        for i in range(2, inp):
            if inp % i == 0:
                prime = False
                break
    else:
        prime = False
    if prime:
        print('Yes')
    else:
        print('No')
main()
