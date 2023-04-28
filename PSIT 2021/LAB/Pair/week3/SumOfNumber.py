'''SumOfNumber'''
def main():
    """ab"""
    sumvar = int(input())#ค่าที่ต้องการให้หยุดทำงาน
    keep = 0
    while True:
        var = int(input())
        if var == -1 or keep == sumvar or var == sumvar or var <= 0\
            or var+keep == sumvar:
            if not var == -1:
                keep += var
                break
            break
        else:
            keep += var
    print("%d"%keep)
main()
