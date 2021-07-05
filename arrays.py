import array

# create an array
arr=array.array('i', [1,2,3])

#print an array
print("The created array has values: ", end=" ")
for i in range(0,3):
    print(arr[i], end=" ")

print("\r")

# append an element to the array
arr.append(5);
print("The appended array is:", end=" ")
for i in range(0,4):
    print(arr[i], end=" ")
print("\r")
# make use of insert() function to insert value at specified position
arr.insert(2,5)
print("Updated array is:" , end=" ")
for i in range(0,5):
    print(arr[i], end=" ")
print("\r")

# popping elements
popped_elem=arr.pop(1)
print(f"The popped element is {popped_elem}.")
print("\r")

# using remove() function to remove first occurence of element in the array
arr.remove(1)
for i in range(0,len(arr)):
    print(arr[i], end=" ")
print("\r")




# usage of index function to return the index of the first occurence of value mentioned in arguments
idx_pos=arr.index(5)
print(idx_pos)

arr.append(2)

# using array reverse
arr.reverse()
for i in range(0,len(arr)):
    print(arr[i], end=" ")
print("\r")

# usage of typecode function to return the data type by which the array is initialised
print(arr.typecode)


#usage of itemsize func to return size in bytes of a single array element
print(arr.itemsize)

# usage of buffer_info() func to return a tuple representing the address in which array is stored and number of elements in it
print(arr.buffer_info())

print("That's good to hear")


#count func
count_val=arr.count(5)
print(count_val)


# extend func
arr1=array.array('i',[20,5])
arr.extend(arr1)
new_len_arr=len(arr1)+len(arr)
for i in range(0,6):
    print(arr[i])

# usage of fromList(list) func to append a list to the end of the array arr
li=[1,2,3]
arr.fromlist(li)
for i in range(0,9):
    print(arr[i])

# usage of toList(list) to convert array arr to a list
li2=arr.tolist()
print("\r")
for i in range(0, len(li2)):
    print(li2[i], end=" ")
    
    
