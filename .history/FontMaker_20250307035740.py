import tkinter as tk
from tkinter import ttk
from tkinter import font


def preview_font(*args):
    try:
        selected_item = tree.selection()
        if selected_item:
            selected_font_name = tree.item(selected_item, "text")
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
            update_font_samples(selected_font_name, selected_size, font_style)
    except tk.TclError:
        preview_label.config(text="所选字体可能不支持，请选择其他字体。")


def update_font_samples(font_name, size, style):
    for i, sample_label in enumerate(sample_labels):
        sample_size = sample_sizes[i]
        sample_font_obj = font.Font(family=font_name, size=sample_size,
                                    weight="bold" if "bold" in style else "normal",
                                    slant="italic" if "italic" in style else "roman")
        sample_label.config(font=sample_font_obj)
        sample_label.config(text=f"{font_name} 字体 {sample_size} 号字预览")


root = tk.Tk()
root.title("字体选择与预览")

# 获取系统所有字体
all_fonts = font.families()

# 创建样式对象并设置 Treeview 的行高
style = ttk.Style()
style.configure("Custom.Treeview", rowheight=30)  # 调整行高，可根据需要修改值

# 创建 Treeview 来替代 Listbox
tree = ttk.Treeview(root, columns=("Fonts"), show="tree", style="Custom.Treeview")
tree.column("Fonts", width=400)
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# 将字体添加到 Treeview 并设置对应字体样式
for font_name in all_fonts:
    try:
        # 尝试创建字体对象
        font_obj = font.Font(family=font_name, size=14)
        tree.insert("", "end", text=font_name, tags=(font_name,))
        tree.tag_configure(font_name, font=font_obj)
    except tk.TclError:
        # 若字体不支持则以默认字体显示
        default_font = font.Font(size=14)
        tree.insert("", "end", text=font_name, tags=("default",))
        tree.tag_configure("default", font=default_font)

# 绑定 Treeview 的选择事件
tree.bind("<<TreeviewSelect>>", preview_font)

# 字号选择和样式选择的框架
option_frame = tk.Frame(root)
option_frame.pack(pady=10)

size_var = tk.IntVar()
size_var.set(24)
font_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
size_label = tk.Label(option_frame, text="字号:")
size_label.pack(side=tk.LEFT, padx=10)
size_menu = tk.OptionMenu(option_frame, size_var, *font_sizes, command=lambda _: preview_font())
size_menu.pack(side=tk.LEFT, padx=10)

bold_var = tk.IntVar()
italic_var = tk.IntVar()
bold_checkbox = tk.Checkbutton(option_frame, text="加粗", variable=bold_var, command=preview_font)
bold_checkbox.pack(side=tk.LEFT, padx=10)
italic_checkbox = tk.Checkbutton(option_frame, text="倾斜", variable=italic_var, command=preview_font)
italic_checkbox.pack(side=tk.LEFT, padx=10)

# 预览按钮（可保留也可删除，这里保留作为额外的触发方式）
preview_button = tk.Button(root, text="预览字体", command=preview_font)
preview_button.pack(pady=20)

# 主预览标签
preview_label = tk.Label(root, text="请选择字体并点击预览。", font=("Arial", 24))
preview_label.pack(pady=20)

# 多种字号的预览标签
sample_sizes = [12, 16, 20, 24]
sample_frame = tk.Frame(root)
sample_frame.pack(pady=10)
sample_labels = []
for sample_size in sample_sizes:
    sample_label = tk.Label(sample_frame, text=f"字体 {sample_size} 号字预览", font=("Arial", sample_size))
    sample_label.pack(pady=5, anchor=tk.W)
    sample_labels.append(sample_label)

# 初始设置窗口大小
root.geometry("600x700")

root.mainloop()