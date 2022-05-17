
import copy
import os
#from typing import MutableMapping
#-----------------------------Import--------------------------------------#

endofgame=True
map=[]
#---------------------------Global value-----------------------------------#
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def checkend_without_choise(map):
    empty_squ=False
    for i in range(5,-1,-1):
        for j in range(7):
            #zarbR
            if(i-3<=0 and j+3<=6):
                for k in range(1,4):
                    if(map[i-k][j+k]=='-'):
                        continue
                    if(map[i-k][j+k]==map[i-k+1][j+k-1] or map[i-k+1][j+k-1]=='-'):
                        empty_squ=True
                        continue
                    else:
                        empty_squ=False
                        break
            if (i-3>=0):
                for k in range(1,4):
                    if(map[i-k][j]=='-'):
                        continue
                    if(map[i-k][j]==map[i-k+1][j] or map[i-k+1][j]=='-'):
                        empty_squ=True
                        continue
                    else:
                        empty_squ=False
                        break
            if(j+3<=6):
                for k in range(1,4):
                    if(map[i][j+k]=='-'):
                        continue
                    if(map[i][j+k]==map[i][j+k-1] or map[i][j+k-1]=='-'):
                        empty_squ=True
                        continue
                    else:
                        empty_squ=False
                        break
    return empty_squ
