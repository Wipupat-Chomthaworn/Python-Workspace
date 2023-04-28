"""[Recommend] Ping"""
def check(this):
    """1"""
    if this.count("out.") > 0 or this.count("fail") > 0:
        return 1
    else:
        return 0
def load(this, num):
    """2"""
    if num == 0:
        oka = this[this.find("time") + 4:this.find("ms")]
        return oka
    if num == 1:
        if this[1:].isnumeric():
            return this[1:]
        else:
            return -1
    if num == 2:
        if this[1:].isnumeric():
            return this[1:]
        else:
            return 10000000000
    if num == 3:
        if this[1:].isnumeric():
            return this[1:]
        else:
            return 0
def mize(time_1, time_2, time_3, time_4, foureveryoung):
    """3"""
    time__1, time__2, time__3, time__4 = load(time_1, 1), \
        load(time_2, 1), load(time_3, 1), load(time_4, 1)
    maxi = max(int(time__1), int(time__2), int(time__3), int(time__4))
    time__1, time__2, time__3, time__4 = load(time_1, 2), \
        load(time_2, 2), load(time_3, 2), load(time_4, 2)
    mini = min(int(time__1), int(time__2), int(time__3), int(time__4))
    time__1, time__2, time__3, time__4 = load(time_1, 3), \
        load(time_2, 3), load(time_3, 3), load(time_4, 3)
    print("    Minimum = %dms, Maximum = %dms, Average = %dms" % \
        (mini, maxi, (int(time__1)+int(time__2)+int(time__3)\
        +int(time__4))/abs(foureveryoung-4)))
def main():
    """[Recommend] Ping"""
    var_3 = input()
    var_3 = input()
    var_3 = input()
    var_4 = input()
    var_5 = input()
    var_6 = input()
    var_7 = input()

    if var_3.find("[") >= 0 and var_3.find("]") >= 0:
        var_3 = var_3[var_3.find("[")+1 : var_3.find("]")]
    else:
        var_3 = var_3[var_3.find("Pinging")+8 : var_3.find("with")-1]
    print("Ping statistics for %s:" % var_3)

    foureveryoung = check(var_4)+check(var_5)+check(var_6)+check(var_7)
    print("    Packets: Sent = 4, Received = %s, Lost = %s (%d%s loss)," % \
        ((4-foureveryoung), foureveryoung, ((foureveryoung*100)/4), "%"))

    if foureveryoung < 4:
        print("Approximate round trip times in milli-seconds:")
        time_1, time_2, time_3, time_4 = load(var_4, 0), load(var_5, 0), \
            load(var_6, 0), load(var_7, 0)
        if str(time_1).count("<") != 0 or str(time_2).count("<") != 0 or str(time_3).count("<") \
            != 0 or str(time_4).count("<") != 0:
            print("    Minimum = 0ms, Maximum = 0ms, Average = 0ms")
        else:
            mize(time_1, time_2, time_3, time_4, foureveryoung)
main()
# """main"""

# from math import floor

# def pure_time(time):
#     """turn value of get time to useable one"""
#     if time[0] == "=":
#         return int(time[1:])
#     elif time[0] == "<":
#         return 0
#     else:
#         return -1

# def get_time(reply):
#     """get time from reply"""
#     time = reply[reply.find('time')+4:reply.find('ms')]
#     return pure_time(time)

# def comp(rep1, rep2, rep3, rep4, condi):
#     """struggle"""
#     if rep4 == -1 and rep3 == -1 and rep2 == -1:
#         return rep1
#     elif rep4 == -1 and rep3 == -1:
#         if condi == 'min':
#             return min(rep1, rep2)
#         elif condi == 'max':
#             return max(rep1, rep2)
#     elif rep4 == -1:
#         if condi == 'min':
#             return min(rep1, rep2, rep3)
#         elif condi == 'max':
#             return max(rep1, rep2, rep3)
#     else:
#         if condi == 'min':
#             return min(rep1, rep2, rep3, rep4)
#         elif condi == 'max':
#             return max(rep1, rep2, rep3, rep4)

# def main():
#     """main"""
#     path = input()
#     space = input()
#     ping = input()
#     reply1 = input()
#     reply2 = input()
#     reply3 = input()
#     reply4 = input()
#     sum_time = 0
#     allreply = (reply1+reply2+reply3+reply4).count('Reply')
#     if "[" not in ping:
#         adde = path[-9:]
#     else:
#         adde = ping[ping.find('[')+1:ping.find(']')]
#     if get_time(reply1) >= 0:
#         sum_time += get_time(reply1)
#     if get_time(reply2) >= 0:
#         sum_time += get_time(reply2)
#     if get_time(reply3) >= 0:
#         sum_time += get_time(reply3)
#     if get_time(reply4) >= 0:
#         sum_time += get_time(reply4)
#     if allreply > 0:
#         avg = sum_time / allreply
#     less = comp(get_time(reply1), get_time(reply2), get_time(reply3), get_time(reply4), 'min')
#     most = comp(get_time(reply1), get_time(reply2), get_time(reply3), get_time(reply4), 'max')
#     print('Ping statistics for %s:' %adde)
#     print('    Packets: Sent = 4, Received = {}, Lost = {} ({}% Loss),'.format\
#         (allreply, 4-allreply, 100-(allreply*25)))
#     if allreply > 0:
#         print('Approximate round trip times in milli-seconds:')
#         print('    Minimum = %dms, Maximum = %dms, Average = %dms' %(less, most, floor(avg)))
#     print(space)
# main()
