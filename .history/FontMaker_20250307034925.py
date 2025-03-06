import tkinter as tk
from tkinter import font

def show_font_preview():
    # 获取所选字体名称
    selected_font = font_listbox.get(font_listbox.curselection())
    # 获取所选字号
    selected_size = size_var.get()
    # 初始化字体样式字符串
    style = ""
    if bold_var.get():
        style += "bold "
    if italic_var.get():
        style += "italic"
    # 去除多余空格
    style = style.strip()
    # 创建字体对象
    preview_font = font.Font(family=selected_font, size=selected_size, weight="bold" if "bold" in style else "normal",
                             slant="italic" if "italic" in style else "roman")
    # 设置预览标签的字体
    preview_label.config(font=preview_font)
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

# 将所有字体添加到列表框中，并设置对应字体样式
for f in all_fonts:
    try:
        # 尝试创建该字体的 Font 对象
        item_font = font.Font(family=f, size=12)
        font_listbox.insert(tk.END, f)
        # 获取当前插入项的索引
        index = font_listbox.size() - 1
        # 设置该项的字体
        font_listbox.itemconfig(index, font=item_font)
    except tk.TclError:
        # 若创建字体对象失败（可能是不支持的字体），则以默认字体显示
        font_listbox.insert(tk.END, f)

# 创建字号选择下拉框
size_var = tk.IntVar(root)
size_var.set(24)  # 默认字号
sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
size_menu = tk.OptionMenu(root, size_var, *sizes)
tk.Label(root, text="字号:").pack(side=tk.LEFT, padx=10)
size_menu.pack(side=tk.LEFT, padx=10)

# 创建加粗和倾斜复选框
bold_var = tk.IntVar()
italic_var = tk.IntVar()
bold_checkbox = tk.Checkbutton(root, text="加粗", variable=bold_var)
italic_checkbox = tk.Checkbutton(root, text="倾斜", variable=italic_var)
bold_checkbox.pack(side=tk.LEFT, padx=10)
italic_checkbox.pack(side=tk.LEFT, padx=10)

# 创建一个按钮，点击时显示字体预览
preview_button = tk.Button(root, text="预览字体", command=show_font_preview)
preview_button.pack(pady=20)

# 创建一个标签用于预览字体
preview_label = tk.Label(root, text="请选择字体并点击预览。", font=("Arial", 24))
preview_label.pack(pady=20)

# 运行主循环
root.mainloop()