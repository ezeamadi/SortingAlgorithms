import time

def insertion_sort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  

# Driver program to test above function 

# numlist = [-5, -10, 0, 6, -3, 10, 8, 5, -1] 

fh = open('numbers.txt')
numlist = list()

for num in fh:
    numlist.append(int(num))

start_time = time.time()
insertion_sort(numlist) 
end_time = time.time()

arr = list();
for i in range(len(numlist)): 
    arr.append(numlist[i]) 

output_file = open("insertion_sort_output.txt", "w")
output_file.write(str(arr));
output_file.close();

print(arr)

# total time taken
print(f"Runtime of the program is {end_time - start_time}")