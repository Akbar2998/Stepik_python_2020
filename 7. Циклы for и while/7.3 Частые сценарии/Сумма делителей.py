a = int(input())
count = a
for i in range(1, (a//2)+1):
    if a%i == 0:
        count += i
print(count) 
