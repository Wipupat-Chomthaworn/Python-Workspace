"""Blacknyack"""
def main():
    """put n print"""
    num_card = int(input())
    total = int(0)
    a_count = int(0)
    for num_card in range(0, num_card):
        inp_card = (str(input())).replace("K", "10")\
            .replace("Q", "10").replace("J", "10")
        a_count += inp_card.count("A")
        value = inp_card.replace("A", "0")
        total += int(value)
    if num_card+1 == 2:
        if a_count > 0:
            total += (11+((a_count-1)*1))
        else:
            total += 0
    elif (total == 10) and (a_count == 1):
        total += 11
    else:
        if (a_count >= 1) and (total < 10):
            total += (11+((a_count-1)*1))
        else:
            total += (a_count)*1
    print(total)
main()
