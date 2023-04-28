"""main"""
def main():
    """main"""
    var = input()
    keep = ''
    for i in var:
        if var.count(i) % 2 != 0:
            if i not in keep:
                keep += i
    if keep == '':
        print('fully paired')
    else:
        print(keep)
main()
