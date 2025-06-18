import random

f= open("listTextFile.txt")



#print(f.read(25))
lenght=0
for x in f:
   lenght+=1
   #print(x)
print(lenght)

rndNumList=[]
rndWordList=[]
i=0
for i in range(7):
    r=random.randint(1,lenght)
    rndNumList.append(r)
    print(f.read(r))
    print(f.readline(r))
    getWord=f.readline(r)
    rndWordList.append(getWord)

print(rndNumList)
print(rndWordList)


    
    




#print(f.readline(r))
