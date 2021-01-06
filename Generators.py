def make_list(num):
    #result = []
    for i in range(num):
        #result.append(i*2)
        yield i*2
    #return result
#print(make_list(1000))
m = make_list(100)
next(m)
print(next(m))
next(m)
print(next(m))
##m = make_list(1) 
#se fizer mais de um 'next' vai ocorrer o erro "StopIteration" pois passou do limite