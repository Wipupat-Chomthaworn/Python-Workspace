"""Concurrent Timeline"""
def main():
    """anotherquest"""
    name = float(input())
    minit = name//1000#ออกมาเป็นวัน วัน1= 86400วิ
    minit2 = name%1000#เอาเศษมาใช้หารหาชม.ต่อ
    hour = minit2//500#หารหาชมใส่ช่อง
    hour2 = minit2%500#ได้เศษชมมาหารต่อ
    days = hour2//100#หารหานาทีใส่ช่อง
    days2 = hour2%100#ได้เศษนาที่มาหาวิต่อ
    days4 = days2//50#หารหานาทีใส่ช่อง
    days5 = days2%50#ได้เศษนาที่มาหาวิต่อ
    days6 = days5//20
    print(int(minit))
    print(int(hour))
    print(int(days))
    print(int(days4))
    print(int(days6))
main()
