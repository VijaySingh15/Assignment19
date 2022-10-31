def f1():
    a=int(input("Enter number :"))
    if a in range(20):
        return "Given number in range"
    else:
        return "Given number not in range"

x=f1()
print(x)