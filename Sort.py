a=list(map(int,input().split()))

def bubble_sort(arr):
    n=len(arr)    
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            print(j)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                # print(a[j])
                swapped=True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n=len(arr)
    for i in range (n):
        min_idx=i
        for j in range(i+1,n,1):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
#ve tu lam lai insertion sort va merge sort
def insertion_sort(arr):
    n=len(arr)
        
    return arr
print(insertion_sort(a))