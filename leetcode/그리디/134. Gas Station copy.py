# greedy 다시 풀어보기
def canCompleteCircuit(gas, cost):
    # gas랑 cost 묶어서 cost 기준 정렬
    gas_and_cost = []
    for i in range(len(gas)):
        gas_and_cost.append([gas[i], cost[i]])
    # gas_and_cost = sorted(gas_and_cost, key=lambda x:x[1])

    curr_gas = gas_and_cost[0][0]
    idx = 0
    success = True
    while idx < len(gas):
        can_go = curr_gas-gas_and_cost[idx][1]
        if can_go > 0:
            is_route = curr_gas-gas_and_cost[idx][1]+gas_and_cost[idx+1][0]
            if is_route>0:
                curr_gas = is_route
                continue
        else:
            success = False
        idx += 1

    if success:
        return gas_and_cost[0][0]-1
    else:
        return -1

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(canCompleteCircuit(gas, cost))
        