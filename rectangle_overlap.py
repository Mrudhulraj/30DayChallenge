def overlap(l1,r1,l2,r2):
    if(l1[0]>=r2[0] or l2[0]>=r1[0]):
        return False
    
    if(r1[1]>=l2[1] or r2[1]>=l1[1]):
        return False
    
    return True
    
if(__name__=="__main__"):
    l1 = [0, 10]
    r1 = [10, 0]
    l2 = [5, 5]
    r2 = [15, 0]
    print(overlap(l1,r1,l2,r2))