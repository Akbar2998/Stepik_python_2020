a = int(input())
largest = 2
previous_largest = 2
for i in range(a):
    num = int(input())
    if num > largest:
        previous_largest = largest
        largest = num
    elif num > previous_largest:
        previous_largest = num
print(largest)  
print(previous_largest)
    


