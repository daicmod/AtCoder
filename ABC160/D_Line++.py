N, X, Y = map(int, input().split())

l = [0] * (N)

graph = [[0] * N] * N

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if i < X:
            distAX = X - i
        else:
            distAX = i - X            
        if j < Y:
            distBY = Y - j
        else:
            distBY = j -Y
        distAB = j - i
        if distAX + distBY + 1 < distAB:
            distAB = distAX + distBY + 1

        l[distAB] = l[distAB] + 1

for i in range(1, N):
    print(l[i])