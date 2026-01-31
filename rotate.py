#brute-force approach to rotate an array to the right by k steps
def rotate_array(array,k):
    if len(array)==0:
        return []

    k = k%len(array)
    temp = array[-k:]
    for i in reversed(range(0,len(array)-k)):
        array[i+k]=array[i]
    for i in range(len(temp)):
        array[i]=temp[i]


    return array

list1=[1,2,3,4,5,6,7]
k=3
print(rotate_array(list1,k))  #output: [5,6,7,1,2,3,4]
#time complexity: O(n) where n is the length of the array space complexity: O(k) where k is the number of rotations

#optimal approach to rotate an array to the right by k steps
def rotate_array_optimal(array,k):
    if len(array)==0:
        return []

    k = k%len(array)

    def reverse(sub_array,start,end):
        while start<end:
            sub_array[start],sub_array[end]=sub_array[end],sub_array[start]
            start+=1
            end-=1

    reverse(array,0,len(array)-1)
    reverse(array,0,k-1)
    reverse(array,k,len(array)-1)

    return array

list2=[1,2,3,4,5,6,7]
k=3
print(rotate_array_optimal(list2,k))  #output: [5,6,7,1,2,3,4]
#time complexity: O(n) where n is the length of the array space complexity: O(1)