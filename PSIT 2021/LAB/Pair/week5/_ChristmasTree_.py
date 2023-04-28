'''ChristmasTree'''
def main():
    """main function"""
    tree, stall = int(input()), int(input())
    for i in range((tree)):
        print(' '*((tree)-i-1), end='')#printspace
        for _ in range(2*i+1):#*2 is double side *
            print('*', end='')# +1 for center*
        print()
    for _ in range(stall):#print stall center
        print('---'.center(2*tree, ' '))
main()
#     *
#    ***
#   *****
#  *******
# *********
#    ---
#    ---
#    ---

# """Virus I"""
# def main():
#     """main func"""
#     num = int(input())
#     num_2 = int(input())
#     bark = 3
#     for i in range(num):
#         print(" "*(num-i-1)+"*"*(2*i+1))
#     for i in range(num_2):
#         print(" "*(num-2)+"-"*bark)
# main()
