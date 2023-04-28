var = int(input())
    var2 = int(input())
    var3 = int(input())
    # if var < 0:
    #     var = int(input())
    #     var2 = int(input())
    #     var3 = int(input())
    # var2 = int(input())
    # if var2 < 0:
    #     var2 = int(input())
    # var3 = int(input())
    # if var3 < 0:
    #     var3 = int(input())
    # var = abs(int(input()))
    # var2 = abs(int(input()))
    # var3 = abs(int(input()))
    def ishigh(ref, num):
        '''find'''
        if ref - num >= 0:
            high = ref
        else:
            high = num
        return high
    num1 = ishigh(var, var2)
    num2 = ishigh(num1, var2)
    num3 = ishigh(num2, var3)
    print(num3, end='')
    def find2(ref, num):
        '''find'''
        if ref - num >= 0:
            sec = num
        else:
            sec = ref
        return sec
    sec = find2(var, var2)
    sec2 = find2(num1, var2)
    low3 = find2(num2, var3)
    if var>low3 and var<num3:
        sec = var
    print(low3, end='')