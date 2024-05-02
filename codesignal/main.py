def solution1(members, messages):
   # Initialize a dictionary to store the count of mentions for each member
   mention_count = {member: 0 for member in members}


   # Iterate through each message
   for message in messages:
       # Split the message into words
       words = message.split()
       user_ids = set()

       # Iterate through each word
       for word in words:
           # Check if the word starts with "@"
           if word.startswith("@"):
               # Extract the user ids mentioned
               user_ids = user_ids.union(set(word[1:].split(",")))
               # Iterate through the user ids mentioned
       for user_id in user_ids:
            # Check if the user id is in the members list
            if user_id in members:
                # Increment the count of mentions for the user id
                mention_count[user_id] += 1


   # Sort the mention count in descending order
   sorted_mentions = sorted(mention_count.items(), key=lambda x: x[1], reverse=True)


   # Generate the output in the required format
   output = [f"{member}={count}" for member, count in sorted_mentions]
   return output
def solution(members, messages):
    return None

# Example usage:

members = ["id123", "id321", "id700", "id8"]
messages = [
   "hi @id123,id321,id800 please check this issue. @id123 what do you think the issue is?",
   "@id123 great job! nice approach!"
]
expected = solution1(members, messages)
result = solution(members, messages)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"

