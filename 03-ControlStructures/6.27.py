n_terms = 20
a, b = 0, 1
out = []

for _ in range(n_terms):
    out.append(str(a))
    a, b = b, a + b

print(" ".join(out))