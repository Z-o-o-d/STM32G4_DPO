import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageDraw, ImageFont

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

def search_fonts(event=None):
    keyword = search_entry.get().lower()
    # 先删除 Treeview 中的所有项
    for item in tree.get_children():
        tree.delete(item)
    # 重新插入符合条件的项
    for font_name, font_obj in font_fonts.items():
        if keyword in font_name.lower():
            tree.insert("", "end", text=font_name, tags=(font_name,))
            tree.tag_configure(font_name, font=font_obj)

def generate_c_code():
    try:
        selected_item = tree.selection()
        if not selected_item:
            result_text.insert(tk.END, "请选择字体。\n")
            return
        selected_font_name = tree.item(selected_item, "text")
        selected_size = size_var.get()
        characters = char_entry.get()
        if not characters:
            result_text.insert(tk.END, "请输入要生成的字符。\n")
            return
        width = int(width_entry.get())
        height = int(height_entry.get())

        # 使用 PIL 生成字体位图
        c_code = f"static const uint16_t Font{width}x{height} [] = {{\n"
        for char in characters:
            img = Image.new('1', (width, height), color=0)
            draw = ImageDraw.Draw(img)
            pil_font = ImageFont.truetype(selected_font_name, selected_size)
            draw.text((0, 0), char, font=pil_font, fill=1)
            row_data = []
            for y in range(height):
                value = 0
                for x in range(width):
                    value |= img.getpixel((x, y)) << (width - 1 - x)
                row_data.append(f"0x{value:04X}")
            c_code += ", ".join(row_data) + ",  // " + char + "\n"
        c_code += "};"
        result_text.insert(tk.END, c_code + "\n")
    except Exception as e:
        result_text.insert(tk.END, f"生成 C 代码时出错: {str(e)}\n")

root = tk.Tk()
root.title("字体选择与预览及 C 代码生成")

# 获取系统所有字体
all_fonts = font.families()

# 创建样式对象并设置 Treeview 的行高
style = ttk.Style()
style.configure("Custom.Treeview", rowheight=30)  # 调整行高，可根据需要修改值

# 创建搜索框
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=10)
# 绑定输入框的按键释放事件
search_entry.bind("<<KeyRelease>>", search_fonts)

# 创建 Treeview 来替代 Listbox
tree = ttk.Treeview(root, columns=("Fonts"), show="tree", style="Custom.Treeview")
tree.column("Fonts", width=400)
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# 存储所有字体名称和对应的字体对象
font_fonts = {}

# 将字体添加到 Treeview 并设置对应字体样式
for font_name in all_fonts:
    try:
        # 尝试创建字体对象
        font_obj = font.Font(family=font_name, size=14)
        tree.insert("", "end", text=font_name, tags=(font_name,))
        font_fonts[font_name] = font_obj
        tree.tag_configure(font_name, font=font_obj)
    except tk.TclError:
        # 若字体不支持则以默认字体显示
        default_font = font.Font(size=14)
        tree.insert("", "end", text=font_name, tags=("default",))
        font_fonts[font_name] = default_font
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

# 输入要生成的字符
char_frame = tk.Frame(root)
char_frame.pack(pady=10)
char_label = tk.Label(char_frame, text="要生成的字符:")
char_label.pack(side=tk.LEFT, padx=10)
char_entry = tk.Entry(char_frame, width=30)
char_entry.pack(side=tk.LEFT, padx=10)

# 输入字体尺寸
size_input_frame = tk.Frame(root)
size_input_frame.pack(pady=10)
width_label = tk.Label(size_input_frame, text="宽度:")
width_label.pack(side=tk.LEFT, padx=10)
width_entry = tk.Entry(size_input_frame, width=5)
width_entry.insert(0, "7")
width_entry.pack(side=tk.LEFT, padx=10)
height_label = tk.Label(size_input_frame, text="高度:")
height_label.pack(side=tk.LEFT, padx=10)
height_entry = tk.Entry(size_input_frame, width=5)
height_entry.insert(0, "10")
height_entry.pack(side=tk.LEFT, padx=10)

# 生成 C 代码按钮
generate_button = tk.Button(root, text="生成 C 代码", command=generate_c_code)
generate_button.pack(pady=20)

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

# 显示生成的 C 代码
result_text = tk.Text(root, height=10, width=60)
result_text.pack(pady=20)

# 初始设置窗口大小
root.geometry("800x900")

root.mainloop()