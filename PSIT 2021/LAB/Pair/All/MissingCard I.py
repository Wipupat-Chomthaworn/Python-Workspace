"""MissingCard I"""
def main():
    """MissingCard I"""
    card = []
    for i in range(2, 11):
        card.append(str(i))
    card.append('J')
    card.append('Q')
    card.append('K')
    card.append('A')
    cate = ['S', 'H', 'D', 'C']
    samrub = []

    for i in cate:
        for j in card:
            samrub.append(j+i)
    # print(samrub)
    have = []
    for _ in range(len(samrub)-1):
        var = input()
        have.append(var)
    for i in samrub:
        if have.count(i) == 0:
            print(i)
            break
main()
