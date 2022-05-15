# product 사용 풀이버전
from itertools import product
def letterCombinations(digits):
    lists_num = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    
    if len(digits) == 4:
        list_product = list(product(lists_num[int(digits[0])-2],lists_num[int(digits[1])-2],lists_num[int(digits[2])-2],lists_num[int(digits[3])-2]))
    elif len(digits) == 3:
        list_product = list(product(lists_num[int(digits[0])-2],lists_num[int(digits[1])-2],lists_num[int(digits[2])-2]))
    elif len(digits) == 2:
        list_product = list(product(lists_num[int(digits[0])-2],lists_num[int(digits[1])-2]))
    elif len(digits) == 1:
        list_product = list(product(lists_num[int(digits[0])-2]))
    else:
        list_product = []


    output = []
    for i in list_product:
        output.append("".join(i))
    return output



digits = "2"
print(letterCombinations(digits))