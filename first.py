print("Hello World")

def binarySearch(lst, target):
    lo = 0
    hi = len(lst)-1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if target == lst[mid] :
            return mid
        if target > lst[mid] :
            lo = mid+1
        else:
            hi = mid-1
    return -1

if __name__ == "__main__" :
    lst = [1,2,3,4,5,6,7,8,9,10]
    print(binarySearch(lst, 2))