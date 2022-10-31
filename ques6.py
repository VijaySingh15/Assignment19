def f1():
    print("Enter four numbers :")
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    l1=[a,b,c,d]
    return max(l1)

x=f1()
print("Maximum number in all numbers :",x)
