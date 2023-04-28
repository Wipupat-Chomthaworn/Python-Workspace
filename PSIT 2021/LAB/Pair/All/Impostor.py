"""main"""
def main():
    """main"""
    # import json
    dict1 = {}
    death = {}
    while True:

        var = input()
        if var == 'Start':
            break
        dict1[var[1:var.find(":")].strip().\
            replace("\"", "")] = var[var.find(":")+1:-1].\
                strip().replace("\"", "")
        # print(dict1)
    while True:
        var = input()
        if var == 'End':
            break
        death[var] = dict1.pop(var).strip()
    # print(dict1, list(dict1.values()))
    print('%d Impostor Remains'%list(dict1.values()).count("Impostor"))
    print('***Alive***')
    for i in sorted(dict1.keys()):
        print('%s : %s'%(i, dict1[i]))
    # death = sorted(death)
    print('***Dead***')
    for i in sorted(death.keys()):
        print('%s : %s'%(i, death[i]))

main()
