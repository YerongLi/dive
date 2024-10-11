from collections import deque
def solution(times):
    ans = -0x7f7f7f7f
    q = deque()
    for time in times:
        while q and q[0] < time: q.popleft()
        starttime = time
        if q : starttime = max(time, q[-1])
        finishtime = starttime + 300
        ans = max(ans, finishtime)
        q.append(finishtime)
    return ans

def solution2(times):
    ans = -0x7f7f7f7f
    # Store the finishing time of the people in the queue
    q = deque()

    for time in times:
        while q and q[0] < time: q.popleft()
        if len(q) == 10: continue
        # start time should be current time if the queue is empty,
        # start time the last finishing time if q is not empty
        finishtime = 300 + max(time, q[-1] if q else 0) 
        q.append(finishtime)
        ans = max(ans, finishtime)

def solution1(arrival_times):
    # Initialize variables
    current_time = 0
    queue = deque()
    max_completion_time = 0
    
    # Iterate over each arrival time
    for arrival_time in arrival_times:
        # Calculate the time it will take to process the person's ID check
        id_check_time = 5 * 60
        
        # Update the queue size based on the arrival time and the number of people already in the queue
        queue.append(arrival_time)
        
        # Process the queue until it's empty or there are more than 10 people in the queue
        while queue and queue[0] <= current_time:
            # Pop the person from the queue and update the queue size
            queue.popleft()
        
        # Check if the queue size exceeds 10
        if len(queue) > 10:
            # If yes, the person leaves immediately
            continue
        
        # Update the current time to the arrival time if the arrival time is greater than the current time
        current_time = max(current_time, arrival_time)
        
        # Calculate the time when the person's ID check will be completed
        completion_time = current_time + id_check_time
        
        # Update the maximum completion time if necessary
        max_completion_time = max(max_completion_time, completion_time)
        
        # Update the current time to the completion time
        current_time = completion_time
        
    return max_completion_time



arrival_times = [1,6,9,502]
expected = solution1(arrival_times)
result = solution(arrival_times)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"

arrival_times = [301, 601, 901, 1201, 1501, 1801, 2101, 2401, 2701, 3001, 3301, 3601, 13, 14, 15]
expected = solution1(arrival_times)
result = solution(arrival_times)
assert result == expected, f"Test Case 2 failed. Expected: {expected}, Got: {result}"
print("All test cases passed successfully.")

