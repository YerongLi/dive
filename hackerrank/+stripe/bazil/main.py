import pandas as pd

def solve1(input_list):
    # Your implementation of solve1 goes here
    
    pass

# Example input list of strings
input_list = [
    "customer_id,merchant_id,payout_date,card_type,amount",
    "cust1,merchantA,2021-12-30,Visa,150",
    "cust2,merchantA,2021-12-30,Visa,200",
    "cust3,merchantB,2021-12-31,MasterCard,300",
    "cust4,merchantA,2021-12-30,Visa,50"
]

# Expected output DataFrame
expected_output = pd.DataFrame({
    "merchant_id": ["merchantA", "merchantB"],
    "card_type": ["Visa", "MasterCard"],
    "payout_date": ["2021-12-30", "2021-12-31"],
    "amount": [400, 300]
})

# Call the solve1 function with the input list
result = solve1(input_list)

# Convert the result to a pandas DataFrame
df = pd.DataFrame(result, columns=["merchant_id", "card_type", "payout_date", "amount"])

# Assert to compare the output of solve1 to the expected output
assert df.equals(expected_output), f"Test failed: {df} != {expected_output}"

print("Test passed!")
