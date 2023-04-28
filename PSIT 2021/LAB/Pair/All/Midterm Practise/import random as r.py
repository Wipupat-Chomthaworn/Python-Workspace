"""main"""
def main():
    """main"""
    path = input()
    space = input()
    ping = input()
    reply1 = input()
    reply2 = input()
    reply3 = input()
    reply4 = input()
    time1 = reply1[reply1.find('time')+5:reply1.find('ms')]
    time2 = reply2[reply2.find('time')+5:reply2.find('ms')]
    time3 = reply3[reply3.find('time')+5:reply3.find('ms')]
    time4= reply4[reply4.find('time')+5:reply4.find('ms')]
    print(time1)
    print(time2)
    print(time3)
    print(time4)
    # allreply = (reply1+reply2+reply3+reply4).count('Reply')
    # if '127.0.0.1' in ping:
    #     adde = '127.0.0.1'
    # else:
    #     adde = ping[ping.find('[')+1:ping.find(']')]
    # print('Ping statistics for %s:' %adde)
    # print('    Packets: Sent = 4, Received = {}, Lost = {} ({}% Loss),'.format\
    #     (allreply, 4-allreply, 100-(allreply*25)))
    # if allreply > 0:
    #     minimun = 
main()


#https://discord.gg/P8QC5sTU


# C:\Users\chotipat>ping www.google.com

# Pinging www.google.com [2404:6800:4001:806::2004] with 32 bytes of data:
# Reply from 2404:6800:4001:806::2004: time=27ms
# Reply from 2404:6800:4001:806::2004: time=28ms
# Reply from 2404:6800:4001:806::2004: time=33ms
# Reply from 2404:6800:4001:806::2004: time=28ms
#output
# Ping statistics for 2404:6800:4001:806::2004:
#     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# Approximate round trip times in milli-seconds:
#     Minimum = 27ms, Maximum = 33ms, Average = 29ms