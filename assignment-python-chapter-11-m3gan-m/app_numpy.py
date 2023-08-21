#megan moore
import numpy as np

simple_list = [1,2,3]
array=np.array(simple_list)
print(array)
print(type(array))

print("----Multidimensional array")
multidimensional_list = [
    [1,2,3],
    [4,5,6]
]
array=np.array(multidimensional_list)
print(array)
print(type(array))
print(f"Dimensions are {array.shape}")

print("-----Initializing arrays")
array=np.zeros((2,4),dtype=int)
print(array)
array=np.ones((2,4),dtype=int)
print(array)
array=np.full((2,4),99,dtype=int)
print(array)

array=np.random.random((2,4))
print(array)

print("-----Accessing elements in the array")
print(array[0,0])
print(array[0,1])
print(array[1,0])
print(array[1,1])

print("-----Loop through elements in the array")
for element in array:
    print(element)

print("-----Loop through individual items in array")
for element in array:
    for item in element:
        print(item)

print("-"*30)
print(array>0.2)
print(array[array>0.2])
print(np.round(array))
print("-"*30)
first = np.array([1,2,3])
second=np.array([1,2,3])
print(first+second)
print(first-second)
print(first*second)
print(first+100)

print("-----convert inches to cm")
dimensions_inch=np.array([1,2,3])
dimensions_cm=dimensions_inch*2.54
print(dimensions_cm)

print("-----convert inches to cm")
dimensions_cm = [x*2.54 for x in dimensions_inch]
print(dimensions_cm)