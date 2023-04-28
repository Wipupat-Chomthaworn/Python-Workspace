"""main"""
def main():
    """main"""
    var = {i:0 for i in range(1, int(input())+1)}
    num = int(input())
    for _ in range(num):
        var[int(input())] += 1
    vote = list(var.keys())
    valuelist = list(var.values())
    ansval = max(valuelist)
    # ansval <= num/2
    # print(che)
    if ansval <= num/2:
        print('0 %d'%ansval)
    else:
        print('%d %d'%(vote[valuelist.index(ansval)], ansval))
main()
