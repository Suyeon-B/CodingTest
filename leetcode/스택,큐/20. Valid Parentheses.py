import collections


def isValid(s: str) -> bool:
    s = collections.deque(list(s))
    pairs = collections.defaultdict(list)
    pairs[')'], pairs['}'], pairs[']'] = '(', '{', '['

    open_brackets = [s.popleft()]
    while s:
        cur = s.popleft()
        if open_brackets and open_brackets[-1] == pairs[cur]:
            open_brackets.pop()
        else:
            open_brackets.append(cur)
    if len(open_brackets):
        return False
    else:
        return True


if __name__ == '__main__':
    s = "()[]{}"
    print(isValid(s))
