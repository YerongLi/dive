def redact_card_numbers(text):
    n = len(text)
    i = 0
    start = None
    ans = []
    while i < n:
        if text[i].isdigit():
            start = i
            while i < n and text[i].isdigit():
                i+= 1
            number = text[start: i]
            if 13<= len(number) <= 16:
                ans.append((len(number) - 4) * 'x' + text[i-4:i])
            else:
                ans.append(number)
        else:
            ans.append(text[i])
            i+= 1
    result = ''.join(ans)
    return result


# Test cases for Part 1
assert redact_card_numbers("is this 123456789 a valid credit card") == "is this 123456789 a valid credit card"
assert redact_card_numbers("4111111111111111 is a valid card") == "xxxxxxxxxxxx1111 is a valid card"
assert redact_card_numbers("My card number is 1234567890123") == "My card number is xxxxxxxxx0123"
assert redact_card_numbers("My card number is 1234567890123456") == "My card number is xxxxxxxxxxxx3456"
assert redact_card_numbers("My card number is 123456789012") == "My card number is 123456789012"

print("All Part 1 tests passed!")

def mask_specific_card_types(text):
    n = len(text)
    i = 0
    start = None
    ans = []
    def check(number):
        found = False
        firsttwo = int(number[:2])
        first4 = int(number[:4])
        if 13 <= len(number) <= 16:
            if 13 == len(number) or len(number) == 16 and number[0] == '4': # VISA
                found = True
            # ans.append((len(number) - 4) * 'x' + text[i-4:i])
            elif number[:2] == '34' or number[2] == '37' and len(number) == 15: # AX
                found = True
            elif 51 <= firsttwo <= 55 or 2221 <= first4 <= 2720:
                found = True
        return found
    i = 0
    while i < n:
        if text[i].isdigit():
            start = i
            while i < n and text[i].isdigit():
                i+= 1
            number = text[start: i]
            if check(number):
                ans.append((len(number) - 4) * 'x' + number[-4:])
            else:
                ans.append(number)
        else:
            ans.append(text[i])
            i+= 1
    result = ''.join(ans)
    return result

def checksum(text):
    i = 0
    n = len(text)
    ans = []
    def check(number):
        found = False
        firsttwo = int(number[:2])
        first4 = int(number[:4])
        if 13 <= len(number) <= 16:
            if 13 == len(number) or len(number) == 16 and number[0] == '4': # VISA
                found = True
            # ans.append((len(number) - 4) * 'x' + text[i-4:i])
            elif number[:2] == '34' or number[2] == '37' and len(number) == 15: # AX
                found = True
            elif 51 <= firsttwo <= 55 or 2221 <= first4 <= 2720:
                found = True


        s = 0

        if not (13 <= len(number) <= 16): return False
        for j, x in enumerate(number):
            v = int(x)
            if j % 2 == 1:
                v*= 2
                if v >= 10:
                    v-= 9
            s+= v
        if s % 10 == 0: found = True
        return found
    while i < n:
        if text[i].isdigit():
            start = i
            while i < n and text[i].isdigit():
                i+= 1
            number = text[start: i]
            if check(number):
                ans.append((len(number) - 4) * 'x' + number[-4:])
            else:
                ans.append(number)
        else:
            ans.append(text[i])
            i+= 1
    result = ''.join(ans)
    return result

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


