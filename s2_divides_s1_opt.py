def splitting(s1,s2):
    sub_len=len(s2)
    i=0

    while(i<len(s1)):
        if(s1[i:i+sub_len]==s2):
            i+=sub_len
            continue
        else:
            return -1
        
    return True


if(__name__=="__main__"):
    s1="abab"
    s2="ab"
    print(splitting(s1,s2)) #O(N/M) Complexity 