"""Solar System"""
def main():
    """Solar System"""
    var = input()
    star, word = [], ''
    for i in var:
        if i == ' ':
            star.insert(0, word)#แทรกเข้า
            word = ''
        else:
            word += i
    star.insert(0, word)
    star = star[::-1]
    first, last, sunindex = star[0], star[-1], star.index("Sun")
    if first == "Sun":
        print("Hot: "+star[1])
        print("Cool: "+last)
    elif last == "Sun":
        print("Hot: "+star[-2])
        print("Cool: "+first)
    else:
        print("Hot: %s %s"%(star[sunindex-1], star[sunindex+1]))
        if abs(star.index(first)-sunindex) == abs(star.index(last)-sunindex):
            print("Cool: %s %s"%(first, last))
        elif abs(star.index(first)-sunindex) > abs(star.index(last)-sunindex):
            print("Cool: %s"%first)
        elif abs(star.index(first)-sunindex) < abs(star.index(last)-sunindex):
            print("Cool: %s"%last)
main()
