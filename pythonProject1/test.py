stack = []
myBoard = []


def myPop(answer):
    if len(stack) > 1:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            return answer + 1
    return answer


def draw(move):
    global myBoard
    for i in range(len(myBoard)):
        if myBoard[i][move - 1] != 0:
            stack.append(myBoard[i][move - 1])
            myBoard[i][move - 1] = 0
            return
    return


def solution(board, moves):
    answer = 0
    global myBoard
    myBoard = board
    for move in moves:
        draw(move)
        answer = myPop(answer)

    return answer
