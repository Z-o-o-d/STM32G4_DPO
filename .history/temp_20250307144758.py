'''
Author: Zeee jinze2021@dgut.edu.cn
Date: 2025-03-07 14:47:40
LastEditors: Zeee jinze2021@dgut.edu.cn
LastEditTime: 2025-03-07 14:47:52
FilePath: \DPO1\temp.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 定义彩虹的基础颜色（RGB）
rainbow_colors = [
    (255, 0, 0),    # 红色
    (255, 165, 0),  # 橙色
    (255, 255, 0),  # 黄色
    (0, 128, 0),    # 绿色
    (0, 0, 255),    # 蓝色
    (75, 0, 130),   # 靛色
    (238, 130, 238) # 紫色
]

# 计算需要插值的颜色数量
total_colors = 10
base_color_count = len(rainbow_colors)
interpolation_count = total_colors - base_color_count

# 计算每两个基础颜色之间需要插入的颜色数量
step = interpolation_count // (base_color_count - 1)
remainder = interpolation_count % (base_color_count - 1)

# 存储最终生成的颜色
final_colors = []

# 开始生成颜色
for i in range(base_color_count - 1):
    r1, g1, b1 = rainbow_colors[i]
    r2, g2, b2 = rainbow_colors[i + 1]

    # 插入当前基础颜色
    final_colors.append((r1, g1, b1))

    # 计算每一步的插值增量
    current_step = step
    if i < remainder:
        current_step += 1

    for j in range(1, current_step + 1):
        r = int(r1 + (r2 - r1) * j / (current_step + 1))
        g = int(g1 + (g2 - g1) * j / (current_step + 1))
        b = int(b1 + (b2 - b1) * j / (current_step + 1))
        final_colors.append((r, g, b))

# 插入最后一个基础颜色
final_colors.append(rainbow_colors[-1])

# 输出为 24 位十六进制数据
hex_colors = []
for r, g, b in final_colors[:total_colors]:
    hex_color = (r << 16) | (g << 8) | b
    hex_colors.append(f"0x{hex_color:06X}")

for hex_color in hex_colors:
    print(hex_color)