"""main"""
def main(num1, num2):
    """main"""
    if num2 == 0: # base case
        return num1
    elif num2 == 1: #
    else:
        return main(num2, num1%num2)
main(int(input()), int(input()))
