"""Duplicate I"""

def main():
    """main"""
    num1, num2, lst1, lst2 = int(input()), int(input()), [], []
    for _ in range(num1):
        lst1.append(str(input()).strip())
    for _ in range(num2):
        check = str(input()).strip()
        if check in lst1:
            if check not in lst2:
                lst2.append(check)
    if len(lst2) == 0:
        print('Nope')
    else:
        print(*(sorted(lst2, reverse=True)), sep="\n")
main()
