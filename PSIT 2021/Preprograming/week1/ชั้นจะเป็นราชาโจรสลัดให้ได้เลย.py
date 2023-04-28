"""timetosec"""
def main():
    """def"""
    num = float(input())
    sec = int(num)
    sec_2 = (num - sec)*100
    sec_3 = int((sec*60)+(sec_2))
    print(sec_3)
main()
