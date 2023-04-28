"""main"""
import math
def main():
    """main"""
    num = int(input())
    prores = int(input())
    disper = int(input())
    stick = int(input())
    allprice = []
    for i in range(num):
        price = int(input())
        allprice.append(price)
    check = sum(allprice) - max(allprice)
    ans = check + (max(allprice) - (max(allprice)*stick/100))
    if sum(allprice) >= prores:
        ans -= (ans*disper/100)
    if ans >= sum(allprice) - (sum(allprice)*disper/100):
        ans = sum(allprice) - (sum(allprice)*disper/100)
    if ans >= (check + (max(allprice) - (max(allprice)*stick/100))):
        ans = check + (max(allprice) - (max(allprice)*stick/100))
    if check + (max(allprice) - (max(allprice)*stick/100))\
         >= sum(allprice) - (sum(allprice)*disper/100):
        print(sum(allprice) - (sum(allprice)*disper/100) - check)
        ans = sum(allprice) - (sum(allprice)*disper/100)
    print(math.floor(ans))
main()
# """main"""
# import math
# def main():
#     """main"""
#     num = int(input())
#     prores = int(input())
#     disper = int(input())
#     stick = int(input())
#     allprice = []
#     for i in range(num):
#         price = int(input())
#         allprice.append(price)
#     check = sum(allprice) - max(allprice)
#     ans = check + (max(allprice) - (max(allprice)*stick/100))
#     if ans >= prores:
#         ans -= (ans*disper/100)
#     print(math.floor(ans))
# main()
