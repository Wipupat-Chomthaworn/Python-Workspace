"""main"""
def check(sta, data, ans):
    """check"""
    for i in sorted(list(set(sta))):
        for j in range(1, data.count(i)+1):
            ans += "-"#ใส่ - ตามจน.
            if j % 5 == 0 and j != data.count(i):#ถ้า มีมากกว่า5 เติม|
                ans += "|"
        print("%s : %s"%(i, ans))
        ans = ""#ลบกันตัวซ้ำ
# import json
def main():
    """main"""
    data = input()
    upp, low = [], []
    ans = ''
    for i in data:
        if i.islower():
            low.append(i)
        if i.isupper():
            upp.append(i)
    check(low, data, ans)
    check(upp, data, ans)
main()
#InformationOfTechnology
