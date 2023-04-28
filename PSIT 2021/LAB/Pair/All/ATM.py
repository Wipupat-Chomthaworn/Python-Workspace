"""ATM"""
def main():
    """main"""
    save = int(input())
    inp = 0
    while True:
        var = input()
        if var == "END":
            break
        if var.split()[0] == "W":
            inp = save - int(var.split()[1])
            if inp <= 0:
                save = 0
            else:
                save -= int(var.split()[1])
        elif var.split()[0] == "D":
            save += int(var.split()[1])
        # print(save)
    print(save)
main()
