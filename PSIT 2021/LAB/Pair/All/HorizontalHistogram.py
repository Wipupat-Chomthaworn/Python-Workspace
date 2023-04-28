"""HorizontalHistogram"""
def main():
    """HorizontalHistogram"""
    message = input()
    low = []
    upp = []
    ans = ""
    for i in message:
        if i.islower():
            low.append(i)
        if i.isupper():
            upp.append(i)
    for i in sorted(list(set(low))):
        for j in range(1, message.count(i)+1):
            ans += "-"
            if j % 5 == 0 and j != message.count(i):
                ans += "|"
        print("%s : %s"%(i, ans))
        ans = ""
    for i in sorted(list(set(upp))):
        for j in range(1, message.count(i)+1):
            ans += "-"
            if j % 5 == 0 and j != message.count(i):
                ans += "|"
        print("%s : %s"%(i, ans))
        ans = ""
main()
