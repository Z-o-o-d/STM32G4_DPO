'''
Author: Zeee jinze2021@dgut.edu.cn
Date: 2025-03-07 03:45:30
LastEditors: Zeee jinze2021@dgut.edu.cn
LastEditTime: 2025-03-07 03:45:38
FilePath: \DPO1\FontMaker.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import tkinter as tk
from tkinter import font

def show_font_preview():
    # 获取用户选择的字体
    selected_font = font_listbox.get(font_listbox.curselection())
    # 设置预览文本的字体
    preview_label.config(font=(selected_font, 24))
    # 更新预览文本
    preview_label.config(text=f"这是 {selected_font} 字体的预览。")

# 创建主窗口
root = tk.Tk()
root.title("字体选择与预览")

# 获取系统中所有可用的字体
all_fonts = font.families()

# 创建一个列表框来显示所有字体
font_listbox = tk.Listbox(root, width=50)
font_listbox.pack(pady=10)

# 将所有字体添加到列表框中
for f in all_fonts:
    font_listbox.insert(tk.END, f)

# 创建一个按钮，点击时显示字体预览
preview_button = tk.Button(root, text="预览字体", command=show_font_preview)
preview_button.pack(pady=10)

# 创建一个标签用于预览字体
preview_label = tk.Label(root, text="请选择字体并点击预览。", font=("Arial", 24))
preview_label.pack(pady=20)

# 运行主循环
root.mainloop()