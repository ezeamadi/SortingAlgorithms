import time

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
def heap_sort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver program to test above function 

# numlist = [-5, -10, 0, 6, -3, 10, 8, 5, -1] 

fh = open('numbers.txt')
numlist = list()

for num in fh:
    numlist.append(int(num))

start_time = time.time()

heap_sort(numlist) 

end_time = time.time()
arr = list()
n = len(numlist)
for i in range(n):
    arr.append(numlist[i])

output_file = open("heap_sort_output.txt", "w")
output_file.write(str(arr))
output_file.close()

print(arr)

# total time taken
print(f"Runtime of the program is {end_time - start_time}")