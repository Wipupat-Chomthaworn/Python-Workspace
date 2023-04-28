"""BusStop I"""
def main():
    """BusStop I"""
    bus_space = int(input())
    bus_stop = int(input())
    bus = []
    keep = []
    count = 0
    for _ in range(1, bus_stop+1):
        human = input().split()
        keep = []
        for k in bus:
            if int(k) == int(human[0]):
                count += 1
                continue
            keep.append(k)
        bus = keep.copy()
        for j in human[1:]:
            if len(bus) < bus_space and int(j) > int(human[0]) and int(j) <= bus_stop:
                bus.append(j)
    print(count)
main()
