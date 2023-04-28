'''[Midterm] Parallelogram'''
def main():
    """main function"""
    var = input()
    for i in range(len(var)):
        print(' '*(len(var)-i-1) + var[:i+1])
    for j in range(len(var), 0, -1):
        print(var[len(var)-j+1:])
main()
#          S
#         Sa
#        Sam
#       Samp
#      Sampl
#     Sample
#    SampleT
#   SampleTe
#  SampleTex
# SampleText
# ampleText
# mpleText
# pleText
# leText
# eText
# Text
# ext
# xt
# t
