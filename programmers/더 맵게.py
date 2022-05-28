import heapq 


def solution(scoville, K):
    """
    섞은 음식의 스코빌 지수 = 
            가장 맵지 않은 음식의 스코빌 지수 + 
            (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

    최소힙 
        먼저 뽑은 음식 - 제일 안 매운 음식 스코빌
        두 번째로 뽑은 음식 - 두 번째로 안 매운 스코빌
    
    두 번 뽑고 식에 맞게 더해서 최소힙에 다시 넣는다.
    제일 안 매운 게 K이상이면 그만 섞는다.
    """
    heapq.heapify(scoville)
    MIN = heapq.heappop(scoville)
    cnt = 0
    while MIN<K:
        if len(scoville) < 1:
            cnt = -1
            break
        MIN_2nd = heapq.heappop(scoville)
        mixed = MIN + MIN_2nd*2
        cnt +=1 
        heapq.heappush(scoville, mixed)
        MIN = heapq.heappop(scoville)
    return cnt

scoville = [1, 2, 3, 9, 10, 12]	
K = 7
print(solution(scoville, K))