def checkend(map):
    #satri
    endofgame=True
    win=0
    for i in range(6):
        for j in range(4):
            if map[i][j]==map[i][j+1] and map[i][j+1]==map[i][j+2] and map[i][j+2]==map[i][j+3] and map[i][j]!='-'  :
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
    #sotoni
    for  j in range(7):
        for i in range(3):
            if map[i][j]==map[i+1][j] and map[i+1][j]==map[i+2][j] and map[i+2][j]==map[i+3][j] and map[i][j]!='-' :
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
    #zarbdariR
    if (map[3][0]==map[2][1] and map[2][1]==map[1][2] and map[1][2]==map[0][3] and map[3][0]!='-'):
        if (map[3][0]=='X'):
            win=1
            endofgame=False
            return endofgame,win
        else:
            win=-1
            endofgame=False
            return endofgame,win
    elif (map[5][3]==map[4][4] and map[4][4]==map[3][5] and map[3][5]==map[2][6] and map[5][3]!='-'):
        if (map[5][3]=='X'):
            win=1
            endofgame=False
            return endofgame,win
        else:
            win=-1
            endofgame=False
            return endofgame,win
    i=4
    j=0
    while(j<2):
        while(i>=3):
            if (map[i][j]==map[i-1][j+1] and map[i-1][j+1]==map[i-2][j+2] and map[i-2][j+2]==map[i-3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            
            i-=1
            j+=1
    i=5
    j=0
    while(j<3):
        while(i>2):
            if (map[i][j]==map[i-1][j+1] and map[i-1][j+1]==map[i-2][j+2] and map[i-2][j+2]==map[i-3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            i-=1
            j+=1 
    i=5
    j=1
    while(j<4):
        while(i>2):
            if (map[i][j]==map[i-1][j+1] and map[i-1][j+1]==map[i-2][j+2] and map[i-2][j+2]==map[i-3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            i-=1
            j+=1            
    i=5
    j=2
    while(j<4):
        while(i>3):
            if (map[i][j]==map[i-1][j+1] and map[i-1][j+1]==map[i-2][j+2] and map[i-2][j+2]==map[i-3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1 
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            i-=1
            j+=1 
    #zarbdariL
    if (map[2][0]==map[3][1] and map[3][1]==map[4][2] and map[4][2]==map[5][3] and map[2][0]!='-'):
        if (map[3][0]=='X'):
            win=1
            endofgame=False
            return endofgame,win
        else:
            win=-1
            endofgame=False
            return endofgame,win
    

    elif (map[0][3]==map[1][4] and map[1][4]==map[2][5] and map[2][5]==map[3][6] and map[0][3]!='-'):
        if (map[0][1]=='X'):
            win=1
            endofgame=False
            return endofgame,win
        else:
            win=-1
            endofgame=False
            return endofgame,win
    i=1
    j=0
    while(j<2):
        while(i<3):
            if (map[i][j]==map[i+1][j+1] and map[i+1][j+1]==map[i+2][j+2] and map[i+2][j+2]==map[i+3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            i+=1
            j+=1
    i=0
    j=0
    while(j<3):
        while(i<3):
            if (map[i][j]==map[i+1][j+1] and map[i+1][j+1]==map[i+2][j+2] and map[i+2][j+2]==map[i+3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            i+=1
            j+=1

    i=0
    j=1
    while(j<4):
        while(i<3):
            if (map[i][j]==map[i+1][j+1] and map[i+1][j+1]==map[i+2][j+2] and map[i+2][j+2]==map[i+3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            i+=1
            j+=1
        
    i=0
    j=2
    while(j<4):
        while(i<2):
            if (map[i][j]==map[i+1][j+1] and map[i+1][j+1]==map[i+2][j+2] and map[i+2][j+2]==map[i+3][j+3] and map[i][j]!='-'): 
                if (map[i][j]=='X'):
                    win=1
                    endofgame=False
                    return endofgame,win
                else:
                    win=-1
                    endofgame=False
                    return endofgame,win
            i+=1
            j+=1
    return endofgame,win
def start():
    global map
    for i in range(6):
        temp=['-','-','-','-','-','-','-']
        map+=[temp]
    return map
def choise(player,column):
    global map,endofgame
    for i in range(5,-1,-1):
        if map[i][column]=='-':
            if player==1:
                map[i][column]='X'
                return
            else:
                map[i][column]='O'
                return
        else:
            continue
def choiseCOM(player,column,map):
    can_choise=False
    for i in range(5,-1,-1):
        if map[i][column]=='-':
            if player==1:
                map[i][column]='X'
                can_choise=True
                break
            else:
                map[i][column]='O'
                can_choise=True
                break
        else:
            continue
    return can_choise,map
def showmap():
    global map
    for i in range(0,7):
        print(i,end=" ")
    print()
    for i in range(6):
        for j in range(7):
            print(map[i][j],end=" ")
        print()
def selectCOM(map):
    global listCOM
    for i in range(7):
        mapCOM1 = copy.deepcopy(map)
        out_choise1= choiseCOM(1,i,mapCOM1)
        count1=0
        if out_choise1[0]:
            count1+=1
            mapCOM1=out_choise1[1] 
            temp = COM(mapCOM1)
            listCOM += [temp]
            temp.leaf()
            count2=0
            #---------------------------------------------------First step-------------------------------------------#
            if temp.return_leaf():
                for j in range(7):
                    mapCOM2 = copy.deepcopy(mapCOM1)
                    out_choise2= choiseCOM(2,j,mapCOM2)
                    if out_choise2[0]:
                        
                        count2+=1
                        mapCOM2 = out_choise2[1]
                        
                        temp=COM(mapCOM2)
                        listCOM += [temp]
                        temp.leaf()
                        count3=0
                        #----------------------------------------Second step-----------------------------------------#
                        if temp.return_leaf():
                            for k in range(7):
                                mapCOM3 = copy.deepcopy(mapCOM2)
                                out_choise3 = choiseCOM(1,k,mapCOM3)
                                
                                if out_choise3[0]:
                                    count3+=1
                                    
                                    mapCOM3=out_choise3[1]
                                    temp=COM(mapCOM3)
                                    listCOM +=[temp]
                                    temp.leaf()
                                    #-----------------------------------------------End step-----------------------------#
                                    if temp.return_leaf():
                                        temp.cal()
                                    else:
                                        if temp.return_win() == 1:
                                            temp.increse_Value()
                                else:
                                    continue    
                        else:
                            if temp.return_win() == -1:
                                listCOM.pop()
                                count2-=1
                                continue
                        MAX=-10 
                        while(count3>=1):
                            count3-=1
                            x=listCOM.pop()
                            if MAX <= x.return_Value():
                                MAX = x.return_Value()    
                        len_listCOM=len(listCOM)-1
                        listCOM[len_listCOM].set_Value(MAX)

                        #set_MAX
                        #------------------------------------------------------End First step------------------------------------#
                    else:
                        continue
            else:
                if temp.return_win()==1 :
                    return i  
                            
        else:
            continue
        MIN=+10
        find=0    
        while(count2>=1):
            count2-=1
            x=listCOM.pop()
            if MIN >= x.return_Value():
                MIN = x.return_Value()        
        len_listCOM=len(listCOM)-1
        listCOM[len_listCOM].set_Value(MIN)
        #set_MIN
    
    len_listCOM = len(listCOM) -1
    MAX=-10
    for i in range(len_listCOM - 1):
        x=listCOM.pop()
        if MAX < x.return_Value():
            MAX = x.return_Value()
            find = x.return_map()
    #set_MAX
    return find_select(map,find)             
def find_select(map1,map2):
    for i in range(5,-1,-1):
        for j in range(6,-1,-1):
            if(map1[i][j] != map2[i][j]):
                return j                            
def showmap(map):
    for i in range(0,7):
        print(i,end=" ")
    print()
    for i in range(6):
        for j in range(7):
            print(map[i][j],end=" ")
        print()
map=start()
#------------------------------------end of Function-----------------------------------------#
class COM:
    Value=0
    status=[]
    leaf=False
    win=0
    def cal(self):
        choisedCOM=[]
        choisedP1=[]
        map=self.map
        for i in range(5,-1,-1):
            for j in range(7):
                if map[i][j]=='X':
                    choisedCOM+=[[i,j]]
        #find selected COM
        for i in range(5,-1,-1):
            for j in range(7):
                if map[i][j]=='O':
                    choisedP1+=[[i,j]]
        #find selected Player1
        length=0
        cost=0
        count=0
        #print(choisedCOM)
        #--------------------------------------COM------------------------------------------#
        while(length<len(choisedCOM)):
            Row=choisedCOM[length][0]
            column=choisedCOM[length][1]
            #SOTON O
            if (Row + 3 <= 5):
                if (map[Row+1][column]=='O' and map[Row+1][column]==map[Row+2][column] and map[Row+2][column]==map[Row+3][column]):
                    cost+=10
            #SATR
            if (column - 3 >= 0 or column + 3 <= 6):
                if column - 3 >= 0:
                    if (map[Row][column-1]=='O' and map[Row][column-1]==map[Row][column-2] and map[Row][column-2]==map[Row][column-3]):
                        cost+=10
                else:
                    if (map[Row][column+1]=='O' and map[Row][column+1]==map[Row][column+2] and map[Row][column+2]==map[Row][column+3]):
                        cost+=10
            #zarbRL O
            if((Row + 3 <= 5 and column + 3 <= 6) or (Row - 3 >= 0 and column - 3 >= 0) or (Row - 3 >= 0 and column + 3 <= 6) or (Row + 3 <= 5 and column - 3 >= 0)):
                if(Row + 3 <= 5 and column + 3 <= 6):
                    if (map[Row + 1][column + 1]=='O' and map[Row + 1][column + 1]==map[Row + 2][column + 2] and map[Row + 2][column + 2]==map[Row + 3][column + 3]):
                        cost+=10
                if(Row - 3 >= 0 and column - 3 >= 0):
                    if (map[Row - 1][column - 1]=='O' and map[Row - 1][column - 1]==map[Row - 2][column - 2] and map[Row - 2][column - 2]==map[Row - 3][column - 3]):
                        cost+=10
                if(Row + 3 <= 5 and column - 3 >= 0):
                    if (map[Row + 1][column - 1]=='O' and map[Row + 1][column - 1]==map[Row + 2][column - 2] and map[Row + 2][column - 2]==map[Row + 3][column - 3]):
                        cost+=10
                if(Row - 3 >= 0 and column + 3 <= 6):
                    if (map[Row - 1][column + 1]=='O' and map[Row - 1][column + 1]==map[Row - 2][column + 2] and map[Row - 2][column + 2]==map[Row - 3][column + 3]):
                        cost+=10
            #soton    
            if Row-3>=0:
                for i in range(1,4):
                    if (map[Row-i][column]=='-' or map[Row-i][column]=='X'):
                        if (map[Row-i][column]=='X'):
                            count+=0.25
                        else:
                            count+=0.01
                    else:
                        count=0
                        break
            if(count >=0.50):
                count+=2
            cost+=count
            count=0   
            #satr
            if column+3<=6 or column-3>=0:
                if column+3<=6:
                    for i in range(1,4):
                        if(map[Row][column+i]=='-' or map[Row][column+i]=='X'):
                            if map[Row][column+i]=='X':
                                count+=0.25
                            else:
                                count+=0.01
                        else:
                            count=0
                            break
                
                if(count >=0.50):
                    count+=2
                cost+=count
                count=0
                if (column-3>=0):
                    for i in range(1,4):
                        if(map[Row][column-i]=='-' or map[Row][column-i]=='X'):
                            if map[Row][column-i]=='X':
                                count+=0.25
                            else:
                                count+=0.01
                        else:
                            count=0
                            break
            if(count >=0.50):
                count+=2
            cost+=count
            count=0
            #zarbR
            if (Row-3>=0 and column+3<=6) or (Row+3>=5 and column+3<=6):
                if (Row-3>=0 and column+3<=6):
                    for i in range(1,4):
                        if (map[Row-i][column+i]=='-' or map[Row-i][column+i]=='X'):
                            if map[Row-i][column+i]=='X':
                                count+=0.25
                            else:
                                count+=0.01
                        else:
                            count=0
                            break
                if (Row+3<=5 and column+3<=6):
                    for i in range(1,4):
                        if (map[Row+i][column+i]=='-' or map[Row+i][column+i]=='X'):
                            if map[Row+i][column+i]=='X':
                                count+=0.25
                            else:
                                count+=0.01
                        else:
                            count=0
                            break
            if(count >=0.50):
                count+=2
            cost+=count
            count=0
            #zarbL    
            if (Row-3>=0 and column-3>=0) or (Row+3>=5 and column-3<=0):
                if (Row-3>=0 and column-3>=0):
                    for i in range(1,4):
                        if (map[Row-i][column-i]=='-' or map[Row-i][column-i]=='X'):
                            if map[Row-i][column-i]=='X':
                                count+=0.25
                            else:
                                count+=0.01
                        else:
                            count=0
                            break
                if (Row+3<=5 and column-3<=0):
                    for i in range(1,4):
                        if (map[Row+i][column-i]=='-' or map[Row+i][column-i]=='X'):
                            if map[Row+i][column-i]=='X':
                                count+=0.25
                            else:
                                count+=0.01
                        else:
                            count=0
                            break
            
            if(count >=0.50):
                count+=2
            cost+=count
            count=0
            length+=1
        #----------------------------Player1--------------------------------------------#
        length=0
        count=0
        
        while(length<len(choisedP1)):
            #soton    
            Row=choisedP1[length][0]
            column=choisedP1[length][1]
            if Row-3>=0:
                for i in range(1,4):
                    if (map[Row-i][column]=='-' or map[Row-i][column]=='O'):
                        if (map[Row-i][column]=='O'):
                            count-=0.25
                        else:
                            count-=0.01
                    else:
                        count=0
                        break
            if(count <=-0.50):
                count-=2
            
            cost+=count 
            count=0   
            #satr
            if column+3<=6 or column-3>=0:
                if column+3<=6:
                    for i in range(1,4):
                        if(map[Row][column+i]=='-' or map[Row][column+i]=='O'):
                            if map[Row][column+i]=='O':
                                count-=0.25
                            else:
                                count-=0.01
                        else:
                            count=0
                            break
                
                if(count <=-0.50):
                    count-=2
                cost+=count
                count=0
                if column-3>=0:
                    for i in range(1,4):
                        if(map[Row][column-i]=='-' or map[Row][column-i]=='O'):
                            if map[Row][column-i]=='O':
                                count-=0.25
                            else:
                                count-=0.01
                        else:
                            count=0
                            break        
            if(count <=-0.50):
                count-=2
            cost+=count
            count=0
            #zarbR
            if (Row-3>=0 and column+3<=6) or (Row+3>=5 and column+3<=6):
                if (Row-3>=0 and column+3<=6):
                    for i in range(1,4):
                        if (map[Row-i][column+i]=='-' or map[Row-i][column+i]=='O'):
                            if map[Row-i][column+i]=='O':
                                count-=0.25
                            else:
                                count-=0.01
                        else:
                            count=0
                            break
                if (Row+3<=5 and column+3<=6):
                    for i in range(1,4):
                        if (map[Row+i][column+i]=='-' or map[Row+i][column+i]=='O'):
                            if map[Row+i][column+i]=='O':
                                count-=0.25
                            else:
                                count-=0.01
                        else:
                            count=0
                            break
            if(count <=-0.50):
                count-=2
            cost+=count
            count=0
            #zarbL    
            if (Row-3>=0 and column-3>=0) or (Row+3>=5 and column-3<=0):
                if (Row-3>=0 and column-3>=0):
                    for i in range(1,4):
                        if (map[Row-i][column-i]=='-' or map[Row-i][column-i]=='O'):
                            if map[Row-i][column-i]=='O':
                                count-=0.25
                            else:
                                count-=0.01
                        else:
                            count=0
                            break    
                if (Row+3<=5 and column-3<=0):
                    for i in range(1,4):
                        if (map[Row+i][column-i]=='-' or map[Row+i][column-i]=='O'):
                            if map[Row+i][column-i]=='O':
                                count-=0.25
                            else:
                                count-=0.01
                        else:
                            count=0
                            break
                
            if(count <=-0.50):
                count-=2
            cost+=count
            count=0
            length+=1
        self.Value=cost
    def __init__(self,map):
        self.map = map
    def set_status(self,status):
        self.status+=[status]
    def leaf(self):
        out=checkend(self.map)
        self.leaf=out[0]
        self.win=out[1]
    def return_leaf(self):
        return self.leaf
    def return_win(self):
        return self.win
    def return_map(self):
        return self.map
    def increse_Value(self):
        self.Value+=100
    def return_Value(self):
        return self.Value
    def set_Value(self,num):
        self.Value=num
#-----------------------------------end of Class------------------------------------------#
listCOM=[]
cls()
input1=int(input())
if input1==1:
    map[5][1],map[5][2],map[4][2],map[3][2],map[2][2],map[1][2],map[5][3],map[4][3],map[3][3],map[2][3],map[1][3]='X','O','O','O','X','O','O','X','O','X','X'
    map[5][4],map[4][4],map[3][4],map[2][4],map[5][5],map[4][5],map[3][5],map[2][5],map[5][6]='O','O','X','X','X','O','X','O','O'
    showmap(map)
    print()
    num=selectCOM(map)
    choise(1,num)
    showmap(map)
    out=checkend(map)
    if out[0]==False:
        if out[1]==1:
            print("Win COM")
        else:
            print("Win Player")   
if input1==2:
    map[5][1],map[5][2],map[4][2],map[3][2],map[2][2],map[1][2],map[5][3],map[4][3],map[3][3],map[2][3],map[1][3]='O','X','X','X','O','X','X','O','X','O','O'
    map[5][4],map[4][4],map[3][4],map[2][4],map[5][5],map[4][5],map[3][5],map[2][5],map[5][6]='X','X','O','O','O','X','O','X','X'
    num=selectCOM(map)
    showmap(map)
    print()
    choise(1,num)
    showmap(map)
    print()
    choise(2,2)
    showmap(map)
    print()
    out=checkend(map)
    if out[0]==False:
        if out[1]==1:
            print("Win COM")
        else:
            print("Win Player")
if input1==3:
    map[5][4],map[4][4],map[3][4]='O','O','O'
    showmap(map)
    num=selectCOM(map)
    choise(1,num)
    showmap(map)
if input1==4:
    endofgame=True
    while(endofgame):
        num=selectCOM(map)
        choise(1,num)
        out=checkend(map)
        if out[0]==False:
            if out[1]==1:
                cls()
                print("Win COM")
                showmap(map)
                break
        cls()
        showmap(map)
        PL=int(input('Choise : '))
        choise(2,PL)
        out=checkend(map)
        if out[0]==False:
            if out[1]==-1:
                cls()
                print("Win PLayer")
                showmap(map)
                break
        













