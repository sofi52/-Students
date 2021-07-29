#числа у которых ровно 3 нетривиальных делителя и их наибольший нетрив делитель
a=123456789
b=223456789

for i in range(a,b+1):
    current_sqrt=i**0.5
    massive=[]
    if current_sqrt==int(current_sqrt): # проверка что число является квадратным корнем
        current_sqrt=int(current_sqrt)
        count=0
       
        for k in range(2,current_sqrt): # не до квадратного корня
            if i%k==0:
                current=i//k
                massive.append(k)
                massive.append(current)
                 
        massive.append(current_sqrt) #добавляем квадратный корень
        if len(massive)==3:
            print(i)
            massive.sort()
            print(massive[2])
