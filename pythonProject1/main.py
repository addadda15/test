def solution(n):
    numList = []
    cnt = 1

    for i in range(n):
        tmpList = []
        for j in range(cnt , cnt + n -i):
            tmpList.append(j)
        numList.append(tmpList)

def myOutput():


    answer = []
    return answer