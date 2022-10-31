def f1(*l):
    return list(l)

s=input("Enter items of list seprated with comma :")
n=[int(e) for e in s.split(',')]
x=f1(n)
print(x)

