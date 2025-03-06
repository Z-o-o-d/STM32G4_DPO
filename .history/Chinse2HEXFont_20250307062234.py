def read_and_process_c_file(input_file_path, output_file_path, group_size, block_length):
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

    # 按指定分组长度进行分块处理
    final_sorted_values = []
    for i in range(0, len(sixteen_bit_values), block_length):
        block = sixteen_bit_values[i: i + block_length]
        if len(block) % group_size == 0:
            # 按指定组大小进行排序
            sorted_block = []
            num_groups = len(block) // group_size
            for j in range(group_size):
                for k in range(num_groups):
                    index = k * group_size + j
                    sorted_block.append(block[index])
            final_sorted_values.extend(sorted_block)

    # 将结果转换为十六进制字符串列表
    hex_strings = [f"0x{value:04X}" for value in final_sorted_values]

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

    return final_sorted_values


# 示例使用
input_file_path = 'test.c'  # 替换为实际的输入 .c 文件路径
output_file_path = 'your_output_file.c'  # 替换为实际的输出 .c 文件路径
group_size = 3  # 可根据需要设置分组大小，例如 2、3、4 等
block_length = 48  # 可根据需要设置分组长度
result = read_and_process_c_file(input_file_path, output_file_path, group_size, block_length)
