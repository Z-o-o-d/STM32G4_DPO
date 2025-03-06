import tkinter as tk
from tkinter import font


def preview_font():
    try:
        selected_font_name = font_listbox.get(font_listbox.curselection())
        selected_size = size_var.get()
        font_style = []
        if bold_var.get():
            font_style.append("bold")
        if italic_var.get():
            font_style.append("italic")
        preview_font_obj = font.Font(family=selected_font_name, size=selected_size,
                                     weight="bold" if "bold" in font_style else "normal",
                                     slant="italic" if "italic" in font_style else "roman")
        preview_label.config(font=preview_font_obj)
        preview_label.config(text=f"这是 {selected_font_name} 字体的预览。")
    except tk.TclError:
        preview_label.config(text="所选字体可能不支持，请选择其他字体。")


root = tk.Tk()
root.title("字体选择与预览")

# 获取系统所有字体
all_fonts = font.families()

# 创建字体列表框，增大宽度和高度
font_listbox = tk.Listbox(root, width=80, height=20)
font_listbox.pack(pady=10)

# 将字体添加到列表框并设置对应字体样式
for font_name in all_fonts:
    try:
        # 尝试创建字体对象
        font_obj = font.Font(family=font_name, size=14)
        font_listbox.insert(tk.END, font_name)
        index = font_listbox.size() - 1
        font_listbox.itemconfig(index, font=font_obj)
    except tk.TclError:
        # 若字体不支持则以默认字体显示
        default_font = font.Font(size=14)
        font_listbox.insert(tk.END, font_name)
        index = font_listbox.size() - 1
        font_listbox.itemconfig(index, font=default_font)

# 字号选择
size_var = tk.IntVar()
size_var.set(24)
font_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
size_label = tk.Label(root, text="字号:")
size_label.pack(side=tk.LEFT, padx=10)
size_menu = tk.OptionMenu(root, size_var, *font_sizes)
size_menu.pack(side=tk.LEFT, padx=10)

# 加粗和倾斜复选框
bold_var = tk.IntVar()
italic_var = tk.IntVar()
bold_checkbox = tk.Checkbutton(root, text="加粗", variable=bold_var)
italic_checkbox = tk.Checkbutton(root, text="倾斜", variable=italic_var)
bold_checkbox.pack(side=tk.LEFT, padx=10)
italic_checkbox.pack(side=tk.LEFT, padx=10)

# 预览按钮
preview_button = tk.Button(root, text="预览字体", command=preview_font)
preview_button.pack(pady=20)

# 预览标签
preview_label = tk.Label(root, text="请选择字体并点击预览。", font=("Arial", 24))
preview_label.pack(pady=20)

root.mainloop()