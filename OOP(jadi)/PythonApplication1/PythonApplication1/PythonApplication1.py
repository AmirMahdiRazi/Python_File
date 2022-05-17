num=[[1,2,3],[4,5,6],[7,8,9]]
print("player1 : X ","\nplayer2 : S ")
num1=0
num2=0
while(1):
    num1+=1
    for x in range(0,3):
        print ("   ",num[x][0],"  ",num[x][1],"  ",num[x][2])
    num_player1=[]
    num_player2=[]
    num_player1=int(input("player1 Choose:"))
    for x in range(0,3):
        for y in range(0,3):    
            if num[x][y]==num_player1:
                num[x][y]="X"
     
    for x in range(0,3):
        print ("   ",num[x][0],"  ",num[x][1],"  ",num[x][2])

    

    if num1>=3:
    #zarbdari
        if num[0][0]==num[1][1] and num[1][1]==num[2][0]:
            if num[0][0]=="X":
                print("player1 Win")
                num3=input("Do you Countinue ?(y/n): ")
                if num3=='y':
                     num=[[1,2,3],[4,5,6],[7,8,9]]
                else :
                     break
            else:
                print("player 2 Win")
                num3=input("Do you Countinue ?(y/n): ")
                if num3=='y':
                     num=[[1,2,3],[4,5,6],[7,8,9]]
                else :
                     break
            
        elif num[0][2]==num[1][1] and num[1][1]==num[2][0]:
            if num[0][0]=="X":
                print("player1 Win")
                num3=input("Do you Countinue ?(y/n): ")
                if num3=='y':
                     num=[[1,2,3],[4,5,6],[7,8,9]]
                else :
                    break
            else:
                print("player 2 Win")
                break
    #satri           
        for x in range(0,3):
            if num[x][0]==num[x][1] and num[x][1]==num[x][2]:
                if num[x][0]=="X":
                    print("player1 Win")
                    num2+=1
                    
                    num3=input("Do you Countinue ?(y/n): ")
                    if num3=='y':
                         num=[[1,2,3],[4,5,6],[7,8,9]]
                    else :
                         break
                else:
                    print("player 2 Win")
                    num2+=1
                    num3=input("Do you Countinue ?(y/n): ")
                    if num3=='y':
                         num=[[1,2,3],[4,5,6],[7,8,9]]
                    else :
                         break
    #sotoni
        for y in range(0,3):
            if num[0][y]==num[1][y] and num[1][y]==num[2][y]:
                if num[0][y]=="X":
                    print("player1 Win")
                    num2+=1
                    num3=input("Do you Countinue ?(y/n): ")
                    if num3=='y':
                         num=[[1,2,3],[4,5,6],[7,8,9]]
                    else :
                         break
                else:
                    print("player 2 Win")
                    num2+=1
                    num3=input("Do you Countinue ?(y/n): ")
                    if num3=='y':
                         num=[[1,2,3],[4,5,6],[7,8,9]]
                    else :
                         break
        if num2==1:
            num3=input("Do you Countinue ?(y/n): ")
            if num3=='y':
                 num=[[1,2,3],[4,5,6],[7,8,9]]
            else :
                break

    num_player2=int(input("player2 Choose:"))
    for x in range(0,3):
        for y in range(0,3):    
            if num[x][y]==num_player2:
                num[x][y]="S"

    if num1>=3:
    #zarbdari
        if num[0][0]==num[1][1] and num[1][1]==num[2][0]:
            if num[0][0]=="X":
                print("player1 Win")
                num3=input("Do you Countinue ?(y/n): ")
                if num3=='y':
                     num=[[1,2,3],[4,5,6],[7,8,9]]
                else :
                    break
            else:
                print("player 2 Win")
                num3=input("Do you Countinue ?(y/n): ")
                if num3=='y':
                     num=[[1,2,3],[4,5,6],[7,8,9]]
                else :
                    break
            
        elif num[0][2]==num[1][1] and num[1][1]==num[2][0]:
            if num[0][0]=="X":
                print("player1 Win")
                num3=input("Do you Countinue ?(y/n): ")
                if num3=='y':
                     num=[[1,2,3],[4,5,6],[7,8,9]]
                else :
                    break
                break
            else:
                print("player 2 Win")
                num3=input("Do you Countinue ?(y/n): ")
                if num3=='y':
                     num=[[1,2,3],[4,5,6],[7,8,9]]
                else :
                    break
    #satri           
        for x in range(0,3):
            if num[x][0]==num[x][1] and num[x][1]==num[x][2]:
                if num[x][0]=="X":
                    print("player1 Win")
                    num2+=1
                    break
                else:
                    print("player 2 Win")
                    num2+=1
                    break
    #sotoni
        for y in range(0,3):
            if num[0][y]==num[1][y] and num[1][y]==num[2][y]:
                if num[0][y]=="X":
                    print("player1 Win")
                    break
                else:
                    print("player 2 Win")
                    num2+=1
                    break

        if num2==1:
            num3=input("Do you Countinue ?(y/n): ")
            if num3=='y':
                 num=[[1,2,3],[4,5,6],[7,8,9]]
                 num1=0
            else :
                break
        if num1>=4:
            num=[[1,2,3],[4,5,6],[7,8,9]]
            num1=0