import time

def count_sort(arr): 
    max_element = int(max(arr)) 
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    # Create a count array to store count of individual 
    # elements and initialize count array as 0 
    count_arr = [0 for _ in range(range_of_elements)] 
    output_arr = [0 for _ in range(len(arr))] 
  
    # Store count of each character 
    for i in range(0, len(arr)): 
        count_arr[arr[i]-min_element] += 1
  
    # Change count_arr[i] so that count_arr[i] now contains actual 
    # position of this element in output array 
    for i in range(1, len(count_arr)): 
        count_arr[i] += count_arr[i-1] 
  
    # Build the output character array 
    for i in range(len(arr)-1, -1, -1): 
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
        count_arr[arr[i] - min_element] -= 1
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(0, len(arr)): 
        arr[i] = output_arr[i] 
  
    return arr 


# Driver program to test above function 

# numlist = [-5, -10, 0, 6, -3, 10, 8, 5, -1] 

fh = open('numbers.txt')
numlist = list()

for num in fh:
    numlist.append(int(num))

start_time = time.time()

ans = count_sort(numlist) 
output_file = open("counting_sort_output.txt", "w")
output_file.write(str(ans));
output_file.close();

end_time = time.time()

print(ans)

# total time taken
print(f"Runtime of the program is {end_time - start_time}")