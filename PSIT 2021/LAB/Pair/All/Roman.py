"""main"""
def main():
    """main"""
    dtc = {"i":1, "v":5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}
    ans = 0
    var = input().lower()
    i = 0
    num = 0
    while i < len(var):
        if i +1 <len(var) and var[i:i+2] in dtc:
            num += dtc[var[i:i+2]]
            i += 2
    else:
    #print(i)
        num += dtc[var[i]]
        i += 1
    return num
    # for i in input().lower():

    #     ans += dtc[i]
    # print(ans)
main()
