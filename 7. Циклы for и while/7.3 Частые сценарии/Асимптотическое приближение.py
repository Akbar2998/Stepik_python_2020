import math
a = int(input())
count = 0
for i in range(1,a+1):
    count += (1/i)
print(count - math.log(a)) 
