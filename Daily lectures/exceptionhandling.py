try:
    n = 0
    res = 100/n
except ZeroDivisionError:
    print("You cannot divide by zero !")
else:
    print("Result is", res)
finally:
    print("execution complete")