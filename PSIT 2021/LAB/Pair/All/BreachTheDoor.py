"""BreachTheDoor"""

def main():
    """BreachTheDoor"""
    st1, lst = str(input()).split(" "), []
    for i in st1:
        if len(i) > 6:
            st2 = ""
            for j in i:
                if j.isalpha():
                    st2 += j
            if len(st2) > 6:
                lst.append(st2)
    print(*lst, end=" ")
main()
