X, Y, A, B, C = map(int, input().split())
red = list(map(int,input().split()))
green = list(map(int,input().split()))
trans = list(map(int,input().split()))

red.sort(reverse=True)
green.sort(reverse=True)
trans.sort(reverse=True)
apple = red[:X] + green[:Y]
apple.sort()

j = 0
for i in range(X + Y):
    if apple[i] < trans[j]:
        apple[i] = trans[j]
        j = j + 1
        if j == C:
            break
    else:
        continue
print(sum(apple))