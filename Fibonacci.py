def Fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + a
for f in Fibonacci(10):
    print (f)

#list
def Fibonacci2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + a
    return result
print(Fibonacci2(10))