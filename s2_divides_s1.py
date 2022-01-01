def splitting(s1,s2):
    req_length=len(s1)//len(s2)+1
    l=s1.split(s2)
    for i in l:
        if(i!=""):
            return -1
    return True
    
if(__name__=="__main__"):
    s1="abab"
    s2="ab"
    print(splitting(s1,s2))