"""main"""
def isprime(num):
    """Check if"""
    if num == 1:# 1 ไม่ใช่ prime
        return False
    for i in range(2, (int(num**0.5)//10)+1):
        if num%i == 0:#ถ้ามีตัวอะไรที่หารลงตัว return 'NO'
            return False
    return True
print(isprime(int(input())))
