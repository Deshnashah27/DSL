'''Write a Python program to store second year percentage of students in array.
Write function for sorting array of floating point numbers in ascending order using
Insertion sort,Shell Sort and display top five scores.Display sorted data with passes.'''
#https://github.com/Deshnashah27



def shellSort(data, n):

    
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp
            print(data)
        gap //= 2





def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i- 1
             
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key
        print(data)





data=[]
n=int(input("Enter the size of array: "))
for i in range (n):
    print("Enter the elements ",i+1,"=")
    m=float(input())
    data.append(m)
    
print("Unsorted data: ",data)
insertionSort(data)
print('\n\nSorted Array using insertion sort:')
print(data)
print("\n\n")
shellSort(data,n)
print('\n\nSorted Array using shell sort:')
print(data)

data.reverse()
for i in range (5):
    print(data[i])
