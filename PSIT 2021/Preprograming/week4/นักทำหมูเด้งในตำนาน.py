"""นักทำหมูเด้งในตำนาน"""
def main():
    '''ab'''
    var_1 = (input()).lower()
    keep = ''
    num = 0
    while True:
        if var_1 not in ('mh', 'ph', 'sh', 'wh', 'gh'):
            keep = ''
            print('ERROR')
        else:
            keep += var_1+','
        var_1 = input().lower()
        if var_1 == 'gh':
            if keep.count('mh') >= 1 and keep.count('ph') >= 1 and keep.count('sh') >= 1 and \
                keep.count('wh') >= 1:
                num += 1
                keep = ''
        if var_1 == 'end':
            print(num)
            break
main()
# elif var_1 == 'gh':
#             var_1 = (input()).lower()
# if var_1 not in ('mh', 'ph', 'sh', 'wh'):
#             print('ERROR')
# or var_1 not in ('mh', 'ph', 'sh', 'wh', 'gh', 'end')
