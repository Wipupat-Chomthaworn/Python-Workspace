"""main"""
def main():
    """main"""
    list1 = []
    count = -1
    rank = 1
    varnum = int(input())
    for i in range(varnum):

        var = input().split()# spilt medal
        list1 += [[int(var[1])*-1, int(var[2])*-1, int(var[3])*-1, var[0]]]
        list1.sort()


    for i in range(len(list1)):
        if (str(list1[i][0])+str(list1[i][1])+str(list1[i][2])) == \
           (str(list1[i-1][0])+str(list1[i-1][1])+str(list1[i-1][2])):
            count += 1

        else:
            rank += 1 + count
            count = 0

        print(rank, list1[i][3], int(list1[i][0])*-1, int(list1[i][1])*-1, \
        int(list1[i][2])*-1, (int(list1[i][0])*-1)+(int(list1[i][1])*-1)+(int(list1[i][2])*-1))
main()
# """Olympic"""
# def main(varnum):
#     """Olympic"""
#     players = []
#     for _ in range(varnum):
#         txt = input()
#         dat = txt.split()[1:]
#         dat = [-int(i) for i in dat]
#         dat.append("%s %d" % (txt, abs(sum(dat))))
#         players.append(dat)
#     players.sort()
#     rank = 1
#     last = ""
#     for i in range(len(players)):
#         data = players[i]
#         key = "".join(data[3].split()[1:])
#         if key != last:
#             rank = i+1
#         last = key
#         print(rank, data[3])
# main(int(input()))
