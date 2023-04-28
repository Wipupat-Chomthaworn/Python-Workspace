"""[Midterm] ValidVar"""
def main():
    '''main func'''
    def space(arg):
        '''buitins'''
        if arg in ("if", "else", "elif", "while", "for", "True", "False", "continue", "break"\
            , "return", "is", "in", "and", "or", "from", "as", "pass", "not", "def", "None"):
            return False
        else:
            return True
    num = int(input())
    for _ in range(num):
        var = input()
        if var.isidentifier() and space(var):
            print('Valid')
        else:
            print('Invalid')
main()
