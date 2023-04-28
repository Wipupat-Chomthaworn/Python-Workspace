'''[Midterm] Diginity'''
def sumans():
    '''sum ans'''
    while True:
        var = input()
        if var == '0':
            break
        while True:
            point = 0
            for digit in var:
                point += int(digit)
            if len(str(point)) == 1:
                break
            var = str(point)
        print(point)
sumans()
