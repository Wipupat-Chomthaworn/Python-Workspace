'''Basic index'''
def main():
    '''ab'''
    mylist = []
    while True:
        var = input()
        if var.lower() != 'end':
            mylist.append(var)
        else:
            var2 = int(input())
            if var2 > len(mylist)-1:
                print("Index Not Found")
                break
            else:
                print('List[%d] = "%s"'%(var2, mylist[var2]))
                break
main()
# if :
#         print("Index Not Found"')
#     else:
#         print('List[%d] = "%s"'%(var2, mylist)) or var2 < len(mylist)
