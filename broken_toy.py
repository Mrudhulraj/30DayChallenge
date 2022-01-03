def pos(n,m,k):
    
    if(m<=n-k+1):
        return m+k-1 #-1 since we are including kth position
    
    rem=m//n 
    m=m-(rem*n+1)
    
    return m+k

if(__name__=="__main__"):
    n=5 #circle size
    m=8 #Number of items to be dist
    k=2 #starting position
    print(pos(n,m,k))