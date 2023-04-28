"""main"""
def main():
    """main"""
    var = input()
    fnd = input()
    list1 = var.split()
    many = list1.count(fnd)#lenth
    where = list1.index(fnd)
    for _ in range(many):
        for _ in range(many):
            print(where, end=' ')
        print()
    # print(list1)
main()
