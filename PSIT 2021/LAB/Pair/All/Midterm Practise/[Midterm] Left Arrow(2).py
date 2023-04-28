'''[Midterm] Parallelogram'''
def main():
    """main function"""
    width, height = int(input()), int(input())
    for i in range((height//2)):
        print(' '*((height//2)-i), end='')
        for _ in range(width):
            print('*', end='')
        print()
    print("*"*width)
    for i in range((height//2), 0, -1):
        print(' '*((height//2)-i+1), end='')
        for _ in range(width):
            print('*', end='')
        print()
        # for j in range(var, 0, -1):
        #     print(var[var-j+1:])
main()
#   *******
#  *******
# *******
#  *******
#   *******
