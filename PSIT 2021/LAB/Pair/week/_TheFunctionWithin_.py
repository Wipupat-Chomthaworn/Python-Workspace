'''TheFunctionWithin'''
def main():
    '''TheFunctionWithin'''
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
    def funcx(num):
        '''fx'''
        fcx = num*2
        return fcx
    def fungx(xxx):
        """g(x)"""
        fgx = 3*pow(xxx, 4)- pow(xxx, 3) + 2*pow(xxx, 2)+ 10
        return fgx
    def hxyz(xxx, yyy, zzz):
        '''h(x)'''
        fhyx = ((zzz+xxx)**2 - (xxx*yyy)+ (yyy**2))
        return fhyx
    def iabc(vara, varb, varc, vard):
        '''i(abcd)'''
        fabcd = (vara**2 + varb**2 -varc**2) /((vard**2)-(2*vara*vard)+(2*vara))
        return fabcd
    print(funcx(funcx(var_a)))
    print(fungx(funcx((var_a-var_b))))
    print(hxyz(funcx((var_a+var_b)), funcx((var_a+var_c)), fungx(funcx(pow(var_d, 2)))))
    print(iabc(hxyz(funcx((var_a+var_b)), funcx((var_a-var_c)), \
    fungx(funcx(pow(var_d, 2)))), \
    fungx(funcx((var_a-var_b))), \
    funcx(funcx(funcx(funcx(funcx(var_c))))), pow(var_d, 8)))
main()
