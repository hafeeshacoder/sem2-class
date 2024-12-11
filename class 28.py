'''length=int(input("Enther the  length  of rectangle:"))
breath=int(input("Enter the breath of rectongle:"))
area=length*breath
print(f"The area of rectangle{area}")
s=int(input("Enter the value:"))
S=s*s
print(f"The area of square{S}")
h=int(input("Enther the hight of the triangle:"))
b=int(input("Enther the breath of the the triangle:"))
t=(1/2*(h*b))
print(f"The area of Triangle{t}")
c=int(input("Enter the radius of the circle"))
C=(3.14)*(c^2)
print(f"The are of circle{C}")
'''
n=int(input())
n1=0
n2=1
count=0
if n<=0:
    print("Enter the positive number")
elif n==1:
    print(n1)
else:
    while count<n:
        print(n1,end="")
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
