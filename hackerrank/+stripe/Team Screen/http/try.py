from collections import defaultdict
def parse_accept_language(accept_language_header, supported_languages):
    accept_language_header = [x.strip() for x in accept_language_header.split(',')]
    m = {}
    for i, x in enumerate(accept_language_header):
        m[x] = i
    ans = []

    for x in supported_languages:
        if x in m:
            ans.append((m[x], x))
        elif '-' in x and x.split('-')[0] in m:
            ans.append((m[x.split('-')[0]], x))
        elif '*' in m:
            ans.append((m['*'], x))
    ans.sort()
    ans = [x for _, x in ans]
    return ans
def part4(accept_language_header, supported_languages):
    accept_language_header = [x.strip() for x in accept_language_header.split(',')]
    m = {}
    for x in accept_language_header:
        name, q = x.split(';')
        q = float(q[2:])
        m[name] = q
    ans = []

    for x in supported_languages:
        if x in m:
            ans.append((m[x], x))
        elif '-' in x and x.split('-')[0] in m:
            ans.append((m[x.split('-')[0]], x))
        elif '*' in m:
            ans.append((m['*'], x))
    ans.sort(reverse=True)
    ans = [x for _, x in ans]
    return ans

    # return ans
# Test case 1: Matching both languages in descending order of preference
assert parse_accept_language(
    "en-US, fr-CA, fr-FR", ["fr-FR", "en-US"]
) == ["en-US", "fr-FR"], "Test case 1 failed"

# Test case 2: Matching only the second preference
assert parse_accept_language(
    "fr-CA, fr-FR", ["en-US", "fr-FR"]
) == ["fr-FR"], "Test case 2 failed"

# Test case 3: Matching only the first language
assert parse_accept_language(
    "en-US", ["en-US", "fr-CA"]
) == ["en-US"], "Test case 3 failed"

# Test case 4: No matching languages
assert parse_accept_language(
    "fr-CA", ["en-US", "fr-FR"]
) == [], "Test case 4 failed"

# Test case 5: Multiple matches but unordered input
assert parse_accept_language(
    "fr-FR, en-US", ["en-US", "fr-FR"]
) == ["fr-FR", "en-US"], "Test case 5 failed"

# Test Part 1
assert parse_accept_language("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"]) == ["en-US", "fr-FR"]
assert parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"]) == ["fr-FR"]
assert parse_accept_language("en-US", ["en-US", "fr-CA"]) == ["en-US"]

# Test Part 2
assert parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"]) == ["en-US"]
assert parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"]) == ["fr-CA", "fr-FR"]
assert parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"]) == ["fr-FR", "fr-CA"]

# Test Part 3
assert parse_accept_language("en-US, *", ["en-US", "fr-CA", "fr-FR"]) == ["en-US", "fr-CA", "fr-FR"]
assert parse_accept_language("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"]) == ["fr-FR", "fr-CA", "en-US"]

# Test Part 4
assert part4("fr-FR;q=1, fr-CA;q=0, fr;q=0.5", ["fr-FR", "fr-CA", "fr-BG"]) == ["fr-FR", "fr-BG", "fr-CA"]
assert part4("fr-FR;q=1, fr-CA;q=0, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"]) == ["fr-FR", "fr-BG", "en-US", "fr-CA"]
assert part4("fr-FR;q=1, fr-CA;q=0.8, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"]) == ["fr-FR", "fr-CA", "fr-BG", "en-US"]

print("All tests passed!")