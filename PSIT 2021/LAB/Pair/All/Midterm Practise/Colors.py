"""main"""
def main():
    """main"""
    mom = ['Blue', 'Yellow', 'Red']
    var = input()
    var2 = input()
    if var not in mom or var2 not in mom:
        print('Error')
    elif var == var2:
        print(var2)
    elif var == 'Blue' and var2 == 'Yellow':
        print('Green')
    elif var == 'Red' and var2 == 'Yellow':
        print('Orange')
    elif var == 'Red' and var2 == 'Blue':
        print('Violet')
    elif var2 == 'Blue' and var == 'Yellow':
        print('Green')
    elif var2 == 'Red' and var == 'Yellow':
        print('Orange')
    elif var2 == 'Red' and var == 'Blue':
        print('Violet')
main()
