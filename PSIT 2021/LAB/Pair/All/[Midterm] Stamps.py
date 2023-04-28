"""main"""
def main():
    """main"""
    timestothis_place = int(input())
    stamp_get_for_each_tran = int(input())
    get_stamp = int(input())
    stamp = int(input())#ครบดวง
    discount = int(input())#ราคาที่ได้ลด
    all_bill_aldis = 0
    rest_stamp = 0
    for _ in range(timestothis_place):

        bill = int(input())#ราคาที่กิน
        if rest_stamp >= stamp:
            twd = bill // discount
            if bill % discount > 0:
                twd += 1
            can_dis = rest_stamp // stamp
            req = min(twd, can_dis)
            if req > 0:
                bill -= req*discount
                bill = max(0, bill)
                rest_stamp -= req * stamp

        if bill >= stamp_get_for_each_tran:
            rest_stamp += (bill // stamp_get_for_each_tran) * get_stamp
        all_bill_aldis += bill

    print(all_bill_aldis)
    print(rest_stamp)
main()
# """[Midterm] Stamps"""

# def main():
#     """[Midterm] Stamps"""
#     n_input, a_input, b_input, c_input, d_input, stamp, total = \
# int(input()), int(input()), int(input()), int(input()), int(input()), 0, 0
#     for _ in range(n_input):
#         amount = int(input())
#         a_discount = amount
#         while True:
#             if stamp >= c_input and a_discount > 0:
#                 stamp -= c_input
#                 a_discount -= d_input
#             else:
#                 break
#         if amount >= a_input:
#             if b_input != 0 or d_input != 0:
#                 stamp += int((a_discount / a_input)) * b_input
#         total += 0 if a_discount <= 0 else a_discount
#     print(int(total))
#     print(int(stamp))
# main()
# """stamp"""

# def main():
#     """stamp"""
#     time = int(input())
#     needmny = int(input()) #ถึงแล้วจะได้ stm
#     stamp = int(input())
#     needstm = int(input()) #ถึงแล้วจะได้ disc
#     discount = int(input())

#     nowstm = 0 #ปจบ.
#     total = 0 #เงินคำตอบ

#     for _ in range(time):
#         money = int(input())
#         while money > 0 and nowstm >= needstm:
#             money -= discount
#             nowstm -= needstm
#             if money < 0:
#                 money = 0
#         if money >= needmny:
#             nowstm += money//needmny*stamp
#             total += money
#         elif money < needmny:
#             total += money
#     print("%d\n%d" %(total, nowstm))
# main()\
# ร้านอาหารแห่งหนึ่งมี promotion ดังนี้

# 1. ทานอาหารและเครื่องดื่ม ในแต่ละครั้ง (bill) ครบทุกๆ a บาท (หลังหักส่วนลด ถ้ามี) จะได้แสดมป์สะสม b ดวง
# 2. สะสมแสตมป์ครบทุกๆ c ดวง สามารถนำไปเป็นส่วนลดในการทานอาหารและเครื่องดื่มครั้งต่อไป d บาท (แสตมป์ที่เกิดขึ้นจากค่าใช้จ่ายในครั้งนี้ ไม่สามารถนำมาลดเป็นส่วนลดในครั้งนี้ได้)
# 3. แสตมป์ที่มีอยู่ถ้าสามารถใช้เป็นส่วนลดได้ จะต้องใช้เลยในครั้งต่อไป ลูกค้าไม่มีสิทธิปฏิเสธขอไม่ใช้ส่วนลดในครั้งใดๆได้ (ถ้ามีส่วนลดที่สามารถใช้ลดได้ ให้ใช้ลดให้หมด)
# 4. หากส่วนลดมีมากกว่าค่าอาหารที่ต้องจ่าย ไม่สามารถเก็บส่วนต่างไว้เป็นส่วนลดในครั้งต่อๆไปได้ เช่น สมมุติว่ามีแสดมป์อยู่ 10 ดวง ทุกๆ 2 ดวงได้ส่วนลด 50 บาท ถ้าครั้งต่อไปไปทานอาหารและเครื่องตื่มรวมกัน 40 บาท จะต้องเสียแสดมป์ 2 ดวง มูลค่า 50 บาททันที (ไม่สามารถปฏิเสธการใช้แสตมป์ได้ตามข้อ 3) เท่ากับว่าทานอาหารและเครื่องดื่มครั้งนี้ไม่ต้องจ่ายเลย แต่แสดมป์จะเหลือ 8 ดวง และส่วนต่างของส่วนลดที่มากกว่าค่าอาหาร 10 บาท ไม่สามารถเก็บไปใช้ต่อได้

# ถ้ามีลูกค้ารายหนึ่งรับประทานอาหารเป็นจำนวน n ครั้ง และมีรายการค่าใช้จ่าย bill (ก่อนหักส่วนลด) ทั้ง n ครั้ง จงหาว่าลูกค้าจ่ายเงินไปจริงๆ (หลังหักส่วนลดแล้ว) รวมเป็นจำนวนทั้งหมดกี่บาท และมีแสดมป์เหลือที่ยังไม่ได้ใช้อีกทั้งหมดกี่ดวง
# บรรทัดที่ 1: จำนวนครั้งไปที่ไปทานอาหารและเครื่องดื่มที่ร้านนี้ (n) เป็นจำนวนเต็มบวกหรือศูนย์
# บรรทัดที่ 2: ค่า a เป็นจำนวนเต็มบวก
# บรรทัดที่ 3: ค่า b เป็นจำนวนเต็มบวกหรือศูนย์
# บรรทัดที่ 4: ค่า c เป็นจำนวนเต็มบวก
# บรรทัดที่ 5: ค่า d เป็นจำนวนเต็มบวกหรือศูนย์
# บรรทัดที่ 6 ถึง บรรทัดที่ n+5 เป็นราคาค่าอาหารและเครื่องดื่มก่อนหักส่วนลดในแต่ละครั้ง ตั้งแต่ครั้งที่ 1 ถึงครั้งที่ n เป็นจำนวนเต็มบวก

# มี 2 บรรทัด
# บรรทัดที่ 1 เป็นผลรวมของจำนวนเงินที่ได้จ่ายไปทั้งหมด หลังจากหักส่วนลดทั้งหมดแล้ว เป็นจำนวนเต็มบวกหรือศูนย์
# บรรทัดที่ 2 เป็นจำนวนแสตมป์ที่เหลืออยู่ เป็นจำนวนเต็มบวกหรือศูนย์
