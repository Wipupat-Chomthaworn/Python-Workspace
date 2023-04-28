"""main"""
def isprime(num):
    """Check if"""
    if num == 1:# 1 ไม่ใช่ prime
        return 'NO'
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:#ถ้ามีตัวอะไรที่หารลงตัว return 'NO'
            return 'NO'
    return 'YES'
print(isprime(int(input())))
