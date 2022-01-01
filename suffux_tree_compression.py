def encode(s):
    final_s=""
    i=0
    j=1
    c=1
    while(j <len(s)): 
        if(s[j]==s[i]):
            c+=1
            i+=1
            j+=1
        else:
            final_s+=s[i]+str(c)
            c=1
            i+=1
            j+=1
    final_s+=s[i]+str(c)       
    return final_s
    
if(__name__=="__main__"):
    s= "wwwwaaadexxxxxx"
    print(encode(s)) #O(N) implementation
