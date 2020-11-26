import time

def selection_sort(arr):

    for i in range(len(arr)): 
      
    # Find the minimum element in remaining unsorted array
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
              
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

# Driver Code
numlist = [-5, -10, 0, 6, -3, 10, 8, 5, -1] 

# fh = open('numbers.txt')
# numlist = list()

# for num in fh:
#     numlist.append(int(num))

start_time = time.time()
selection_sort(numlist) 
end_time = time.time()

arr = list();
for i in range(len(numlist)): 
    arr.append(numlist[i]) 

output_file = open("selection_sort_output.txt", "w")
output_file.write(str(arr));
output_file.close();

print(arr)

# total time taken
print(f"Runtime of the program is {end_time - start_time}")