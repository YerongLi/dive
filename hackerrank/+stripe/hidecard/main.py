def mask_credit_card_numbers(text):
    words = text.split()
    for i, word in enumerate(words):
        if word.isdigit() and 13 <= len(word) <= 16:
            words[i] = 'x' * (len(word) - 4) + word[-4:]
    ans = ' '.join(words)
    print(ans)
    return ans

# Test cases for Part 1
assert mask_credit_card_numbers("is this 123456789 a valid credit card") == "is this 123456789 a valid credit card"
assert mask_credit_card_numbers("4111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert mask_credit_card_numbers("My card number is 1234567890123") == "My card number is xxxxxxxxxx0123"
assert mask_credit_card_numbers("My card number is 1234567890123456") == "My card number is xxxxxxxxxxxx3456"
assert mask_credit_card_numbers("My card number is 123456789012") == "My card number is 123456789012"

print("All Part 1 tests passed!")

def mask_specific_card_types(text):
    words = text.split()
    for i, word in enumerate(words):
        if word.isdigit() and 13 <= len(word) <= 16:
            if word.startswith('4'):  # Visa
                words[i] = 'x' * (len(word) - 4) + word[-4:]
            elif word.startswith('34') or word.startswith('37'):  # American Express
                words[i] = 'x' * (len(word) - 4) + word[-4:]
            elif 51 <= int(word[:2]) <= 55:  # MasterCard
                words[i] = 'x' * (len(word) - 4) + word[-4:]
    return ' '.join(words)

# Test cases for Part 2
assert mask_specific_card_types("is this 123456789 a valid credit card") == "is this 123456789 a valid credit card"
assert mask_specific_card_types("4111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert mask_specific_card_types("341111111111111 is a valid card") == "xxxxxxxxxxx1111 is a valid card"
assert mask_specific_card_types("5111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert mask_specific_card_types("6011111111111111 is not a valid card") == "6011111111111111 is not a valid card"

print("All Part 2 tests passed!")

