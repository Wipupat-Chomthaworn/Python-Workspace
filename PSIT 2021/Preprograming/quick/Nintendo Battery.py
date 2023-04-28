'''Nintendo Battery'''
def main():
    '''ab'''
    per = int(input())
    var = int(input())
    var2 = var*per//100
    ful = 'O'*var2
    bat = '_'*(var - var2)
    per2 = '%'
    print("(%s%s) %d%s" %(ful, bat, per, per2))
main()
