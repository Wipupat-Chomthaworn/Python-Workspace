"""AlmostMean"""
def main(num):
    """AlmostMean"""
    student = []
    score = []
    for _ in range(num):
        word = input().split("\t")
        student.append(word[0])
        score.append(float(word[1]))
    avg = sum(score)/len(score)
    ans = avg
    for i in range(num):
        if score[i] < avg and avg-score[i] < ans:
            ans = avg-score[i]
            anst, anst2 = student[i], score[i]
    print(anst, anst2, sep="\t")
main(int(input()))
