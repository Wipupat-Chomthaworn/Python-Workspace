"""main"""
def main():
    """main"""
    sta = 'l'
    people = 0
    while True:
        var = input().lower()
        if var == "end":
            break
        if var == 'c':#เปลี่ยน status เมื่อ ct
            sta = 'ul'
        elif sta == 'ul' and var == 'p':
            people += 1
            sta = 'l'
    print(people)
main()
