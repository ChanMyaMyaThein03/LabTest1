print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if n == 0:
        return 0
    
    if not all(isinstance(x,int) for x in arr):
       return 2


    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []
    else:
        arr_result = 1

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    arr_ascend = [64, 34, 25, 12, 22, 11, 90]
    arr_descend = [64, 34, 25, 12, 22, 11, 90]

    arr_greater = [64, 34, 25, 12, 22, 11, 90, 25, 48, 30]

    arr_empty = []

    arr_notInt = [64, '34', 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr_ascend, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr_descend, SORT_DESCENDING)
    print(result)

    # total numbers >= 10
    print("List greater than 10")
    result = bubble_sort(arr_greater, SORT_ASCENDING)
    print(result)

    # empty list
    print("Empty list")
    result = bubble_sort(arr_empty,SORT_ASCENDING)
    print(result)

    #Non Integr list
    print("Non Integer List ")
    result = bubble_sort(arr_notInt,SORT_ASCENDING)
    print(result)

if __name__ == "__main__":
    main()


