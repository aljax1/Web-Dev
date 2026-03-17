n = int(input())
a = list(map(int, input().split()))

ok = False
for i in range(1, n):
    if a[i] * a[i-1] > 0:
        ok = True

print("YES" if ok else "NO")