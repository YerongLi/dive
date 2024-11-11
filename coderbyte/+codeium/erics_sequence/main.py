def solution(p):
    n = len(p)
    indices = sorted(range(n), key=lambda i : p[i])
    value = n
    a = [None] * n
    l, r = 0, n - 1
    while l <= r:
        if l >= n - p[indices[l]]:

            while r>= n - p[indices[l]] and l < r:
                a[indices[r]] = value
                value-= 1
                r-= 1
            a[indices[l]] = value
            l+= 1
            value-= 1
        else:
            while r>= n - p[indices[l]] and l < r:
                a[indices[r]] = value
                value-= 1
                r-= 1
            a[indices[l]] = -value
            l+= 1
            value-= 1
    return a

from bisect import *
def generate(nums):
    # Sort the list to enable binary search
    sorted_nums = sorted(nums)
    n = len(nums)
    result = []
    
    # Iterate over each element in the original list
    for num in nums:
        # Target we need to beat in sorted list
        target = -num
        # Find the first index in sorted_nums where sorted_nums[j] > target
        idx = bisect_left(sorted_nums, target + 1)
        # Count of elements in sorted_nums that satisfy nums[i] + nums[j] > 0
        count = n - idx
        result.append(count)
    
    return result

pairs = [3, 2, 3]
print(solution(pairs))

nums = [2, -1, 3]
pairs = generate(nums)
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-3, 1, 2, -3, 5]
pairs = generate(nums) # [1, 3, 3, 1, 5]
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-5, -2, 1, 3, 6, 8]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-7, -4, 2, 5, 9, 10]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)


nums = [-6, -1, 3, 4, 7, 11]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-8, -5, 1, 3, 7, 9]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-9, -6, 2, 4, 10, 11]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-7, -3, 5, 6, 8, 12]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-12, -4, 1, 2, 9, 13]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-11, -2, 4, 5, 10, 14]
pairs = generate(nums) 
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)

nums = [-10, -3, 3, 6, 8, 15]
pairs = generate(nums)
# print(generate(solution(pairs)), pairs, )
assert generate(solution(pairs)) == pairs,(
    f"Assertion failed: The output of generate(solution(pairs)) does not match the original pairs.\n"
    f"Expected (original pairs): {pairs}\n"
    f"Generated (from solution): {generate(solution(pairs))}"
)


assert solution([3,2,3]) == [2, -1, 3]
assert solution([0,0,0,1]) == [-4, -3, -2, 1]
assert solution([6,5,5,3,3,1]) == [6, 3, 4, -2, -1, -5]
assert solution([3,3,4,1,0]) ==  [1, 2, 4, -3, -5]

print(solution([1,1,1,1]))
