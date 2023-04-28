'''EuclideanDistance2D'''
def main():
    '''ab'''
    uxx = float(input())
    uyy = float(input())
    a_x = float(input())
    a_y = float(input())
    a_to_me = (((uxx-a_x)**2)+(uyy-a_y)**2)**0.5
    print(a_to_me)
main()
