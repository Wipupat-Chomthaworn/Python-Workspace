"""L's number"""
def main():
    """anotherquest"""
    name = (int(input())//10000)
    name2 = (int(input())//10000)
    name3 = (int(input())//10000)
    name4 = int(input())
    name5 = (int((name4)//10000)%10)
    name6 = (int((name4)//1000)%10)
    name7 = (int((name4)//100)%10)
    name8 = (int((name4)//10)%10)
    print(int(name+name2+name3+name5+name6+name7+name8))
    #print("'%s' %02d/%02d/%4d"%(name, date, month, year))
    #print('%03d' % 8)
main()

