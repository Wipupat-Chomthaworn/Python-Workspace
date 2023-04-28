"""BookWorm"""
def main():
    """BookWorm"""
    list1 = []
    num1 = int(input())#pack of book
    for _ in range(num1):
        mini = float(input())#เวลา(minutes)
        count = 0
        timeuse = []
        for _ in range(int(input())):
            timeuse.append(float(input()))
        for i in sorted(timeuse):
            if mini >= i:
                mini -= i#ลบเวลา
                count += 1
        list1.append(count)
    print(*list1, sep="\n")
main()
