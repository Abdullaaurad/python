def Valleys(steps,path):
    ValleysI=0
    height=0
    for i in range(steps):
        if(path[i]=='D'):
            height-=1
        else:
            height+=1
        if(height==0):
            ValleysI+=1

    return ValleysI

