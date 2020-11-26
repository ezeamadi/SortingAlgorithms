import time

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

def quick_sort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 

        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high) 
  

# Driver program to test above function 

# numlist = [-5, -10, 0, 6, -3, 10, 8, 5, -1] 

fh = open('numbers.txt')
numlist = list()

for num in fh:
    numlist.append(int(num))

start_time = time.time()

n = len(numlist) 
quick_sort(numlist, 0, n-1) 

end_time = time.time()

arr =list()
for i in range(n):
    arr.append(numlist[i])

output_file = open("quick_sort_output.txt", "w")
output_file.write(str(arr));
output_file.close();

print(arr)

# total time taken
print(f"Runtime of the program is {end_time - start_time}")