from pulp import *

item_weights = [6, 7, 4, 9, 3, 8]
item_values = [60, 70, 40, 70, 16, 100]
n = len(item_weights)

# Choice Variables, 0 if we don't pick it. 1 if we do pick it.
xs = [LpVariable(f"x_{i}", lowBound=0, upBound=1, cat=LpInteger) for i in range(n)]
w =  lpSum([item_weights[i]*xs[i] for i in range(n)])

prob = LpProblem("Suitcase", LpMaximize)

# Objective Function
prob += lpSum([item_values[i]*xs[i] for i in range(n)]), "Total Cost In Suitcase"

# Constraints
prob += w <= 20, "Weight Capacity of Suitcase"
prob += xs[3] >= xs[2], "C must only be taken with D"

prob.solve()

for i, v in enumerate(prob.variables()):
    message = "Pick Item" if v.varValue == 1 else "Don't Pick Item"

    print(message, chr(65+i))

print("Total Cost:", value(prob.objective))
print("Total Weight:", value(w))
