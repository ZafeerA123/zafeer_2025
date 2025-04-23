---
layout: post
title: 3.4 BigO Lesson (4.22.2025) 
description: Homework and Notes for BigO lesson
type: issues 
comments: true
permalink: 3_4_BigO
categories: [Big Idea 3]
---

# Popcorn Hack 1
The TWO most efficient strategies are:
Use the modulus operator (%) to check if the remainder when divided by 2 is 0.

Check if the last digit is 0, 2, 4, 6, or 8 manually.

Explanation:
Both methods are O(1) in time complexity, meaning they give a result instantly regardless of the number's size. The modulus method directly uses arithmetic, while checking the last digit relies on a simple lookup, both avoiding unnecessary loops or data structures.

# Popcorn Hack 2
Time Complexity:
Linear Search: O(n) — it checks each element one by one until it finds the target or reaches the end.

Binary Search: O(log n) — it halves the search space each step by exploiting the sorted nature of the list.

How Many Times Faster is Binary Search than Linear Search?
When n = 10,000,000:

Linear Search takes about n steps → 10,000,000 steps.

Binary Search worst-case takes about log₂(n) steps → log₂(10,000,000) ≈ 24 steps.

So Binary Search is about 400,000 times faster than Linear Search in the worst case.

What Happens if You Increase data_size to 20,000,000?
Linear Search: Time roughly doubles because it has to check twice as many elements.

Binary Search: Time increases slightly, because log₂(20,000,000) ≈ 24-25 steps, only 1-2 more steps than before.

# Homework Hack 1

```python
import random
import time

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Merge Sort function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Generate list of 100 random numbers between 1 and 1000
random_list = [random.randint(1, 1000) for _ in range(100)]
# Make a copy for each sort to use the same data
list_for_bubble = random_list.copy()
list_for_merge = random_list.copy()

# Time Bubble Sort
start_bubble = time.time()
bubble_sort(list_for_bubble)
end_bubble = time.time()
bubble_time = end_bubble - start_bubble

# Time Merge Sort
start_merge = time.time()
merge_sort(list_for_merge)
end_merge = time.time()
merge_time = end_merge - start_merge

# Output results
print(f"Bubble Sort took: {bubble_time:.6f} seconds")
print(f"Merge Sort took: {merge_time:.6f} seconds")

if bubble_time < merge_time:
    print("Bubble Sort is faster.")
else:
    print("Merge Sort is faster.")
```

Bubble Sort took: 0.004230 seconds
Merge Sort took: 0.000140 seconds
Merge Sort is faster.

Why does Merge Sort consistently outperform Bubble Sort?
Merge Sort is better than Bubble Sort because Merge Sort breaks down the list and sorts smaller parts before merging them, giving it a better time complexity.

Bubble Sort repeatedly swaps adjacent elements and is inefficient for large lists due to too many comparisons and swaps.


# Homework Hack 2

```python
import random

# Linear Search function
def linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == target:
            return count
    return -1

# Binary Search function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    count = 0
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return count
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Generate sorted list of 100,000 numbers
sorted_list = list(range(1, 100001))

# Pick a random target
target = random.randint(1, 100000)

# Perform searches
linear_steps = linear_search(sorted_list, target)
binary_steps = binary_search(sorted_list, target)

print(f"Target: {target}")
print(f"Linear Search Steps: {linear_steps}")
print(f"Binary Search Steps: {binary_steps}")
```

1. Which search algorithm is faster, and why?

Binary Search is faster.

Binary Search gets rid of half of the remaining elements with each step, so its time complexity is O(log n).

Linear Search checks each element one by one, with time complexity O(n).

For a list of 100,000 numbers, Linear Search takes 100,000 steps in the worst case.

2. What happens if you run both searches on an unsorted list?

Linear Search still works fine because it doesn't depend on the order of elements.

Binary Search fails because it requires the list to be sorted. Without sorting, its logic for eliminating half of the elements doesn't work.