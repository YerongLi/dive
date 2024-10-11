import re

# 假设 `rooms` 是包含公寓描述的字典
rooms = {
    "room1": {"description": "This is a beautiful studio apartment."},
    "room2": {"description": "This apartment has 1b and a yoga studio."},
    "room3": {"description": "Spacious 1b apartment with great amenities."},
    "room4": {"description": "Charming studio with large windows."},
}

def filter_studios(rooms):
    studio_rooms = []
    # 定义正则表达式，不使用 IGNORECASE
    studio_pattern = re.compile(r'\bstudio\b')
    one_bed_pattern = re.compile(r'\b1b\b|\b1 bedroom\b')
    
    # 遍历每个房间的描述
    for room_name, room_info in rooms.items():
        # 将描述转为小写
        description = room_info["description"].lower()
        
        # 匹配包含 'studio' 且不包含 '1b' 或 '1 bedroom'
        if studio_pattern.search(description) and not one_bed_pattern.search(description):
            studio_rooms.append(room_name)
    
    return studio_rooms

# 调用函数并输出结果
filtered_rooms = filter_studios(rooms)
print(filtered_rooms)
