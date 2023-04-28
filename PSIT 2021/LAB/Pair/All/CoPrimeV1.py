"""CoPrimeV1"""
def main():
    """main"""
    num, num2 = int(input()), int(input())
    for i in range(1, min(num, num2) + 1):#let's loop find coprime
        if num % i == 0 and num2 % i == 0:
            result = i
    print('YES' if result == 1 else 'NO')
    print(result)
    # ตัวเลขจำนวนเต็ม 2 ตัวจะถูกเรียกว่า Coprime หรือ Relatively prime ถ้าตัวเลขทั้ง 2 ตัวนั้นมี ตัวหารร่วมมาก (หรม) เป็น 1 
    # ยกตัวอย่างเช่นตัวเลข 7 กับ 81 เป็น Coprime เพราะ หรม ของเลขทั้ง 2 ตัวนี้คือ 1
    # อีกตัวอย่างเช่นตัวเลข 14 กับ 21 ไม่เป็น Coprime เพราะ หรม ของเลขทั้ง 2 ตัวนี้คือ 7

    # จงเขียนโปรแกรมทดสอบว่าตัวเลข 2 ตัวที่กำหนดเป็น Coprime หรือไม่ โดยการตอบกลับค่ากลับมา 2 บรรทัด บรรทัดแรกตอบว่า YES หรือ NO และบรรทัดที่ 2 เป็น หรม. ของเลขทั้ง 2 ตัวนี้
main()
