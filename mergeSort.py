import time

def merge_sort(arr):
    if len(arr) > 1:
 
        # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
 
        # Sorting each half
        merge_sort(L)
        merge_sort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 

# Driver program to test above function 

# numlist = [-5, -10, 0, 6, -3, 10, 8, 5, -1] 

fh = open('numbers.txt')
numlist = list()

for num in fh:
    numlist.append(int(num))

start_time = time.time()

merge_sort(numlist) 

end_time = time.time()
arr = list()
n = len(numlist)

for i in range(n):
    arr.append(numlist[i])

output_file = open("merge_sort_output.txt", "w")
output_file.write(str(arr));
output_file.close();

print(arr)

# total time taken
print(f"Runtime of the program is {end_time - start_time}")