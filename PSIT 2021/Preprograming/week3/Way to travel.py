"""Way to travel"""
def main():
    '''ab'''
    wel = input()
    imp = input()
    far = int(float(input()))
    if far >= 300:
        print("Private jet")
    elif far < 0:
        print('Error')
    elif far < 1:
        print("Walk")
    elif far < 20:
        print("Motorcycle")
    elif imp == 'not important':
        print("Not go")
    elif far < 300:
        print("Car")
        print(wel*False)
main()
