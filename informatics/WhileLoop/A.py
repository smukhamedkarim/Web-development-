import math

a = int(input())

i = 1

while i <= a:
    if int(math.sqrt(i)) == math.sqrt(i):
        print(i)
        i += 1
        continue
    i += 1

