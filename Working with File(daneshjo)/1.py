f = open ('E:\Python\Working with File(daneshjo)\\text.txt', 'w')
li=[]
# count =[10,1,100,10,1000,100]
# for _ in range(0,6,2):
#     for i in range(0,count[_],count[_+1]):
#         li.append(f'\'{i}\'\n')
 
for _ in range(1,21):
    li.append(f'\'{_}\',\n')
        
f.writelines(li)
f.close()

