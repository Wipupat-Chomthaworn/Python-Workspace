""""BusStop I"""
def main():
    """"BusStop I"""
    capacity = int(input())
    station = int(input())
    list1 = []
    pai = []
    person = []
    count = 0
    for _ in range(station):
        st1 = str(input()).split()
        paione = int(st1[0])
        pai.append(int(st1[0]))
        st1.pop(0)
        list1.append([paione, st1])
    for i in sorted(pai):
        checkpai = sorted([a for a in pai if int(a) > i])
        list1pai = []
        for j in list1:
            if int(j[0]) == int(i):
                list1pai.append(j)
        for _ in range(5):
            for j in person:
                if int(j) == int(list1pai[0][0]):
                    count += 1
                    person.remove(int(j))

        for k in list1pai[0][1]:
            if checkpai.count(int(k)) == 1 and len(person) < capacity:
                person.append(int(k))
    print(count)
main()
# """BusStop I"""
# def main():
#     """main function"""
#     full, sign, bus, count = int(input()), int(input()), [], 0
#     all_way = sorted([list(map(int, input().split())) for _ in range(sign)])
#     all_sign = [i[0] for i in all_way]
#     for i in range(len(all_way)):
#         sign_num = all_way[i].pop(0)
#         stop_num = bus.count(sign_num)
#         for _ in range(stop_num):
#             bus.remove(sign_num)
#         count += stop_num
#         for j in all_way[i]:
#             if len(bus) < full and j in all_sign[i:]:
#                 bus.append(j)
#     print(count)
# main()
# """PSIT"""
# def main():
#     """PSIT"""
#     vol, num = int(input()), int(input())
#     inbus, pai, fosot, ans = [], [], [], 0
#     for i in range(num):#เอาข้อมูลมา sort
#         txt = input().split()
#         fosot.append([int(txt[0]), txt[1:]])
#     fosot.sort()
#     for i in range(num):#แต่ละรอบคือเกิดขึ้นภายใน 1 ป้าย
#         pai += [fosot[i][0]]
#         while str(i+1) in inbus:#คนลงจากรถ
#             inbus.remove(str(i+1))
#             ans += 1
#         k = 0
#         while len(inbus) < vol:#รับคนขึ้นรถ
#             if k >= len(fosot[i][1]):
#                 break
#             if int(fosot[i][1][k]) not in pai and \
#                int(fosot[i][1][k]) <= num and int(fosot[i][1][k]) > 0:
#                 inbus.append(str(int(fosot[i][1][k])))
#             k += 1
#     print(ans)
# main()
# """BusStop I"""
# def main(maximum_number, all_busstop, check, count):
#     """Design For BusStop I"""
#     bus = sorted([input().split() for i in range(all_busstop)], key=lambda x: int(x[0]))
#     for i in bus:
#         finish = check.count(int(i[0]))
#         count, check = count + finish, check[finish:]
#         check += [int(j) for j in i[1:] if int(j) > int(i[0])][:maximum_number-len(check)]
#         check.sort()
#     print(count)
# main(int(input()), int(input()), [], 0)
