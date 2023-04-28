'''Just MAX it V.6'''
def main():
    '''ab'''
    mylist = []
    num = int(input())
    for _ in range(num):
        var = float(input())
        mylist.append(var)
    print("%.2f"%max(mylist))
main()
