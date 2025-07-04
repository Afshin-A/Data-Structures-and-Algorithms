from pprint import pprint
s = ['c', 'b', 'c']
from icecream import ic


# time complexity 2^n
def subsets(index, path, l) -> list:
    # base case:
    # found a solution
    if index == len(l):
        return [path]
    else:
        return subsets(index+1, path, l) + subsets(index+1, path+[l[index]], l)
    

# print(subsets(0, [], s))


def subsets_backtracking(l):
    solution = []
    path = []
    
    def dfs(index):
        if index == len(l):
            solution.append(path[:])
            return
        else:
            # do nothing
            # explore path
            dfs(index+1)
            # include current path
            path.append(l[index])
            # explore path
            dfs(index+1)
            # backtrack
            path.pop()
    dfs(0)
    
    return solution




def knapsack(wt: list, val: list, cap: int, index: int) -> int:
    if index == len(wt):
        return 0
    
    not_pick = knapsack(wt, val, cap, index + 1)
    pick = 0
    if wt[index] <= cap:
        pick = val[index] + knapsack(wt, val, cap - wt[index], index + 1)
    
    return max(pick, not_pick)

# print(knapsack(weights, values, 7, 0))

# if we draw the tree form of this problem, we can characterize each node as (index, capacity_remaining)
def knapsack_memoization(weights, values, max_capacity):
    '''
    Worst Time Complexity: O(n*max_capacity)
    This is because it's the size of our dp table, and that is how many nodes there are. And every node is calculated only once. 
    '''
    n = len(weights)
    dp = [[-1 for _ in range(max_capacity+1)] for _ in range(n)]
    
    def helper(index, capacityRemaining):
        if index == n:
            return 0
        
        # if the solution for this node has been calculated before, we immediately return it and skip performing calculations/traverse deeper
        if dp[index][capacityRemaining] != -1:
            return dp[index][capacityRemaining]
        # decision: skip current index, capacity is unchanged
        not_picked = helper(index + 1, capacityRemaining)
        # decision: use the current index, but only is the remaining capacity allows to use the current element
        picked = 0
        if weights[index] <= capacityRemaining:
            # remaining capacity gets reduced 
            picked = values[index] + helper(index + 1, capacityRemaining - weights[index])
        
        # store the solution 
        dp[index][capacityRemaining] = max(not_picked, picked)
            
        return dp[index][capacityRemaining]
        
    return helper(0, max_capacity)



# NOTE: This specific problem can further be optamized
# we can use a 1D array to save values
# at each row, we only access the values of the previous row
# so we can keep updating the values in place
# NOTE: the trick is that we have to iterate each row from right to left 
def knapsack_tabulation(weights, values, max_capacity):
    # initialize everything to 0
    dp = [[0 for _ in range(max_capacity+1)] for _ in weights]
    
    # initialize first row 
    for current_capacity in range(1, max_capacity+1):
        if current_capacity >= weights[0]:
            dp[0][current_capacity] = values[0]
    
    # we skip loop 0 and columns 1 to avoid out of range errors
    # column 0 is initialized to 0 by default
    for index in range(1, len(weights)):
        for current_capacity in range(1, max_capacity+1):
            # scenario 1: don't pick the current element
            # what is the best value of the previous objects at the current capacity?
            not_pick_current = dp[index-1][current_capacity]
            # scenario 2: pick the current element
            pick_current = 0
            # can we even add the current element? does its weight allow that?
            if weights[index] <= current_capacity:
                # adding value of current element
                pick_current += values[index]
                # how much capacity are we left with?
                remaining_capacity = current_capacity-weights[index]
                # okay, we've used the current element. what's the best value out of the elements up to B with the remaining capacity?
                pick_current += dp[index-1][remaining_capacity]
            # which one gives more value? adding the current element, or not adding it?
            dp[index][current_capacity] = max(not_pick_current, pick_current)

    return dp[len(weights)-1][max_capacity]


def knapsack_unbounded(items: dict[str, tuple[int, int]], max_capacity: int) -> int:
    dp = {}
    def helper(current_value, current_path, capacityRemaining):
        if capacityRemaining in dp:
            return dp[capacityRemaining]
        
        choices = []
        for item in items:
            weight, value = items[item]
            if weight <= capacityRemaining:
                choices.append(
                    helper(current_value + value, current_path + [item], capacityRemaining - weight)
                )
                
        dp[capacityRemaining] = max(choices) if choices else (current_value, current_path)
        return dp[capacityRemaining]
        
    
    return helper(0, [], max_capacity)
            
def knapsack_unbounded_tabulation(items:  dict, max_capacity):
    dp = [0 for _ in range(max_capacity+1)]
    
    for current_capacity in range(1, len(dp)):
        max_value = 0
        for weight, value in items.values():
            if weight <= current_capacity:
                max_value = max(max_value, value + dp[current_capacity - weight])
        dp[current_capacity] = max_value
    print(dp)
    return dp[-1]

# weights = [1, 3, 4, 5]
# values = [15, 20, 30, 50]
# ic(knapsack_tabulation(weights, values, 7))

# ic(knapsack_memoization(weights, values, 7))

items = {
    'A': (1, 15),
    'B': (3, 20),
    'C': (4, 30),
    'D': (5, 50)
}
# ic(knapsack_unbounded(items, 7))
# test = {
#     (1, 2): 1,
#     (2, 3): 2,
#     (1, 2, 3): 3,
    
# }


# ic(knapsack_unbounded_tabulation(items, 7))


def coinChangeMemoization(coins: list, target: int) -> int:
    smallest = min(coins)
    # maximum number of coins 
    inf = (target // smallest) + 1
    dp = [inf for _ in range(target+1)]
    optimizationCount = 0
    def makeChange(changeRemaining, numCoins):
        nonlocal inf
        nonlocal optimizationCount
        
        if dp[changeRemaining] != inf:
            optimizationCount += 1
            return dp[changeRemaining]
        
        # base cases:
        if changeRemaining == 0:
            # found a solution
            return numCoins
        if changeRemaining < 0:
            # solution does not exist
            return inf
        
        fewest = inf
        for coin in coins:
            fewest = min(fewest, makeChange(changeRemaining-coin, numCoins+1))
        
        dp[changeRemaining] = fewest
        return dp[changeRemaining]
                
    result = makeChange(target, 0)
    print(optimizationCount)      
    return -1 if result == inf else result

# print(coinChangeMemoization([25, 10, 5], 75))

def coinChangeTabulation(coins, target):
    dp = [float('inf') for _ in range(target+1)]
    dp[0] = 0
    
    for currentTarget in range(1, target+1):
        
        for coin in coins:
            if coin <= target:
                dp[currentTarget] = min(dp[currentTarget], 1 + dp[currentTarget - coin])
        
    pprint(list(enumerate(dp)))
    return dp[target]
            
ic(coinChangeTabulation([1, 5, 10, 25, 100], 761))
        
