# sign(x) = 1,   если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0,   если x = 0.

a = int(input())
if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)