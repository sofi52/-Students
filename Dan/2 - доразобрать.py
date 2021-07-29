

a=500000
f = 0
for i in range(a+1,a + 30):
    m = []
    sqrt = int(i**0.5)
    for k in range(2,sqrt+1): 
        if i%k==0 and k!= 8:
            if k%10==8:
                m.append(k)
            if (i//k)%10 == 8:
                m.append(i//k)
                
    if len(m)!=0:
        f+=1
        print(i)
        m.sort()
        print(m[0])
        if f == 5:
            break
                
    
    
