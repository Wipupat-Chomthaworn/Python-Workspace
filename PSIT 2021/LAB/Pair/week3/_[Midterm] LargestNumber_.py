"""[Midterm] LargestNumber"""
def main():
    """Return Largest Value"""
    var = input()
    var2 = input()
    var3 = input()
    ans = int(var+var2+var3)
    ans_1 = int(var+var3+var2)
    ans2 = int(var2+var+var3)
    ans_2 = int(var2+var3+var)
    ans3 = int(var3+var2+var)
    ans_3 = int(var3+var+var2)
    if ans >= ans2 and ans >= ans3:
        if ans >= ans_1:
            print(ans)
        else:
            print(ans_1)
    elif ans2 >= ans and ans2 >= ans3:
        if ans2 >= ans_2:
            print(ans2)
        else:
            print(ans_2)
    elif ans3 >= ans and ans3 >= ans2:
        if ans3 >= ans_3:
            print(ans3)
        else:
            print(ans_3)
main()
