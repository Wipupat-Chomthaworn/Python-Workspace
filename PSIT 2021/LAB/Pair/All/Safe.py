"""Safe"""

def fewzao1(start, tfo):
    # 97, 122
    """Safe"""
    count, count1 = ord(start), 0
    while True:
        count += 1
        count1 += 1
        if count == 123:
            count = 97
        if tfo == chr(count):
            break
    count2, count3 = ord(start), 0
    while True:
        count2 -= 1
        count3 += 1
        if count2 == 96:
            count2 = 122
        if tfo == chr(count2):
            break
    return min(count1, count3)

def main():
    """Safe"""
    st1, st2, pluis = str(input()).lower(), str(input()).lower(), 0
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            pluis += fewzao1(st1[i], st2[i])
    print(pluis)
main()
