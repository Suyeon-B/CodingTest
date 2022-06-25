def solution(board, moves):
    """
    배열 돌면서 movs[n]열 스택에 넣기 시도
    같은 게 끝에 있으면 터뜨림, 결과 += 1
    """
    stack = []
    answer = 0
    for m in moves:
        for i, b in enumerate(board):
            if b[m-1]:
                if stack and stack[-1] == b[m-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(b[m-1])
                board[i][m-1] = 0
                break
    
    return answer

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	
print(solution(board, moves)) # 4