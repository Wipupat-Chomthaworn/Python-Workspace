"""Concurrent Timeline"""
def main():
    """anotherquest"""
    name = float(input())
    minit = name//86400#ออกมาเป็นวัน วัน1= 86400วิ
    minit2 = name%86400#เอาเศษมาใช้หารหาชม.ต่อ
    hour = minit2//3600#หารหาชมใส่ช่อง
    hour2 = minit2%3600#ได้เศษชมมาหารต่อ
    days = hour2//60#หารหานาทีใส่ช่อง
    days2 = hour2%60#ได้เศษนาที่มาหาวิต่อ
    print('%02d:%02d:%02d:%02d'%(minit, hour, days, days2))
    #print("'%s' %02d/%02d/%4d"%(name, date, month, year))
    #print('%03d' % 8)
main()
