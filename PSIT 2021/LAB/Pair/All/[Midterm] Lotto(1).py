"""main"""
def main():
    """main"""
    first = input()
    if first == "000000":
        near = "000001"
        near2 = "999999"
    elif first == "999999":
        near = "000000"
        near2 = "999998"
    else:
        near = "%06d" % (int(first) - 1)
        near2 = "%06d" % (int(first) + 1)
    # print(type(near))
    # print(near, near2)
    twobk = input()
    threefirst = input()
    threefirst2 = input()
    threeback = input()
    threeback2 = input()
    lotto = input()
    prize = 0
    if lotto == first:
        prize += 6000000
    if lotto == near or lotto == near2:
        prize += 100000

    if lotto[4:] == twobk:
        prize += 2000

    if lotto[:3] == threefirst:
        prize += 4000
    if lotto[:3] == threefirst2:
        prize += 4000

    if lotto[3:] == threeback:
        prize += 4000
    if lotto[3:] == threeback2:
        prize += 4000

    print(prize)
main()
