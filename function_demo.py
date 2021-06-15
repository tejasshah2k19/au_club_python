
#no return -- no argument
def add():
    a = 10
    b = 20
    c = a+b
    print("add = ",c)

def sub(a,b):
    c = a-b
    print("sub = ",c)

def sqr():
    num = 9
    return num*num

def cube(num):
    return  num*num*num

def moreThanOneReturn():
    return 1,2,3,4,5


def mul(a,b):
    print(a)
    print(b)

def div(z,a=10,b=2):
    print("z : ",z)
    print("a : ",a)
    print("b : ",b)

def sum(*a):
    ans =0
    for i in a:
        ans = ans + i
    print("Total = ",ans)

add()
sub(60,50)
print("sqr = ",sqr())
ans = sqr()
print("sqr = ",ans)
ans = cube(3)
print(ans)
print(cube(5))
ans = moreThanOneReturn()
print(ans)
print(list(ans))

mul(10,20)
mul(b=20,a=200)
div(12)
div(12,23)
div(12,23,230)

sum(1,2,3)
sum(10,20)
sum(1,2,3,4,5)