def product(sub_l,k):
    c=1
    for i in sub_l:
        c=c*i
    if(c<k):
        return True
    else:
        return False

def sub_array(l,k):
    count=0
    for i in range(len(l)+1):
        for j in range(i):
            sub_l=l[j:i]
            if (product(sub_l,k)):
                count+=1
    return count

def easy(l,k):
    n=len(l)
    s=0
    e=0
    p=l[0]
    count=0
    while(s<n and e<n):
        if(p<k):
            e+=1
            if(e>=s):
                count+=e-s
            if(e<n):
                p*=l[e]
        else:
            p=int(p//l[s])
            s+=1
    return count


if __name__=="__main__":
    k=100
    l=[10,5,2,6] #Taken form Leet code for checking example

    print(sub_array(l,k)) #O(N^2) implementation
    print(easy(l,k)) #O(N) implementation
