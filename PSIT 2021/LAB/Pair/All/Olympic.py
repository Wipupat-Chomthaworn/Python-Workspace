"""Olympic"""

def main():
    """Olympic"""
    num1, lst, name, lst2, countfew = int(input()), [], [], [], 0
    for _ in range(num1):
        st1 = str(input()).split(" ")
        lst.append([int(st1[1]), int(st1[2]), int(st1[3])])
        name.append([st1[0], [st1[1] + " " + st1[2] + " " + st1[3]]])
    for i in lst:
        if lst2.count(i) == 0:
            lst2.append(i)
    for i in sorted(lst2)[::-1]:
        fewz, indexz = lst.count(i), str(i[0]) + " " + str(i[1]) + " " + str(i[2])
        few, sumf = sorted([a[0] for a in name if a[1][0] == indexz]), i[0] + i[1] + i[2]
        for j in range(fewz):
            print("%s %s %s %s" %(str(countfew + 1), few[j], indexz, sumf))
        countfew += fewz
main()
