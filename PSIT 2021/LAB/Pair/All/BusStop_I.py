"""BusStop I"""
def main(amount, count):
    """BusStop I"""
    ppl = [] #list string
    pplincar = [] #list int
    home = 0
    #sort ppl
    for _ in range(count):
        bus = input().split()
        ppl.append(bus)
    ppl.sort(key=lambda i: int(i[0]))
    #arrive home
    for i in ppl:
        busstop = int(i[0])# busstop

        #remove ppl in car
        if len(pplincar) != 0:
            pplincar2 = pplincar.copy()
            for arrive in pplincar:
                if arrive == busstop:
                    pplincar2.remove(arrive)
                    home += 1
            pplincar = pplincar2
        #add ppl in car
        for j in range(1, len(i)):
            if len(pplincar) == amount:
                break
            if busstop < int(i[j]):
                pplincar.append(int(i[j]))
    print(home)
main(int(input()), int(input()))
