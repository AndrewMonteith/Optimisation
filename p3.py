from pulp import *

prob = LpProblem("Paintshop", LpMaximize)

# Variables for paint quantities used in mixing the other colours
pos_var = lambda name: LpVariable(name, lowBound=0)

Yr, Yg, Yk = pos_var("Yr"), pos_var("Yg"), pos_var("Yk")
Mr, Mb, Mk = pos_var("Mr"), pos_var("Mb"), pos_var("Mk")
Cg, Cb, Ck = pos_var("Cg"), pos_var("Cb"), pos_var("Sk")

# Variables for the total amount of paint made for R, G, B, K
R = (Yr + Mr)
G = (Yg + Cg)
B = (Mb + Cb)
K = (Ck + Mk + Yk)

# Objective Function
prob += 10*R + 15*G + 25*B + 25*K, "Total Cost from Paint"

# Constraints for quantities used in mixing
prob += Yr == Mr, "Preserve red quantities"
prob += Yg == Cg, "Preserve green quantities"
prob += Mb == Cb, "Preserve blue quantities"
prob += Ck == Mk, "Preserve black quantities (1)"
prob += Mk == Yk, "Preserve black quantities (2)"

# Constraints for capacities on total amount of paint
prob += Yr+Yg+Yk <= 11, "Total Amount of Yellow Paint"
prob += Mr+Mb+Mk <= 5, "Total amount of Magenta Paint"
prob += Cg+Cb+Ck <= 10, "Total amount of cyan paint"

prob.solve()

print("Total Cost Achieved:", value(prob.objective))
print("Total Amount of Red:", value(R))
print("Total Amount of Green:", value(G))
print("Total Amount of Blue:", value(B))
print("Total Amount of Black:", value(K))


print(value(Yk), value(Yg), value(Yr))
print(value(Mr), value(Mb), value(Mk))
print(value(Cg), value(Cb), value(Ck))

