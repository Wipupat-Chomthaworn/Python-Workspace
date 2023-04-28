"""Prime"""
def main():
    """Prime"""
    inputs = abs(int(input()))
    count = 0
    if inputs > 1:
        for num in range(2, inputs+1):
            i = 1
            for i in range(2, num):
                if num % i == 0:
                    i = num
                    break
            if i != num:
                count += 1
            else:
                continue
    print(count)
main()
