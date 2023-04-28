"""Kabata"""
def main():
    """main"""
    num = int(input())
    anslist = []
    check = ''
    for _ in range(num):
        string = str(input())
        string = string.replace("bakka", "34")

        if len(string) % 2 == 0 and string.count("baka") < 1:
            iskabata = 'yes'
            for i in range(0, len(string), 2):
                check = string[i:i+2]
                if check == "ka" or check ==\
                        "ba" or check == "ta" \
                            or check == "34":
                    iskabata = 'yes'
                else:
                    iskabata = 'no'
                    break
            anslist.append(iskabata)
        else:
            anslist.append('no')
    for i in anslist:
        print(i)
main()
