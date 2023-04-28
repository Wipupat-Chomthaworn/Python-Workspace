"""main"""
def main():
    """main"""
    price = int(input())
    disa = input().split()
    disper = input().split()
    ans1 = (price >= int(disa[0]))*(price-int(disa[1]))
    ans2 = (int(disper[0]) <= price)*(price-price*(int(disper[1])/100))
    # print(ans1)
    # print(ans2)
    if ans1 == ans2:
        if int(disa[0]) < int(disper[0]):
            print('1 %.1f'%ans1)
        elif int(disa[0]) > int(disper[0]):
            print('2 %.1f'%ans2)
        else:
            print('1 %.1f'%ans1)
    elif ans1 < ans2:
        print('1 %.1f'%ans1)
    else:
        print('2 %.1f'%ans2)
main()
