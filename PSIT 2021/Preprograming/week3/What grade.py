"""What grade?"""
def main():
    '''ab'''
    human = int(float(input()))
    if human >= 80:
        print("A")
    elif 75 <= human <= 79:
        print('B+')
    elif 70 <= human <= 74:
        print("B")
    elif 65 <= human <= 69:
        print("C+")
    elif 60 <= human <= 64:
        print("C")
    elif 55 <= human <= 59:
        print("D+")
    elif 50 <= human <= 54:
        print("D")
    elif human < 50:
        print("F")
main()
