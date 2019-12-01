# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if (len(A) ==1 or len(A)==0 or K==0):
        return A
    else:
        a=A
        
        for j in range(0,K):
        
            list=[]
            l=len(a)
            c=a.pop(l-1)
            list.append(c)
            
            for i in range(0,l-1):
                list.append(a[i])
                
            a=list
            
        return(list)