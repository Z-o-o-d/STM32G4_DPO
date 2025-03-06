def read_and_process_c_file(input_file_path, output_file_path):
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

    # 将结果转换为十六进制字符串列表
    hex_strings = [f"0x{value:04X}" for value in final_result]

    # 以逗号连接十六进制字符串
    output_content = ', '.join(hex_strings)

    # 写入输出文件
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_content)

    return final_result


# 示例使用
input_file_path = 'test.c'  # 替换为实际的输入 .c 文件路径
output_file_path = 'your_output_file.c'  # 替换为实际的输出 .c 文件路径
result = read_and_process_c_file(input_file_path, output_file_path)
