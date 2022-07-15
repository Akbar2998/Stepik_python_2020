a = int(input())
x = 0
y = 1
print(1, end=" ")
for i in range(a):
    x,y = y, x+y
    print(x, end=" ")
