"""[Recommend] Ping"""
def check(this):
    """1"""
    if this.count("out.") > 0 or this.count("fail") > 0:
        return 1
    else:
        return 0
def reply(this, num):
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


def time_cal(time1, time2, time3, time4, received):
    """3"""
    time__1, time__2, time__3, time__4 = reply(time1, 1), \
        reply(time2, 1), reply(time3, 1), reply(time4, 1)
    maxi = max(int(time__1), int(time__2), int(time__3), int(time__4))
    time__1, time__2, time__3, time__4 = reply(time1, 2), \
        reply(time2, 2), reply(time3, 2), reply(time4, 2)
    mini = min(int(time__1), int(time__2), int(time__3), int(time__4))
    time__1, time__2, time__3, time__4 = reply(time1, 3), \
        reply(time2, 3), reply(time3, 3), reply(time4, 3)
    print("    Minimum = %dms, Maximum = %dms, Average = %dms" % \
        (mini, maxi, (int(time__1)+int(time__2)+int(time__3)\
        +int(time__4))/abs(received-4)))


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

    received = check(var_4)+check(var_5)+check(var_6)+check(var_7)
    print("    Packets: Sent = 4, Received = %s, Lost = %s (%d%s loss)," % \
        ((4-received), received, ((received*100)/4), "%"))


    if received < 4:
        print("Approximate round trip times in milli-seconds:")
        time1, time2, time3, time4 = reply(var_4, 0), reply(var_5, 0), \
            reply(var_6, 0), reply(var_7, 0)
        if str(time1).count("<") != 0 or str(time2).count("<") != 0 or str(time3).count("<") \
            != 0 or str(time4).count("<") != 0:
            print("    Minimum = 0ms, Maximum = 0ms, Average = 0ms")
        else:
            time_cal(time1, time2, time3, time4, received)

main()
