# print 1 to n using recursion

def print1ton(n):
    if n==1:
        print(1)
        return
    print1ton(n-1)
    print(n)

print1ton(5)