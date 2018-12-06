arr = [2,4,6,3,34,56,354,78]
arr.sort()

def binS(arr,l,h,x):
    while(l<=h):
        m = l + int((h-l)/2)
        if arr[m] == x:
            return m
        elif arr[m]<x:
            return binS(arr,m+1,h,x)
        else:
            return binS(arr,l,m-1,x)
    
    return -1
    


print(binS(arr,0,len(arr)-1,4))
