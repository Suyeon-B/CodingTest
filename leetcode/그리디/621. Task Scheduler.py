from collections import Counter


def leastInterval(tasks, n):
    if n == 0:
        return len(tasks)
    
    cnt = Counter(tasks)
    max_freq = max(cnt.values())
    max_freq_cnt = len(cnt.most_common())
    interval_schedule = (max_freq-1)*(n+1) + max_freq_cnt

    return max(len(tasks), interval_schedule)

tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks, n))
        