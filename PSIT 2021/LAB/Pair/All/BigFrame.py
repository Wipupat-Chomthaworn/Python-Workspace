"""[Midterm] BigFrame"""
def bigframe():
    """[Midterm] BigFrame"""
    var = input().strip()
    var1 = input().strip()#strip หน้าหลังstrip arg
    var2 = input().strip()
    var3 = input().strip()
    var4 = input().strip()
    size = max(len(var), len(var1), \
        len(var2), len(var3), len(var4))
    print('*'*(size+4))
    tup = (var, var1, \
        var2, var3, var4)
    for i in range(5):
        print('* %s%s'%(tup[i], ' '*(size-len(tup[i]))), end='')
        print(' *')
    print('*'*(size+4))
bigframe()
# """BigFrame"""
# def big_frame():
#     """print Frame contains words in it"""
#     word_1 = input().strip()
#     word_2 = input().strip()
#     word_3 = input().strip()
#     word_4 = input().strip()
#     word_5 = input().strip()
#     size = max(len(word_1), len(word_2), len(word_3), len(word_4), len(word_5))
#     print("*"*int(size+4))
#     print("*"+" "+word_1+(size-len(word_1))*" "+" "+"*")
#     print("*"+" "+word_2+(size-len(word_2))*" "+" "+"*")
#     print("*"+" "+word_3+(size-len(word_3))*" "+" "+"*")
#     print("*"+" "+word_4+(size-len(word_4))*" "+" "+"*")
#     print("*"+" "+word_5+(size-len(word_5))*" "+" "+"*")
#     print("*"*int(size+4))
# big_frame()
