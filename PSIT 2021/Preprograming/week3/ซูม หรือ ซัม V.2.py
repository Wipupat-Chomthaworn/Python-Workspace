"""ซูม หรือ ซัม V.2"""
def main():
    '''ab'''
    sol = int(input())
    sol2 = int(input())
    sol3 = int(input())
    if sol == sol2 == sol3:
        print(0)
    elif sol == sol3:
        print(sol2)
    elif sol2 == sol3:
        print(sol)
    elif sol == sol2:
        print(sol3)
    else:
        print((sol+sol2+sol3))
main()
