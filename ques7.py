def add():
    s=input("Enter numbers in list seprated with comma :")
    l=[int(e) for e in s.split(",")]
    return sum(l)

x=add()
print(x)
