"""PSIT"""
def main():
    """PSIT"""
    group_1 = int(input())
    group_2 = int(input())
    set_1 = set()
    set_2 = set()
    for _ in range(group_1):
        set_1.add(int(input()))
    for _ in range(group_2):
        set_2.add(int(input()))
    inter_set = set_1.intersection(set_2)
    if inter_set == set():
        print("Nope")
    else:
        inter_list = list(inter_set)
        inter_list.sort(reverse=True)
        for i in inter_list:
            print(i)

main()
