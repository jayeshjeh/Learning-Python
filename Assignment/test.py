M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

J = {sum(row) for row in M}
print(J)

S = list(map(sum, M))
print(S)
