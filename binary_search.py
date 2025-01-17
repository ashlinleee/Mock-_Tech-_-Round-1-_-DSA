def binary_search_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence
def count_occurrences(arr, target, first_index):
    if first_index == -1:
        return 0
    count = 0
    for i in range(first_index, len(arr)):
        if arr[i] == target:
            count += 1
        else:
            break
    return count
def find_first_and_count(arr, target):
    first_index = binary_search_first_occurrence(arr, target)
    if first_index == -1:
        return -1
    count = count_occurrences(arr, target, first_index)
    return (first_index, count)
arr = list(map(int, input("Enter the sorted array with spaces in between: ").split()))
target = int(input("Enter the target value: "))
result = find_first_and_count(arr, target)
if result == -1:
    print("-1 (target not found)")
else:
    print(f"First occurrence is at index {result[0]}, and there are {result[1]} occurrences of {target}.")