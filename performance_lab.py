# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1

    max_count = 0
    result = None
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            result = num

    return result

"""
Time and Space Analysis for problem 1:
- Best-case: The best-case time-complexity is O(n). In a scenario where the input list is small and there is only one unique value, The program will iterate through each integer in the input list and each pair in the dictionary.
- Worst-case: The worst-case time complexity is O(n). In a scenario where the input list is large and every value is unique, the program will iterate through each integer in the input list and each pair in the dictionary.
- Average-case: The average-case time complexity is O(n). In a scenario where the input list is moderately sized and distributed randomly, the program will iterate through each integer in the input list and each pair in the dictionary.
- Space complexity: The space complexity of this program is O(n) because in all cases, the dictionary will store one entry per unique number.
- Why this approach?: Using a dictionary to store and update frequency is an efficient way to count unique values. The .get() and .items() methods handle errors well. 
- Could it be optimized?: Not in terms of its big-O performance, but the lines of code could be reduced using collections.Counter or combining the two loops. 
- Trade Offs?: O(n) time and space complexity means very large inputs can take up a lot of time and memory. 
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result 

"""
Time and Space Analysis for problem 2:
- Best-case: The best-case time-complexity is O(n). In a scenario where the input list is small and there are no duplicates, every integer is added to both the result list and the set.
- Worst-case: The worst-case time-complexitiy is O(n). In a scenario where the input list is large and there are many duplicates, every integer is added to both the reuslt list and the set. 
- Average-case: The average-case time-complexity is O(n). In a scenario where the input list is moderately sized and there is an even mixture of unique values and dupplicates, each integer is added to both the result list and the set. 
- Space complexity: The space-complexity of the program is O(n). Every integer is stored in both the result list and set. 
- Why this approach?: A set is the most efficient way to perform a membership check, and a list preserves order int he result. 
- Could it be optimized?: Not in terms of its big-O performance, but there may be a way to reduce the lines of code.
- Trade Offs?: O(n) time and space complexity means very large inputs can take up a lot of time and memory. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    result = []

    for num in nums:
        complement = target - num 
        if complement in seen:
            result.append((complement, num))
        seen.add(num)

    return result 

"""
Time and Space Analysis for problem 3:
- Best-case: The best-case time-complexity is O(n). In a scenario where the input list is small and there are no pairs, every integer gets scanned and membership checked.
- Worst-case: The worst-case time-complexity is O(n). In a scenario where the input list is large with many pairs, every integer gets scanned and membershio checked. 
- Average-case: The average-case time-complexity is O(n). In a scenario where the input list is moderately sized with some pairs, every integer gets scanned and membership checked.
- Space complexity: The space complexity is O(n). Every integer is stored in the seen set and all pairs in the result list.
- Why this approach?: A set is the most efficient way to check for membership.
- Could it be optimized?: Not in terms of big-O performance.
- Trade-Offs?: O(n) time and space complexity means the program will slow down and take up more memory as the input grows. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    items = []
    capacity = 1
    
    for i in range(n):
        if len(items) == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            capacity *= 2 
        
        items.append(i)

"""
Time and Space Analysis for problem 4:
- When do resizes happen?: Resizes happen when the number of items is equal to the current capacity.
- What is the worst-case for a single append?: The worst-case for a single append is when resizing occurs, since all items need to be copied.
- What is the amortized time per append overall?: The amortized time per append overall is O(1) since the average time cost will be constant.
- Space complexity: The space complextity is O(n) since every item is added to the list.
- Why does doubling reduce the cost overall?: Doubling the capacity keeps resizes from happening too often.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = []

    for num in nums:
        total = total + num
        result.append(total)
    
    return result 

"""
Time and Space Analysis for problem 5:
- Best-case: The best-case time-complexity is O(n). In a scenario with a short list of small positive integers, every number is added to the running total.
- Worst-case: The worst-case time-complexitty is O(n). In a scenario with a large list of large positive and negative integers, every number is added to the running total. 
- Average-case: Tbe average-case time-complextity is O(n). In a scenario with a moderately sized list of a mixture of various integers, every number is added to the running total. 
- Space complexity: The space complexity is O(n). The memory the program uses expands linearly with the size of the input. 
- Why this approach?: A for loop iterates throuh each integer once and storing the running total in a list preserves order.
- Could it be optimized?: Not in terms of time or space complexity. 
- Trade-Offs: None that I can see.
"""

# 🔍 Problem 1 Refactored: Find Most Frequent Element

def most_frequent(numbers):
    if not numbers:
        return None
    
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1

    return max(count, key=count.get)

"""
The time and space complexity remains O(n), however I believe this would be considered a refactor because it eliminates unnecessary variables and takes advantage of Python's built in functions. It makes the code more concise.
"""