def product():
    s=input("Enter numbers in list seprated with comma :")
    l=[int(e) for e in s.split(",")]
    result=1
    for i in l:
        result=result * i
    return result
    

x=product()
print(x)
