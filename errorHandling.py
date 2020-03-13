x = 42 
y = 0
try:
    print(x/y)
except ZeroDivisionError as e:
    print("not allowed to divide by zero")
else:
    print("something else gone wrong")
finally:
    print("clean up code")
print(x/y)