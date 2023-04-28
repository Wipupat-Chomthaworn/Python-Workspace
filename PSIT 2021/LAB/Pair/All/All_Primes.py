""""All_Primes"""
def main():
    """"main"""
    num = int(input())
    count = 0
    for i in range(1, num+1):
        check = True
        if i == 1:
            check = False
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check == True:
            count += 1
    print(count)
main()
