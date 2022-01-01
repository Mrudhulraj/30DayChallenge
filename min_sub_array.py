def min_sub_array(l,k):
    s=0
    e=0
    n=len(l)
    sum_arr=l[0]
    best=0
    count=10**9
    while(s<n and e<n):
        if(sum_arr<k):
            e+=1
            if(e<n):
                sum_arr+=l[e]
        else:
            if((e-s+1)<count):
                count=e-s+1
            sum_arr-=l[s]
            s+=1
    if(count==10**9):
        return 0
    return count

if(__name__=="__main__"):
    l=[2,3,1,2,4,3]
    k=7
    print(min_sub_array(l,k))