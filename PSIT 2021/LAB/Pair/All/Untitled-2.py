


x = 3
delx = 0.5
keep = 0
for i in range(8):
    keep += (2*(x**2) - 1)*delx
    x += delx
    print('+++%d'%x)
    print(keep)