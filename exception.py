# try-catch-finally of division
try:
    a = int(input())
    b = int(input())
    c = a // b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("Division attempt complete.")
