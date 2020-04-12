K, N = map(int, input().split())
A = list(map(int, input().split()))

maxA = 0
distSum = 0
for i in range(N):
    if i < N -1:
        dist = A[i+1] - A[i]
    else:
        dist = A[0] + K - A[N-1]
    if maxA < dist:
        maxA = dist
    distSum = distSum + dist 

distSum = distSum - maxA
print(distSum)
    