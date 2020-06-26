studentScore = []
scoreList = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    studentScore.append([name, score])
    scoreList.append(score)

secondLowestScore = sorted(list(set(scoreList)))[1]

for name, score in sorted(studentScore):
    if score == secondLowestScore:
        print(name)
