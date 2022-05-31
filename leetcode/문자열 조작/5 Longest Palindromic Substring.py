# 중간 문자를 뛰어 넘고 추가하면 안되는 문제였음
import collections


def main():
    s = "eabcb"

    result = ""

    # 예외 처리
    if len(set(s)) == len(s):
        return s[0]
    else:
        for i in range(len(s)):
            string = s[i:]
            deq = collections.deque(list(string))
            arr = list(string)
            temp = ""
            while arr:
                d = deq.popleft()
                a = arr.pop()
                if a == d:
                    temp += a
                else:
                    deq.appendleft(d)

            if len(result) < len(temp):
                result = temp
        return result


print(main())
