def solution1(s: str) -> str:
    start_underscores = len(s) - len(s.lstrip('_'))  # 保留开头的下划线
    end_underscores = len(s) - len(s.rstrip('_'))    # 保留结尾的下划线
    
    # 处理中间部分，去掉中间的下划线
    middle_part = s.strip('_')  # 去掉前后的下划线
    parts = middle_part.split('_')  # 按下划线分割
    
    # 第一个部分保持不变，其他部分首字母大写
    middle_converted = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    # 拼接前后的下划线和中间处理后的字符串
    return '_' * start_underscores + middle_converted + '_' * end_underscores



# 测试用例
input_str = "leet_code"
expected = "leetCode"

# Run the solution and get the result
result = solution(input_str)

# Use assert to test if the result matches the expected output
assert result == expected

input_str = '_leet_code_'
expected = "_leetCode_"

# Run the solution and get the result
result = solution(input_str)
assert result == expected


input_str = '____leet_code_'
expected = "____leetCode_"

# Run the solution and get the result
result = solution(input_str)
assert result == expected

input_str = '__he_llo how are you_'
expected = "__heLlo how are you_"

# Run the solution and get the result
result = solution(input_str)
assert result == expected

input_str = '__he_l_lo how are you hm_mmmm___'
expected = "__heLLo how are you hmMmmm___"

# Run the solution and get the result
result = solution(input_str)
assert result == expected

input_str = '____leet_code_'
expected = "____leetCode_"

# Run the solution and get the result
result = solution(input_str)
assert result == expected

