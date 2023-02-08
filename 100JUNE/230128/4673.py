natural = set(range(1,10001))
t = set()
for i in range(10001) :
    j = sum(map(int, str(i))) + i
    t.add(j)
self_num = sorted(natural - t) 
for k in self_num :
    print(k)


        
