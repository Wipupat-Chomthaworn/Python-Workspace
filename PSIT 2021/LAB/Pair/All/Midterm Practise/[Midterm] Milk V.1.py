"""main"""
def main():
    """main"""
    price = int(input())
    pro = int(input())
    free = int(input())
    money = int(input())
    total = money // price
    if pro > 0:
        praa = money // price
        while praa >= pro:
            more_milk = (praa//pro) * free
            praa = praa % pro
            praa += more_milk
            total += more_milk
    print(total)
main()
