def Binary_search(arr,target):
    low=0
    high=len(arr)-1

    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return f"Element found at index {mid} "
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return "Element not found "

arr=list(map(int,input("Enter sorted array elements separated by space ").split()))
target=int(input("Enter targeted value "))
print(Binary_search(arr,target))
