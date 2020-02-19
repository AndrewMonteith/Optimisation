from pulp import *

item_weights = [6, 7, 4, 9, 3, 8]
item_values = [60, 70, 40, 70, 16, 100]
n = len(item_weights)

# Choice Variables, 0 if we don't pick it. 1 if we do pick it.
xs = [LpVariable(f"x_{i}", lowBound=0, upBound=1, cat=LpInteger) for i in range(n)]  # Selection Variables
w = lpSum([item_weights[i]*xs[i] for i in range(n)])  # Total Weight Selected
overflow = LpVariable("overflow", lowBound=0, cat=LpInteger)

prob = LpProblem("Suitcase", LpMaximize)

# Objective Function
prob += lpSum([item_values[i]*xs[i] for i in range(n)]) - 15*overflow, "Total Cost In Suitcase"
prob += w <= 20+overflow, "overflow constraint"

prob.solve()

for i, v in enumerate(prob.variables()):
    if i > 5:
        continue

    message = "Pick Item" if v.varValue == 1 else "Don't Pick Item"

    print(message, chr(65+i))

print("Total Value:", value(prob.objective))
print("Total Weight:", value(w))




