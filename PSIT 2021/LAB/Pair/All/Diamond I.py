"""Diamond I"""
def main():
    """Diamond I"""
    num1, num2 = int(input()), int(input())
    list1, las = [], []
    for _ in range(num1):
        list1.append('')
    for i in range(num1):
        list1[i] = (input().split(" "))#เก็บค่าแต่ละตัว
    for i in range(num2):
        point = 0
        for j in range(num1):
            point += int(list1[j][i])#ขุดแร่โดยจับคู่ละไล่บวก
        las.append(point)
    print(max(las))#หาที่ขุดแล้วคุ้ม
main()
