def redact_card_numbers(text):
    pass


# Test cases for Part 1
assert redact_card_numbers("is this 123456789 a valid credit card") == "is this 123456789 a valid credit card"
assert redact_card_numbers("4111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert redact_card_numbers("My card number is 1234567890123") == "My card number is xxxxxxxxx0123"
assert redact_card_numbers("My card number is 1234567890123456") == "My card number is xxxxxxxxxxxx3456"
assert redact_card_numbers("My card number is 123456789012") == "My card number is 123456789012"

print("All Part 1 tests passed!")

def mask_specific_card_types(text):
    pass

def checksum(text):
    pass

# Test cases for Part 2
assert mask_specific_card_types("is this 123456789 a valid credit card") == "is this 123456789 a valid credit card"
assert mask_specific_card_types("4111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert mask_specific_card_types("341111111111111 is a valid card") == "xxxxxxxxxxx1111 is a valid card"
assert mask_specific_card_types("5111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert mask_specific_card_types("6011111111111111 is not a valid card") == "6011111111111111 is not a valid card"

print("All Part 2 tests passed!")
# assert 1 == 0, 'TEST'

# Test cases for the 3 question
assert checksum("basic_string 12345 no redaction") == "basic_string 12345 no redaction"
assert checksum("1234567890123456 is not valid") == "1234567890123456 is not valid"
assert checksum("421111111111111111 is not valid") == "421111111111111111 is not valid"
assert checksum("4234567890123456 is valid") == "xxxxxxxxxxxx3456 is valid"

print("All Part 3 tests passed!")
print("All third question tests passed!")


