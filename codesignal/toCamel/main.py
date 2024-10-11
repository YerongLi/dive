def solution1(str: str) -> str:
   def convert(s):
       start_underscores = len(s) - len(s.lstrip('_'))  # 保留开头的下划线
       end_underscores = len(s) - len(s.rstrip('_'))    # 保留结尾的下划线
       
       # 处理中间部分，去掉中间的下划线
       middle_part = s.strip('_')  # 去掉前后的下划线
       parts = middle_part.split('_')  # 按下划线分割
       
       # 第一个部分保持不变，其他部分首字母大写
       middle_converted = parts[0] + ''.join(word.capitalize() for word in parts[1:])
       
       # 拼接前后的下划线和中间处理后的字符串
       return '_' * start_underscores + middle_converted + '_' * end_underscores
   words = [convert(s) for s in str.split()]
   return ' '.join(words)
# Example usage
docString = "This is a document includes `first_variable second_camel_varible`. There are also symbols `FIRST_CONSTANT` and `third_variable`."
print(solution1(docString))
