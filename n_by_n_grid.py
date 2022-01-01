def count(N):
    s=1
    for i in range(2,N+1):
        s=s+i**2

    return s
if __name__=="__main__":
    N=4
    print(count(N))