# reverse an array
a=[1,2,3,4,5]
a.reverse()
print(a)

# another way to reverse an array
a=[1,2,3,4,5]
n=len(a)
for i in range(n//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]
print(a)

# another way to reverse an array using slicing
a=[1,2,3,4,5]
a=a[::-1]

# check if array is sorted or not
a=[1,2,3,4,5]
is_sorted=True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        is_sorted=False
        break
print(is_sorted)

# another way to check if array is sorted or not
a=[1,2,3,4,5]
print(a==sorted(a))

















