"""[Midterm] Shorten"""
def main():
    """[Midterm] Shorten"""
    count = 0
    keep_2 = 0
    string = ""
    while True:
        num = int(input())
        if  count == 0:
            keep_1 = num
            sub = num
            count += 1
        elif sub+1 == num:
            if sub != num:
                sub += 1
                keep_2 = num
        else:
            if keep_2 != 0:
                string += ("%s-%s" %(keep_1, keep_2))
                count = 1
                keep_1 = num
                keep_2 = 0
                sub = num
            else:
                string += ("%s" %keep_1)
                count = 1
                keep_1 = num
                sub = num
                keep_2 = 0
            if num != -1:
                string += (", ")
        if num == -1:
            if string == "0":
                print()
            else:
                print(string)
            break
main()
