'''
Author: Zeee jinze2021@dgut.edu.cn
Date: 2025-03-07 05:59:16
LastEditors: Zeee jinze2021@dgut.edu.cn
LastEditTime: 2025-03-07 05:59:47
FilePath: \DPO1\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def read_and_process_c_file(test.c):
    # 读取文件内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 提取十六进制数据
    hex_values = []
    lines = content.split('\n')
    for line in lines:
        values = line.replace(',', ' ').split()
        for value in values:
            if value.startswith('0x'):
                hex_values.append(int(value, 16))

    # 两两拼成16位
    sixteen_bit_values = []
    for i in range(0, len(hex_values), 2):
        if i + 1 < len(hex_values):
            # 将两个8位数据拼成一个16位数据
            combined_value = (hex_values[i] << 8) | hex_values[i + 1]
            sixteen_bit_values.append(combined_value)

    # 分离奇数字个和偶数字个的16位数据
    odd_index_values = []
    even_index_values = []
    for i, value in enumerate(sixteen_bit_values):
        if i % 2 == 0:
            odd_index_values.append(value)
        else:
            even_index_values.append(value)

    # 合并奇数字个和偶数字个的16位数据
    final_result = odd_index_values + even_index_values

    return final_result

# 示例使用
file_path = 'your_file.c'  # 替换为实际的 .c 文件路径
result = read_and_process_c_file(file_path)

# 输出结果
for value in result:
    print(f"0x{value:04X}")
