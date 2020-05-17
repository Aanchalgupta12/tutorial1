#swap 2 variables without using a third variable
a=int(input("enter valueof a:"))
b=int(input("enter value of b:"))
a=a+b
b=a-b
a=a-b
print("a:",a)
print("b:",b)