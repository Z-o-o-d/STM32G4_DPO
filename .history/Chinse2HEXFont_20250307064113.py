import re


def read_and_process_c_file(input_file_path, output_file_path, group_size):
    # 读取文件内容
    with open(input_file_path, 'r') as file:
        content = file.read()

    # 用于存储最终结果
    final_result = []
    # 存储当前分组的数据
    current_group = []
    # 正则表达式匹配注释
    comment_pattern = re.compile(r'/\*.*?\*/')
    comment_matches = comment_pattern.finditer(content)
    comment_positions = [0] + [match.start() for match in comment_matches] + [len(content)]

    for i in range(len(comment_positions) - 1):
        start_pos = comment_positions[i]
        end_pos = comment_positions[i + 1]
        sub_content = content[start_pos:end_pos]

        # 提取十六进制数据
        hex_values = []
        lines = sub_content.split('\n')
        for line in lines:
            values = line.replace(',', ' ').split()
            for value in values:
                if value.startswith('0x'):
                    hex_values.append(int(value, 16))

        # 两两拼成 16 位
        for j in range(0, len(hex_values), 2):
            if j + 1 < len(hex_values):
                combined_value = (hex_values[j] << 8) | hex_values[j + 1]
                current_group.append(combined_value)

                # 当分组达到指定大小，进行排序并添加到最终结果
                if len(current_group) == group_size:
                    sorted_group = []
                    for k in range(group_size):
                        sorted_group.append(current_group[k])
                    final_result.extend(sorted_group)
                    current_group = []

    # 处理最后不足一组的数据
    if current_group:
        final_result.extend(current_group)

    # 将结果转换为十六进制字符串列表
    hex_strings = [f"0x{value:04X}" for value in final_result]

    # 每隔 16 个元素插入换行符
    output_lines = []
    for i in range(0, len(hex_strings), 16):
        line = ', '.join(hex_strings[i: i + 16])
        output_lines.append(line)

    output_content = '\n'.join(output_lines)

    # 写入输出文件
    with open(output_file_path, 'w') as output_file:
        output_file.write(output_content)

    return final_result


# 示例使用
input_file_path = 'test.c'
output_file_path = 'your_output_file.c'
group_size = 3  # 可根据需要设置分组大小
result = read_and_process_c_file(input_file_path, output_file_path, group_size)
