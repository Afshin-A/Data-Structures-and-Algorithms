from random import randint
from math import floor

def subsets_tree_solution(l: list[int]) -> list[int]:
    '''
    Explicitly solves the problem by first creating a complete binary tree. The leaf nodes are the subsets
    Returns all possible subsets of the given list

    for each level:
        for each node in that level
            left child --> don't include the level
            right child --> include the level
    '''
    # initialize a complete tree
    solution = []
    # total number of nodes
    total_nodes = pow(2, len(l)+1) - 1
    # number of internal nodes
    internal_nodes = floor(total_nodes / 2)
    # initialize each node to an empty list
    for i in range(total_nodes):
        solution.append([])
    # these determine the range of indices for the nodes in each level in the tree
    i, j = 0, 0
    # we use index because we need it to calculate i and j
    # we iterate through each element in the array
    for level in range(len(l)):
        level_element = l[level]
        for node in range(i, j+1):
            # index of left child
            node_left = node * 2 + 1
            # index of right child
            node_right = node_left + 1
            # we need to copy the parent to the child, then build on top of it
            solution[node_left] = solution[node].copy()
            solution[node_right] = solution[node].copy()
            # we either don't add the element, which translates to doing nothing
            # do_nothing()
            # or we add the element
            solution[node_right].append(level_element)
        i = j+1
        j += pow(2, level+1)
    return solution[internal_nodes:]


# l = [randint(1, 10) for _ in range(3)]
l = [1, 2, 3]
# print(l)
print(sorted(subsets_tree_solution(l)))


def subsets_backtrack_solution(l: list[int]):
    solution = []
    path = []

    def backtrack(index):
        if index == len(l):
            solution.append(path[:])

            return
        # make a decision: don't include current element in the path
        # we do nothing
        # explore that path
        backtrack(index + 1)
        # make a decision: include current element in the path
        path.append(l[index])
        # explore that path
        backtrack(index + 1)
        # undo the decision. This is the equivalent of going to the parent
        # we do this by popping the element we just added. this works because path is a global variable
        path.pop()

    backtrack(0)

    return solution

# print(sorted(subsets_backtrack_solution(l)))



# can we make this faster by hashing results?
# can there even be duplicates?
def combination_sum(candidates: list[int], target):
    solution = []
    path = []
    
    path_sum = 0

    def find_target(index):
        nonlocal path_sum
        remainder = target - path_sum
        if remainder == 0:
            solution.append(path[:])
            return
        
        
        for index in range(index, len(candidates)):
            # we're working with a sorted array
            # if adding the current element makes the sum too big, then all other larger elements will
            # also make the sum too large. Therefore, we end the loop early.
            if remainder < candidates[index]:
                return
            path.append(candidates[index])
            path_sum += candidates[index]
            find_target(index)
            path.pop()
            path_sum -= candidates[index]

    find_target(0)

    return solution

# ans = combination_sum([2, 3, 6, 7], 7)
# print(ans)

'''

base case:
if remainder is 0:
    found a solution
if remainder is negative:
    this isn't a solution
    go back

at each step:
either include the candidate and calculate the remainder
or move on to the next candidate

'''

# this solution is virtually the same as above, but uses a class to keep track of variables
# I wrote this before I knew about the nonlocal keyword
class combination_sum:
    def __init__(self, candidates: list[int], target):
        self.candidates = sorted(candidates)
        self.target = target
        self.solution = []
        self.path = []
        self.path_sum = 0
        self.find_target(0)


    def find_target(self, index):
        remainder = self.target - self.path_sum
        if remainder == 0:
            self.solution.append(self.path[:])
            return
        
        for index in range(index, len(self.candidates)):
            if remainder < self.candidates[index]:
                return
            self.path.append(self.candidates[index])
            self.path_sum += self.candidates[index]
            self.find_target(index)
            self.path.pop()
            self.path_sum -= self.candidates[index]

    def __str__(self):
        return str(self.solution)
    

def combination_sum_bottom_up(candidates, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # Base case

    for c in candidates:
        for t in range(c, target + 1):
            for comb in dp[t - c]:
                dp[t].append(comb + [c])

    return dp[target]


# print(combination_sum_bottom_up([2, 3, 6, 7], 7))
candidates = [2, 3, 6, 7]
def explore(target):
    if target == 0:
        return [[]]
    if target < 0:
        return []

    path = []
    for c in candidates:
        for remainder in explore(target - c):
            path.append(remainder + [c])
    return path
