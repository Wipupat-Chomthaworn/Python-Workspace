"""RectangleArea"""
def main(num1, num2, num5):
    """RectangleArea"""
    num3 = (min(int(num1[0])+int(num1[2]), int(num2[0])+int(num2[2])) - \
max(int(num1[0]), int(num2[0])))
    num4 = (min(int(num1[1])+int(num1[3]), int(num2[1])+int(num2[3])) - \
max(int(num1[1]), int(num2[1])))

    if num3 > 0 and num4 > 0:
        num5 = num3 * num4

    if num5 == 0:
        print("no overlapping")
    else:
        print(num5)

main(input().split(), input().split(), 0)
