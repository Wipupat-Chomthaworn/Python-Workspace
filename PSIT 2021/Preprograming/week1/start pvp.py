"""start pvp"""
def main():
    """anotherquest"""
    name_1 = (input())
    ph_1 = int(input())*'O'
    atk_p = int(input())
    defe = int(input())
    name2 = (input())
    ph_12 = int(input())*'O'
    atk_p2 = int(input())
    defe2 = int(input())
    print('##############')
    print('# %10s #'%(name_1))
    print("# HP:%7s #" %(ph_1))
    print("# ATk || DEF #")
    print('# %04d||%04d #'%(atk_p, defe))
    print('############## VS ##############')
    print('                  # %10s #'%(name2))
    print('                  # HP:%7s #' %(ph_12))
    print('                  # ATk || DEF #')
    print('                  # %04d||%04d #'%(atk_p2, defe2))
    print('                  ##############')
    #print('[" %5.2f "]'%(sum1))
    #print("'%s' %02d/%02d/%4d"%(name, date, month, year))
    #print('%03d' % 8)
main()
