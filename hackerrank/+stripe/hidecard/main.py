def mask_credit_card_numbers(text):
    result = []
    i = 0
    while i < len(text):
        if text[i].isdigit():
            start = i
            while i < len(text) and text[i].isdigit():
                i += 1
            number = text[start:i]
            if 13 <= len(number) <= 16:
                result.append('x' * (len(number) - 4) + number[-4:])
            else:
                result.append(number)
        else:
            result.append(text[i])
            i += 1
    ans = ''.join(result)
    print(ans)
    return ans

# Test cases for Part 1
assert mask_credit_card_numbers("is this 123456789 a valid credit card") == "is this 123456789 a valid credit card"
assert mask_credit_card_numbers("4111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert mask_credit_card_numbers("My card number is 1234567890123") == "My card number is xxxxxxxxx0123"
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

def mask_specific_card_types(text):
    def is_valid_card(number):
        if 13 <= len(number) <= 16:
            if number.startswith('4'):  # Visa
                return True
            elif number.startswith('34') or number.startswith('37'):  # American Express
                return True
            elif 51 <= int(number[:2]) <= 55:  # MasterCard
                return True
        return False

    words = text.split()
    for i, word in enumerate(words):
        if word.isdigit() and is_valid_card(word):
            words[i] = 'x' * (len(word) - 4) + word[-4:]
    return ' '.join(words)

# Test cases for the third question
assert mask_specific_card_types("This is a card number 1234567890123456") == "This is a card number xxxxxxxxxxxx3456"
assert mask_specific_card_types("This is a card number 4111111111111111 but another one is 341111111111111") == "This is a card number xxxxxxxxxxxx1111 but another one is xxxxxxxxxxx1111"
assert mask_specific_card_types("This is a card number 5111111111111111") == "This is a card number xxxxxxxxxxxx1111"
assert mask_specific_card_types("This is a card number 6011111111111111") == "This is a card number 6011111111111111"

print("All third question tests passed!")


