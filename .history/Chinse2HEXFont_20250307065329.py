'''
Author: Zeee jinze2021@dgut.edu.cn
Date: 2025-03-07 05:59:16
LastEditors: Zeee jinze2021@dgut.edu.cn
LastEditTime: 2025-03-07 06:53:23
FilePath: \DPO1\Chinse2HEXFont.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def read_and_process_c_file(input_file_path, output_file_path, group_size):
    # 读取文件内容
    with open(input_file_path, 'r') as file:
        content = file.read()

    # 提取十六进制数据
    hex_values = []
    lines = content.split('\n')
    for line in lines:
        values = line.replace(',', ' ').split()
        for value in values:
            if value.startswith('0x'):
                hex_values.append(int(value, 16))

    # 两两拼成 16 位
    sixteen_bit_values = []
    for i in range(0, len(hex_values), 2):
        if i + 1 < len(hex_values):
            combined_value = (hex_values[i] << 8) | hex_values[i + 1]
            sixteen_bit_values.append(combined_value)

    # 按指定组大小进行排序
    sorted_values = []
    num_groups = len(sixteen_bit_values) // group_size
    for i in range(group_size):
        for j in range(num_groups):
            index = j * group_size + i
            sorted_values.append(sixteen_bit_values[index])

    # 将结果转换为十六进制字符串列表
    hex_strings = [f"0x{value:04X}" for value in sorted_values]

    # 每隔 16 个元素插入换行符，同时保留逗号
    output_content = ""
    for i, hex_str in enumerate(hex_strings):
        output_content += hex_str
        if (i + 1) % 16 == 0:
            output_content += ",\n"
        elif i < len(hex_strings) - 1:
            output_content += ", "

    # 去除最后多余的逗号和空格
    output_content = output_content.rstrip(', ')

    # 写入输出文件
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_content)

    return sorted_values


# 示例使用
input_file_path = 'your_input_file.c'  # 替换为实际的输入 .c 文件路径
output_file_path = 'your_output_file.c'  # 替换为实际的输出 .c 文件路径
group_size = 3  # 可根据需要设置分组大小，例如 2、3、4 等
result = read_and_process_c_file(input_file_path, output_file_path, group_size)
