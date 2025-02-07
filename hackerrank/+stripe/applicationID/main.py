def part1(input_data):
    i = 0
    n = len(input_data)
    ans = []
    while i < n:
        if input_data[i] == '0':
            break
        length = int(input_data[i: i + 2])
        ans.append(input_data[i + 2: i + 2 + length])
        i = i + 2 + length
    return ans
def part2(card_application_ids, terminal_application_ids):
    i = 0
    n = len(card_application_ids)
    ans = set()
    while i < n:
        if card_application_ids[i] == '0':
            break
        length = int(card_application_ids[i: i + 2])
        aid = card_application_ids[i + 2: i + 2 + length]
        ans.add(aid[:10])
        i = i + 2 + length
    res = set()
    for a in terminal_application_ids:
        if a[:10] in ans:
            res.add(a)


    return list(res)
def test_part1():
    """Test part1 function that extracts Application IDs from the concatenated string."""
    input_data = "18D2760000254550010016A00000000310100116A0000000031010020"
    expected_output = ["D27600002545500100", "A000000003101001", "A000000003101002"]
    assert part1(input_data) == expected_output

def test_part2():
    """Test part2 function that supports partial matching and deduplication."""
    card_application_ids = "18D2760000254550010016A00000000310100110A0000000030"
    terminal_application_ids = ["A000000003101001", "A000000003101002", "D27600002545500100"]
    expected_output = set(["D27600002545500100", "A000000003101001", "A000000003101002"])
    assert set(part2(card_application_ids, terminal_application_ids)) == set(expected_output)

    # Additional test case from the image
    card_application_ids = "18D2760000254550010016A00000000310100116A0000000031010020"
    terminal_application_ids = ["D27600002545500100", "A000000003101001"]
    expected_output = ["D27600002545500100", "A000000003101001"]
    assert set(part2(card_application_ids, terminal_application_ids)) == set(expected_output)

if __name__ == "__main__":
    test_part1()
    test_part2()
    print("All tests passed.")
