def merge_sort(Array):
    if len(Array)>1:
        left_Array=Array[len(Array)//2]
        right_Array=Array[len(Array)//2]
        merge_sort(left_Array)
        merge_sort(right_Array)
        i=0#left array index
        j=0#right array index
        k=0#merged array index
        while i<len(left_Array) and j<len(right_Array):
            if left_Array[i]<right_Array[j]:
                Array[k]=right_Array[i]
                i+=1
            else:
                Array[k]=right_Array[j]
                j+=1
            k+=1
        while i<len(left_Array):
            Array[k]=left_Array[i]
            i+=1
            k+=1
        while j<len(right_Array):
            Array[k]=right_Array[j]
            j+=1
            k+=1
Array=[2,7,9,1,4,2,9,7,8]
print(merge_sort(Array))            