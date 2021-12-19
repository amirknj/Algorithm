"""The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a
value, determine the number of each item to include in a collection so that the total weight is less than or equal to
a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who
is constrained by a fixed-size knapsack and must fill it with the most valuable items. The problem often arises in
resource allocation where the decision makers have to choose from a set of non-divisible projects or tasks under a
fixed budget or time constraint, respectively .
reference :https://en.wikipedia.org/wiki/Knapsack_problem"""


# A naive recursive implementation of 0-1 Knapsack Problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapsack(w, wt, val, i):
    # Base Case
    if i == 0 or w == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if wt[i - 1] > w:
        return knapsack(w, wt, val, i - 1)
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[i - 1] + knapsack(w - wt[i - 1], wt, val, i - 1), knapsack(w, wt, val, i - 1))


value = [60, 50, 70, 30]
weight = [5, 3, 4, 2]
W = 5
n = len(value)  # n = 4
print(knapsack(W, weight, value, n))


