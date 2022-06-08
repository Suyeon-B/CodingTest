from collections import defaultdict


def characterReplacement(s,k):
    if len(s) == 1:
        return 1
    
    dict = defaultdict(int)
    l, r = 0, 1
    dict[s[l]]+=1
    dict[s[r]]+=1
    output = 0

    while r < len(s):
        result = max(dict.values())
        if sum(dict.values())-max(dict.values())>k:
            output = max(output, sum(dict.values()))
            l, r = r, r+1
            dict = defaultdict(int)
            dict[s[l]]+=1
            dict[s[r]]+=1
        else:
            r = r+1
            if r>len(s):
                break
            dict[s[r]]+=1
    return max(output, sum(dict.values()))

s = "AABABBA"
k = 1
print(characterReplacement(s,k))