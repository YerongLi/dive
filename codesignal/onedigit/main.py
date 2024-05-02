import math
from collections import Counter
def solution1(nums):
    pairs = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            dig1 = list(str(nums[i]))
            dig2 = list(str(nums[j]))
            
            if len(dig1) == len(dig2):
                diff = 0
                for k in range(len(dig1)):
                    if dig1[k] != dig2[k]:
                        diff += 1
                if diff == 1:
                    pairs += 1
    return pairs


def solution2(items):
    # Function to count pairs within items_of_length with the same number of digits and differing on exactly one digit
    def count_items_of_length(ii, items_of_length):
        total = 0
        # Count occurrences of each item's frequency
        item_counter = [item for item in dict(Counter(items_of_length)).values()]
        # Calculate adjustment for pairs of equal items
        adjust_for_equal_items = 0
        for duplicate_item_count in item_counter:
            adjust_for_equal_items += math.comb(duplicate_item_count, 2)
        # Iterate over possible dropped indices
        for dropped_index in range(ii):
            # Generate items with the dropped index
            items_with_dropped_index = [item[:dropped_index] + item[dropped_index + 1:] for item in items_of_length]
            # Iterate over unique items with dropped index
            for item_with_dropped_index in set(items_with_dropped_index):
                # Count occurrences of item_with_dropped_index
                num_matching = sum((1 if item == item_with_dropped_index else 0 for item in items_with_dropped_index))
                # Add combinations of pairs differing on one digit
                total += math.comb(num_matching, 2)
            # Adjust total for pairs of equal items
            total -= adjust_for_equal_items
        return total

    # Convert items to strings for easier manipulation
    items = [str(item) for item in items]

    total = 0
    # Iterate over possible lengths of items
    for ii in range(1, 12): # Assuming maximum number of digits is 12.
        # Filter items by length
        items_of_length = [item for item in items if len(item) == ii]
        # Count pairs of items with the same length differing on exactly one digit
        total += count_items_of_length(ii, items_of_length)
    return total



# Test Case 1
nums = [1, 9, 33, 402, 420, 502, 1]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"

# Test Case 2
nums = [10, 20, 300, 4000]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 2 failed. Expected: {expected}, Got: {result}"

# Test Case 3
nums = [123, 234, 345, 456, 567]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 3 failed. Expected: {expected}, Got: {result}"

# Test Case 4
nums = [12, 23, 34, 45, 56]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 4 failed. Expected: {expected}, Got: {result}"

# Test Case 5
nums = [11, 22, 33, 44, 55, 66]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 5 failed. Expected: {expected}, Got: {result}"

# Test Case 6
nums = [1, 10, 100, 1000, 10000]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 6 failed. Expected: {expected}, Got: {result}"

# Test Case 7
nums = [11, 111, 1111, 11111]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 7 failed. Expected: {expected}, Got: {result}"

# Test Case 8
nums = [123, 124, 134, 234, 245, 345, 456]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 8 failed. Expected: {expected}, Got: {result}"

# Test Case 9
nums = [123, 234, 345, 456, 567, 678, 789, 890]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 9 failed. Expected: {expected}, Got: {result}"

# Test Case 10
nums = [12, 123, 234, 345, 456, 567, 678, 789, 890]
expected = solution1(nums)
result = solution(nums)
assert result == expected, f"Test Case 10 failed. Expected: {expected}, Got: {result}"
print("All test cases passed successfully.")

