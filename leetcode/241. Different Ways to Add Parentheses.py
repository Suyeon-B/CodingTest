def compute(left, right, op):
    results = []
    for l in left:
        for r in right:
            results.append(eval(str(l)+op+str(r)))
    return results

def diffWaysToCompute(expression):
    if expression.isdigit():
        return [int(expression)]

    results = []
    for idx, oper in enumerate(expression):
        if oper in "*-+":
            left = diffWaysToCompute(expression[:idx])
            right = diffWaysToCompute(expression[idx+1:])
            results.extend(compute(left, right, oper))
    return results


expression = "2*3-4*5"
print(diffWaysToCompute(expression))
        