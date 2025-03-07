'''
Author: Zeee jinze2021@dgut.edu.cn
Date: 2025-03-07 14:47:40
LastEditors: Zeee jinze2021@dgut.edu.cn
LastEditTime: 2025-03-07 15:01:07
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

# 灯的数量
num_lights = 10

# 计算每个颜色间隔对应的索引步长
step = len(rainbow_colors) / num_lights

# 存储最终生成的颜色
final_colors = []

# 生成 10 个灯的颜色
for i in range(num_lights):
    # 计算当前索引对应的颜色位置
    index = i * step
    # 获取颜色区间的起始和结束索引
    start_index = int(index)
    end_index = (start_index + 1) % len(rainbow_colors)
    # 计算插值比例
    fraction = index - start_index

    # 获取起始和结束颜色
    r1, g1, b1 = rainbow_colors[start_index]
    r2, g2, b2 = rainbow_colors[end_index]

    # 线性插值计算当前颜色
    r = int(r1 + (r2 - r1) * fraction)
    g = int(g1 + (g2 - g1) * fraction)
    b = int(b1 + (b2 - b1) * fraction)

    final_colors.append((r, g, b))

# 输出为 C 语言数组定义格式
print("RGBColor rainbow_colors[10] = {")
for i, (r, g, b) in enumerate(final_colors):
    line = f"    {{{r:3d}, {g:3d}, {b:3d}}}"
    if i < len(final_colors) - 1:
        line += ","
    print(line)
print("};")