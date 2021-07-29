a=2000000
b=3000000


for i in range(a,b+1):
    current_sqrt=i**0.5
    current_sqrt=int(current_sqrt)
    
    count=0
    for k in range(200,current_sqrt+1): #почему от 2?
        if i%k==0:
            
           if (i//k)-k<=115:
                count+=1
                
    if count>2: #почему 2?
        print(i)
