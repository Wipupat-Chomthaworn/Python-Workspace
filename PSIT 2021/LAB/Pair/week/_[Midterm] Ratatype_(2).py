'''[Midterm] Ratatype'''
def main():
    '''ab'''
    var_1 = 'In Deep Learning, a Convolutional Neural Network (CNN) is a'
    var_1 += ' class of Deep Neural Networks, most commonly applied to analyzing visual imagery.'
    var_2 = '"Two things are infinite: the universe and'
    var_2 += ' human stupidity; and I\'m not sure about the universe". - Albert Einstein'
    var_3 = 'Statistics is the discipline that concerns the collection,'
    var_3 += ' organization, displaying, analysis, interpretation and presentation of data.'
    var_4 = 'The backslash (\\) is a typographical mark used mainly in computing'
    var_4 += ' and is the mirror image of the common slash (/).'
    var_4 += ' It is sometimes called "escape character".'
    varans = (var_1, var_2, var_3, var_4)
    def findword():
        '''findword'''
        ans = int(input())-1
        for i in range(5):
            if i == ans:
                print(varans[i])
    findword()
main()
