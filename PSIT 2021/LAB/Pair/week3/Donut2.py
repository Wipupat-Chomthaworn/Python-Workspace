'''[Midterm] Donut'''
def main():
    '''ab'''
    vara = int(input())#price
    varb = int(input())#pro
    varc = int(input())#free
    vard = int(input())#need
    bpc = varb + varc
    promo = vard//bpc#จน.promoที่เข้า
    pro2 = bpc*promo#donut
    restneed = vard-pro2#the rest we need
    if restneed >= varb:#withpro
        price = vara*((promo+1)*varb)
        donut = bpc*(promo+1)
    else:
        price = vara*(varb*promo+restneed)#ราคา*โปร
        donut = vard
    print(price, donut)
main()
# โดนัทราคาชิ้นละ a บาท ถ้าซื้อโดนัทจำนวน b ชิ้นด้วยกัน \
# จะได้แถมอีก c ชิ้นฟรี ถ้าคุณต้องการได้โดนัทอย่างน้อย d ชิ้น \
# จะต้องจ่ายเงินน้อยที่สุดกี่บาท และจะได้โดนัทจำนวนมากที่สุดทั้งหมดกี่ชิ้น
# หมายเหตุ โดนัทในรูปดูน่าอร่อยมาก
