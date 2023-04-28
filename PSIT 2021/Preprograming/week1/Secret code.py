"""Secret code"""
def main():
    """anotherquest"""
    name_1 = int(input())
    pas_1 = str(int((name_1%10)%10))
    pas_2 = str(int(name_1//100)%10)
    pas_3 = str(int((name_1//10000)%10))
    pas_4 = str(int((name_1//1000000)%10))
    pas_5 = str(int((name_1//100000000)%10))
    print(pas_5+pas_4+pas_3 +pas_2+pas_1)
main()

'''"""Secret code"""
def main():
    """Secret naja"""
    number = int(input())
    number1 = int(number/10**8%10)
    number2 = int(number/10**6%10)
    number3 = int(number/10**4%10)
    number4 = int(number/10**2%10)
    number5 = int(number%10)
    print(number1, number2, number3, number4, number5, sep="")
main()
"""Secret code"""
 
 
def decode():
    """decode function"""
    code = int(input())
    number_1 = str(code %10**9 // 10**8) #ดอกจัน2อัน=ยกกำลัง #ตัวเลขที่เอายกกำลังไม่ควรเว้นวรรค
    number_2 = str(code %10**7 // 10**6)
    number_3 = str(code %10**5 // 10**4)
    number_4 = str(code %10**3 // 10**2)
    number_5 = str(code %10**1)
    print(number_1 + number_2 + number_3 + number_4 + number_5)
 
decode()
"""this is..."""
NUM_1 = int(input())
NUM_2 = NUM_1//10**8%10
NUM_3 = NUM_1//10**6%10
NUM_4 = NUM_1//10**4%10
NUM_5 = NUM_1//10**2%10
NUM_6 = NUM_1%10
print(("%d%d%d%d%d")%(NUM_2, NUM_3, NUM_4, NUM_5, NUM_6))'''