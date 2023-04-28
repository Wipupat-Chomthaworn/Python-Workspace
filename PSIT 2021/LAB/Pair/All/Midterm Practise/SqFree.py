"""main"""
def main():
    """main"""
    count = 0
    for i in range(1, int(input())):
        for j in range(2, i):
            if i % j**2 == 0:
                count += 1
    print(count)
main()
