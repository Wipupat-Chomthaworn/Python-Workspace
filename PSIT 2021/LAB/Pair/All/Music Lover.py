"""main"""
def main():
    """main"""
    keep = dict()
    las = ''
    coun = 0
    art = []
    var1, var2 = [], []
    for _ in range(int(input())):
        var = input().split("-")
        keep[var[0]] = []
        var1.append(var[0])
        var2.append(var[1])
    art.append(list(zip(var1, var2)))
    keep[var[0]] = []
    # for i in art:
    #     coun += 1
    #     if coun == 0:
    #         las = i
    #     if i[0] == las:

    #         print(i)
        # for j in keep[i]:
        #     print(len(keep[i]))
    for i in art:
        print(i.count(i[0]))
main()
