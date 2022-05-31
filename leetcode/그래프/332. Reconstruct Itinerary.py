import collections


def findItinerary(tickets):
    dict = collections.defaultdict(list)
    for FROM, TO in sorted(tickets):
        dict[FROM].append(TO)

    route = []

    def dfs(a):
        while dict[a]:
            dfs(dict[a].pop(0))
        route.append(a)

    dfs("JFK")
    return route[::-1]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(findItinerary(tickets))

# ["JFK","ATL","JFK","SFO","ATL","SFO"]
