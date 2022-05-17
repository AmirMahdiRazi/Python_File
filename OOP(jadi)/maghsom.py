li=[]
def adaval(number):
    global li
    lower = 1
    upper = int(number/2)
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                li+=[num]

num=[]
max=0
count=0
counter=[]
out=[]
for i in range(10):
    number=int(input())
    if number > max:
        max=number
    num+=[number]

adaval(max)
max=0
for i in range(10):
    count=0
    for j in range(len(li)):
        if num[i]%li[j]==0:
            count+=1
                
    counter+=[num[i],count]
max=0
for i in range(1,20,2):
    if counter[i] > max:
        max=counter[i]

for i in range(1,20,2):
    if counter[i]==max:
        out+=[counter[i-1]]
out.sort(reverse=True)
print(out[0],max)



