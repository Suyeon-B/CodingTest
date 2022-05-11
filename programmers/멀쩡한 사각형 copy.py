import math


def solution(w, h):
    answer = 0

    def recur(w, h):
        nonlocal answer

        if w == 1 or h == 1:
            return

        answer += 2 * (w//2) * (h//2)
        left_up = recur(math.ceil(w/2), math.ceil(h/2))
        right_up = recur(math.ceil(w/2), math.ceil(h/2))
        if left_up and right_up:
            answer = left_up+right_up

    recur(w, h)
    return answer
