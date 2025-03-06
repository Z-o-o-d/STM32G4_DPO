from PIL import Image

def convert_image_to_c_array(image_path, output_file_path):
    try:
        # 打开图片
        image = Image.open(image_path)
        # 获取图片的宽度和高度
        width, height = image.size
        # 转换为 RGB 模式
        image = image.convert('RGB')

        # 初始化 C 语言数组字符串
        c_array = f"const uint16_t image_array[][{width}] = {{\n"

        # 遍历图片的每一行
        for y in range(height):
            row_data = []
            # 遍历图片的每一列
            for x in range(width):
                # 获取像素值
                r, g, b = image.getpixel((x, y))
                # 将 RGB 值转换为 16 位无符号整数（5 - 6 - 5 格式）
                pixel_value = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                # 交换字节顺序（高比特和低比特弄反）
                swapped_pixel_value = ((pixel_value & 0xFF) << 8) | ((pixel_value >> 8) & 0xFF)
                row_data.append(f"0x{swapped_pixel_value:04x}")
            c_array += f"    {{{', '.join(row_data)}}}"
            if y < height - 1:
                c_array += ",\n"
            else:
                c_array += "\n"

        c_array += "};\n"

        # 输出图片的高和宽
        print(f"图片宽度: {width}")
        print(f"图片高度: {height}")

        # 保存为 .c 文件
        with open(output_file_path, 'w') as file:
            # 可以添加一些头文件包含和注释
            file.write(c_array)

        print(f"已将数组保存到 {output_file_path}")

    except Exception as e:
        print(f"处理图片时出错: {e}")

# 输入图片的路径，需要替换为实际图片路径
image_path = "logo-icon-white-bg.png"
# 输出 .c 文件的路径
output_file_path = "image_array.c"
convert_image_to_c_array(image_path, output_file_path)