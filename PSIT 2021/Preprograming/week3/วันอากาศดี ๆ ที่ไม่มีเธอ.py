# """วันอากาศดี ๆ ที่ไม่มีเธอ"""
# def main():
#     '''ab'''
#     uxx = int(input())
#     uyy = int(input())
#     a_x = int(input())
#     a_y = int(input())
#     b_x = int(input())
#     b_y = int(input())
#     a_to_me = (((uxx-a_x)**2)+(uyy-a_y)**2)**0.5
#     b_to_me = (((uxx-xat2)**2)+(uyy-b_y)**2)**0.5
#     if a_to_me > b_to_me:
#         print('B')
#     elif a_to_me < b_to_me:
#         print('A')
#     elif a_to_me == b_to_me:
#         if a_y > b_y:
#             print("A")
#         elif a_y < b_y:
#             print("B")
#         elif a_y == b_y:
#             print('A'*(xat < xat2)+'B'*(xat > xat2)+'A'*(a_y == b_y))
#     else:
#         print('A')
# main()
# """วันอากาศดี ๆ ที่ไม่มีเธอ"""
# def main():
#     '''ab'''
#     uxx = int(input())
#     uyy = int(input())
#     xat = int(input())
#     a_y = int(input())
#     xat2 = int(input())
#     b_y = int(input())
#     a_to_me = (((uxx-xat)**2)+(uyy-a_y)**2)**0.5
#     b_to_me = (((uxx-xat2)**2)+(uyy-b_y)**2)**0.5
#     if a_to_me == b_to_me:
#         if a_y > b_y:print("B")
#         elif a_y < b_y:print("A")
#         elif a_y == b_y:
#             print('A'*(xat < xat2)+'B'*(xat > xat2)+'A'*(a_y == b_y))
#     else:
#         print('B'*(a_to_me > b_to_me)+'A'*(a_to_me < b_to_me))
# main()
"""วันอากาศดี ๆ ที่ไม่มีเธอ"""
def main():
    '''ab'''
    uxx = int(input())
    uyy = int(input())
    a_x = int(input())
    a_y = int(input())
    b_x = int(input())
    b_y = int(input())
    a_to_me = (((uxx-a_x)**2)+(uyy-a_y)**2)**0.5
    b_to_me = (((uxx-b_x)**2)+(uyy-b_y)**2)**0.5
    # if a_to_me == b_to_me:
    #     if a_y > b_y:
    #         print("A")
    #     elif a_y < b_y:
    #         print("B")
    #     elif a_y == b_y:
    #         print('A'*(a_x < b_x)+'B'*(a_x > b_x))
    # elif a_to_me > b_to_me:
    #     print(('B'*(a_to_me > b_to_me)))
    # elif a_to_me < b_to_me:
    #     print('A')
    # else:
    #     print('A')
    if a_to_me < b_to_me:
        print("A")
    elif b_to_me < a_to_me:
        print("B")
    elif b_to_me == a_to_me:
        if a_y > b_y:
            print("A")
        elif b_y > a_y:
            print("B")
        elif b_y == a_y:
            if a_x < b_x:
                print("A")
            elif b_x < a_x:
                print("B")
            else:
                print("A")
main()
# """วันอากาศดี ๆ ที่ไม่มีเธอ"""
# def main():
#     """inprint"""
#     mnx, mny, pax, pay = int(input()), int(input()), int(input()), int(input())
#     pbx, pby = int(input()), int(input())
#     dia, dib = ((mnx-pax)**2+(mny-pay)**2)**0.5, ((mnx-pbx)**2+(mny-pby)**2)**0.5
#     pr1, pr2 = dia == dib and pay > pby, dia == dib and pay == pby and pax < pbx
#     if (pr1 or pr2) or (dia == dib and pay == pby and pax == pbx) or (dia < dib):
#         return print("A")
#     else:
#         print("B")
# main()
# """วู้วฮู้ว"""
# def main():
#     """อู้วๆ"""
#     myx, myy = int(input()), int(input())
#     car_ax, car_ay = int(input()), int(input())
#     car_bx, car_by = int(input()), int(input())
#     itocara = (((car_ay-myy)**2)+((car_ax-myx)**2))**0.5
#     itocarb = (((car_by-myy)**2)+((car_bx-myx)**2))**0.5
#     if itocara == itocarb and car_by == car_ay and car_ax == car_bx:
#         print("A")
#     elif itocara == itocarb and car_by == car_ay:
#         print("A"*(car_ax < car_bx)+"B"*(car_bx < car_ax))
#     elif itocara == itocarb:
#         print("A"*(car_ay > car_by)+"B"*(car_by > car_ay))
#     else:
#         print("A"*(itocara < itocarb)+"B"*(itocarb < itocara))
# main()
