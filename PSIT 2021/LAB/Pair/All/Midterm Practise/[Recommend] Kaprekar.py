"""main"""
def answer(var):
    """findans"""
    var = list(var)
    var2 = list(var)
    for i in range(len(var)):
        for j in range(i + 1, len(var)):
            if var[i] > var[j]:
                var[i], var[j] = var[j], var[i]
    for i in range(len(var2)):
        for j in range(i + 1, len(var2)):
            if var2[i] < var2[j]:
                var2[i], var2[j] = var2[j], var2[i]
    # print(var, var2)
    rev = ''.join(var2)
    upp = ''.join(var)
    # print(rev, upp)
    ans = str(int(rev)-int(upp)).zfill(4)
    return ans
def main():
    """mainb"""
    var = input()
    keep = 0
    ans = var
    while int(ans) != 6174:
        keep += 1
        ans = answer(ans)
    print(keep)
main()
# '''[Recommend] Kaprekar'''
# def arrange(line):
#     '''main'''
#     for run1 in range(4):
#         for run2 in range(4):
#             if line[run1] < line[run2]:
#                 temp_line = ""
#                 for run3 in range(4):
#                     if run3 == run1:
#                         temp_line += line[run2]
#                     elif run3 == run2:
#                         temp_line += line[run1]
#                     else:
#                         temp_line += line[run3]
#                 line = temp_line
#     return line
 
# def main():
#     '''main'''
#     line = input()
 
#     counter = 0
#     while line != "6174":
#         line = arrange(line)
#         line_reversed = line[::-1]
#         line = "%04d"%(abs(int(line)-int(line_reversed)))
#         counter += 1
#     print(counter)
# main()
# """[Midterm] Kaprekar"""
# def main():
#     """work"""
#     num = input()
#     n_count = 0
#     while num != "6174":
#         n_1 = int(num[0])
#         n_2 = int(num[1])
#         n_3 = int(num[2])
#         n_4 = int(num[3])
#         for _ in range(3):
#             if n_1 > n_2:
#                 n_1, n_2 = n_2, n_1
#             if n_2 > n_3:
#                 n_2, n_3 = n_3, n_2
#             if n_3 > n_4:
#                 n_3, n_4 = n_4, n_3
#         sum1 = int(str(n_4)+str(n_3)+str(n_2)+str(n_1))
#         sum2 = int(str(n_1)+str(n_2)+str(n_3)+str(n_4))
#         num = sum1 - sum2
#         num = str("%04d" %(num))
#         n_count += 1
#     print(n_count)
# main()
