"""4 mista"""
def main():
    '''ab'''
    sol = (input()).upper()
    sol2 = (input()).upper()
    sol3 = sol.count(sol2)
    if  '4' in sol:
        print('It\'s not safe four Mista....')
    elif 'FOUR' in sol:
        print('It\'s not safe four Mista....')
    elif 'FOURTH' in sol:
        print('It\'s not safe four Mista....')
    elif sol3 == 4:
        print('It\'s not safe four Mista....')
    elif len(sol) % 4 == 0:
        print('It\'s not safe four Mista....')
    else:
        print('MISTA, THIS ONE\'S 4 U.')
main()
# def main():
#     '''ab'''
#     sol = (input()).upper()
#     sol2 = (input()).upper()
#     sol3 = sol.count(sol2)
#     if  '4' in sol or 'FOUR' in sol or 'FOURTH' in sol:
#         print('It\'s not safe four Mista....')
#     elif sol3 % 4 == 0:
#         print('It\'s not safe four Mista....')
#     elif len(sol) % 4 == 0:
#         print('It\'s not safe four Mista....')
#     else:
#         print('MISTA, THIS ONE\'S 4 U.')
# main()
