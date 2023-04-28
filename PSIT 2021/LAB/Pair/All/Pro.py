"""main"""
def pro():
    """main"""
    promo = int(input())
    pay = int(input())
    baht = int(input())
    people = int(input())
    ans = (people // pay)*baht*pay
    people = people % promo
    # while True
    # if people >= promo or people < promo:
    ans += (people)*baht
    # print((people % pro))
    print(ans)
pro()
