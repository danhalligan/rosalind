n = 80
m = 18

v = [1] + (m - 1) * [0]
for i in range(2, n + 1):
    v = [sum(v[1:])] + v[:-1]

print(sum(v))
