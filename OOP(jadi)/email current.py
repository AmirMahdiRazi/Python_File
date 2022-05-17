alfa_low=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfa_up=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numb=['0','1','2','3','4','5','6','7','8','9']
part1,part2,part3=[],[],[]
str_1,str_2,str_3=[],[],[]
count=0
bpart1,bpart2,bpart3,b1,b2=True,True,True,True,True

while b1:
    Username=input()
    is_space = Username.find(" ")
    idx_ad = Username.find("@")
    idx_dot = Username.find(".")
    dis=idx_dot - idx_ad
    if (("@" not in Username or "." not in Username) or (Username.endswith(".") or Username.startswith("@")) or (is_space != -1 or dis == 1) ):
        bpart1=False
    else:
        count=0
        for i in range(idx_ad):
            if (Username[i] in alfa_low or Username[i] in alfa_up or Username[i] in numb):
                part1.append(Username[i])
                if Username[i] in numb:
                    count+=1
                if count==idx_ad:
                    bpart1=False
                    
                else:
                    bpart1=True
            else :
                bpart1=False
                break
        if bpart1:
            count=0
            for i in range(idx_ad+1,idx_dot):
                if (Username[i] in alfa_low or Username[i] in alfa_up or Username[i] in numb):
                    part2.append(Username[i])
                    if Username[i] in numb:
                        count+=1
                    if count==(idx_dot-idx_ad-1):
                       bpart2=False
                    else:
                        bpart2=True
                else :
                    bpart1=False
                    break
        if bpart1 and bpart2:
            count=0
            for i in range(idx_dot+1,len(Username)):
                if (Username[i] in alfa_low or Username[i] in alfa_up or Username[i] in numb):
                    part3.append(Username[i])
                    if Username[i] in numb:
                        count+=1
                    if count==(len(Username)-idx_dot-1):
                        bpart3=False
                    else:
                        bpart3=True

                else :
                    bpart1=False
                    break
    if bpart1 and bpart2 and bpart3:
        print("OK")
        b1=False
    else:
        print("WRONG")
        b1=False
