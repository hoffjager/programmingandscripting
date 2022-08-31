from random import randint  # Python module that generates random numbers.
from timeit import repeat   # Python module that measures running time of algorithms.

def bubble_sort(array):
    # Reference: https://realpython.com/sorting-algorithms-python/
    n = len(array)

    for i in range(n):
        # The variable "already_sorted" that's set to True, ensures the function breaks if there is nothing left to sort within the array:
        already_sorted = True

        for j in range(n - i - 1):
        # The algorithm begins by examining each element in the array one by one, and comparing each element with the value adjacent to it:
            if array[j] > array[j + 1]:
                # If the element is greater than its adjacent value, then the elements are swapped:
                array[j], array[j + 1] = array[j + 1], array[j]
                # Following on from swapping the elements, the variable "already_sorted" is set to False, 
                # this prevents the algorithm from ending before all the elements are analysed for sorting.
                already_sorted = False
        # If swapping is deemed impossible, then the array is deemed to be completely sorted and the algorithm will end and return the sorted array.
        if already_sorted:
            break
    return array

def merge(left, right):
    # Reference: https://realpython.com/sorting-algorithms-python/#implementing-merge-sort-in-python
    # Using the divide and conquer concept, the algorithm splits the array into two subarrays, named left and right.
    # If the left-hand subarray is empty, then return the right-hand subarray:
    if len(left) == 0:
        return right
    # If the right-hand subarray is empty, then return the left-hand subarray:
    if len(right) == 0:
        return left
    result = [] # The 'result' variable is used to store the recently sorted elements taken from both subarrays:
    index_left = index_right = 0
    # The algorithm checks through both subarrays until all elements are transferred into the ordered array 'result':
    while len(result) < len(left) + len(right):
        # All elements require sorting in order to add them to the ordered array 'result', a decision needs to be made on
        # whether to obtain the next element from the first subarray or second subarray:
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        # At the end of either subarray, the remaining elements from the other subarray
        # are added to the ordered array 'result', and the algorithm terminates.
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(array):
    # Reference: https://realpython.com/sorting-algorithms-python/#implementing-merge-sort-in-python
    # If the contents of the array contains only one element, the array is returned:
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # The array is sorted by recursively splitting it into two equal subarrays,
    # then sorting through each subarray, and finally merging both sorted subarrays into the final result.
    return merge(
        left = merge_sort (array[:midpoint]),
        right = merge_sort (array[midpoint:])
        )

def bucket_sort(input_list):
    # Reference: https://www.programiz.com/dsa/bucket-sort
    # Find the maximum value in the array, then
    # the length of the array determines which
    # value in the list goes into which bucket. 
    max_value = max(input_list)
    size = max_value/len(input_list)
    # Create n empty buckets, where n is equal to
    # the length of the input list.
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([]) 
    # Put list elements into different buckets
    # based on the size.
    for i in range(len(input_list)):
        j = int(input_list[i]/size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])
    # Sort elements within the buckets
    # via the Insertion Sort algorithm.
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
    # Concatenate buckets with sorted elements
    # into a single list.
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

def insertion_sort(array):
    # Reference: https://www.programiz.com/dsa/insertion-sort
    # The for Loop is set to begin at Index 1 in the array and proceed to the last element:
    for i in range(1, len(array)):
        # The 'key_item' is declared as the element to be repositioned within the array:
        key_item = array[i]
        # The variable 'j' is to be used to find the correct position of the `key_item`.
        j = i - 1
        # Iterate through the list of items (the left portion of the array) in order to
        # find the correct position of the element referenced by the variable `key_item`.
        while j >= 0 and array[j] > key_item:
            # The value is pushed one over to the left and j is relocated (from right to left),
            # in order to point to the next element to be sorted.
            array[j + 1] = array[j]
            j -= 1
        # When all elements have been moved in the array, the `key_item` is then placed in its correct location.
        array[j + 1] = key_item
    return array

def quicksort(array):
    # If the input array contains only one element, this is returned as the result.
    if len(array) < 2:
        return array

    low, same, high = [], [], [] # arrays used to store various values in comparison to the pivot's value.

    # The `pivot` element is randomly selected.
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        # Elements that are less than the `pivot` will be stored in the 'low` array.
        # Elements that are equal to the `pivot` will be stored in the `same` array.
        # Elements that are greater than the `pivot` will be stored in the `high` array.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    # The final result combines the three sorted arrays, `low`, `same` and `high`.
    return quicksort(low) + same + quicksort(high)

def run_sorting_algorithm(algorithm, array):
    # Reference: https://realpython.com/sorting-algorithms-python/#implementing-bubble-sort-in-python
    # The 'setup_code' variable is used to prepare the call to the specified algorithm using the supplied array.
    # This variable only imports the algorithm function if it is not Python's built-in function 'sorted()':
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    
    stmt = f"{algorithm}({array})"

    # 'times' variable is used to execute the algorithm 10 different times:
    times = repeat(setup = setup_code, stmt = stmt, repeat = 3, number = 10)

    # Print the name of the algorithm, the input size n used in the array,
    # and the average running time (converted to milliseconds & rounded to 3 decimal places):
    print(f"Algorithm: {algorithm}. Array Length: {array_length}. Average Running Time (ms): {round((sum(times)/10) * 1000, 3)}")

array_length = 100 # variable 'array_length' is used to facilitate various input sizes of data n for the list of sorting algorithms.

if __name__ == "__main__":
    # The variable 'array' consists of randomly generated integers from 0 to 999 (based on the input size data n stated in 'array_length'):
    array = [randint(0, 1000) for i in range(array_length)]
    # The function 'run_sorting_algorithm' is used to call upon each respective algorithm and the randomly assorted array: 
    run_sorting_algorithm(algorithm = "bubble_sort", array = array)
    run_sorting_algorithm(algorithm = "merge_sort", array = array)
    run_sorting_algorithm(algorithm = "bucket_sort", array = array)
    run_sorting_algorithm(algorithm = "insertion_sort", array = array)
    run_sorting_algorithm(algorithm = "quicksort", array = array)