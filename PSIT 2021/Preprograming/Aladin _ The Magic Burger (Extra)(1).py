"""Aladin & The Magic Burger (Extra)"""
def main():
    '''ab'''
    max1 = (input())
    solf = (max1.lower().find('burger'))
    solbur = '{}'*solf
    solbread = len(max1)%10
    solbread2 = '(|'*solbread
    solbread3 = '|)'*solbread
    print('%s%s%s'%(solbread2, solbur, solbread3))
main()
