"""cutecat2"""
def main():
    """main"""
    many = int(input())
    dict1 = {}
    set1 = [("Garfield", 'Cat01'), ('Fubuki', 'Fox01')]
    for _ in range(many):
        inp = input()
        if len(inp.split('"')) > len(inp.split("'")):
            dict1[inp.split('"')[1]] = inp.split('"')[3]
        else:
            dict1[inp.split("'")[1]] = inp.split("'")[3]
    dict1 = list(dict1.items())
    for i in range(len(dict1)):
        if len(set1) == 0:
            break
        if dict1[i][0] == "Garfield" or dict1[i][1] == "Cat01" and\
                ("Garfield", 'Cat01') in set1:
            set1.remove(("Garfield", 'Cat01'))
        elif dict1[i][0] == 'Fubuki' or dict1[i][1] == 'Fox01' and \
                ('Fubuki', 'Fox01') in set1:
            set1.remove(('Fubuki', 'Fox01'))
    dict1.extend(set1)
    cat, fox, dict1 = {}, {}, dict(dict1)
    for i in sorted(dict1, key=lambda x: int(dict1[x].replace("Cat", "").replace("Fox", ""))):
        if dict1[i].count('Cat') > 0:
            cat[i] = dict1[i]
        if dict1[i].count('Fox') > 0:
            fox[i] = dict1[i]
    print('Cat : %d' % len(cat))
    print('Fox : %d' % len(fox))
    for i in cat:
        print("%s : %s" % (i, cat[i]))
    for i in fox:
        print("%s : %s" % (i, fox[i]))
main()
