def convert_to_camel_case(docString):
   def to_camel_case(match):
       snake_case = match.group(1)
       words = snake_case.split('_')
       return words[0] + ''.join(word.capitalize() for word in words[1:])


   import re
   pattern = r'`([^`]+)`'  # 匹配反引号``之间的任意内容，除了反引号自身
   result = re.sub(pattern, lambda x: '`' + to_camel_case(x) + '`', docString)  # 保留原始的反引号
   return result


# Example usage
docString = "This is a document includes `first_variable second_camel_varible`. There are also symbols `FIRST_CONSTANT` and `third_variable`."
print(convert_to_camel_case(docString))
