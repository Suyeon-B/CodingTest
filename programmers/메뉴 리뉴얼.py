from itertools import combinations
from typing import Counter


def solution(orders, course):
    cnts = Counter("".join(orders))
    # cnt value가 <2라면 제거
    candidate_menu = {}
    for key, value in cnts.items():
        if value >= 2:
            candidate_menu[key] = value
    # 조합으로 course 개의 조합을 만듦
    orders.sort(key=len)
    candidate_courses = []
    for num_of_menu in course:
        if len(orders[-1]) > num_of_menu:
            course_list = list(combinations(candidate_menu.keys(), num_of_menu))
            for candidate_course in course_list:
                candidate_courses.append("".join(candidate_course))
        else:
            continue
    
    # 그 조합이 사람들의 주문에 2번 이상 등장하면 answer에 추가
    # for can


    # return candidate_courses
    return orders

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))