"""Do you know leap year?"""
def main():
    '''ab'''
    sol = int(input())
    if (sol % 400 == 0) or (sol % 4 == 0) and (sol % 100 != 0):
        print('%d is a leap year.'%sol)
    elif sol % 400 != 0:
        print('%d is not a leap year.'%sol)
main()
