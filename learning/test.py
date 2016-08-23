L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

S = sorted(L, key=lambda x: x[1])
print(S)

M = {'A': 3, 'B': 2}
SM = sorted(M.items(), key=lambda x: x[1])
print(SM)
