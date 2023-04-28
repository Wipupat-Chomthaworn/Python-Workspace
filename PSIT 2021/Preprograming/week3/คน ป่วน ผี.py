"""คน ป่วน ผี"""
def main():
    '''ab'''
    sol = int(input())
    solall = (sol%10+(sol%100//10)+\
        (sol%1000//100)+(sol%10000//1000)+(sol%100000//10000))
    if (solall % 2 == 0) and (solall % 4 == 0):
        print('ผีตานี')
    elif (solall % 2 == 0) and (solall % 4 != 0):
        print('ผีกระหัง')
    elif (solall % 2 != 0) and (solall % 5 == 0):
        print('ผีกระสือ')
    elif (solall % 2 != 0) and (solall % 5 != 0):
        print("ผีปอบ")
main()
