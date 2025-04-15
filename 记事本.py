import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import os


class Notepad:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("记事本")
        self.root.geometry("800x600")
        self.current_file = None
        self.bg_image = None
        self.current_bg_path = None

        self.create_menu()

        self.canvas = tk.Canvas(self.root)#创建一个 Canvas（画布）组件，用于绘制背景图片和放置文本框。
        self.canvas.pack(fill=tk.BOTH, expand=True)#将画布置于窗口中，并设置其填充方式为水平和垂直填充，同时允许画布随窗口大小变化而扩展

        self.text = tk.Text(self.canvas, wrap=tk.WORD)
        self.text_window = self.canvas.create_window(0, 0, window=self.text, anchor=tk.NW, tags="text_window")

        self.canvas.bind("<Configure>", self.on_canvas_resize)
        self.set_background_color('#FFFFFF')

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.root.mainloop()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="新建", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="打开", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="保存", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="另存为", accelerator="Ctrl+Shift+S", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="退出", accelerator="Alt+F4", command=self.on_exit)
        menubar.add_cascade(label="文件", menu=file_menu)

        # 背景菜单
        bg_menu = tk.Menu(menubar, tearoff=0)
        bg_menu.add_command(label="更换背景图片", command=self.change_background_image)
        bg_menu.add_command(label="设置背景颜色", command=self.choose_background_color)
        bg_menu.add_command(label="设置文字颜色", command=self.set_text_color)
        menubar.add_cascade(label="背景", menu=bg_menu)

        self.root.config(menu=menubar)

        # 快捷键绑定
        self.root.bind_all("<Control-n>", lambda e: self.new_file())
        self.root.bind_all("<Control-o>", lambda e: self.open_file())
        self.root.bind_all("<Control-s>", lambda e: self.save_file())
        self.root.bind_all("<Control-Shift-S>", lambda e: self.save_as())

    def on_canvas_resize(self, event):
        self.canvas.itemconfig(self.text_window, width=event.width, height=event.height)
        if self.bg_image:
            self.resize_background_image(event.width, event.height)

    def resize_background_image(self, width, height):
        try:
            image = Image.open(self.current_bg_path)
            image = image.resize((width, height), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(image)
            self.canvas.delete("bg_image")
            self.canvas.create_image(0, 0, image=self.bg_image, anchor=tk.NW, tags="bg_image")
            self.canvas.lift("text_window")
        except Exception as e:
            messagebox.showerror("错误", f"调整图片大小失败：{e}")

    def change_background_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("图片文件", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        if file_path:
            self.current_bg_path = file_path
            try:
                self.set_background_color('')  # 清除背景颜色
                self.resize_background_image(self.canvas.winfo_width(), self.canvas.winfo_height())
            except Exception as e:
                messagebox.showerror("错误", f"加载图片失败：{e}")

    def choose_background_color(self):
        color_tuple = colorchooser.askcolor(title="选择背景颜色")
        if color_tuple and color_tuple:  # 正确处理颜色选择返回值
            self.set_background_color(color_tuple)

    def set_background_color(self, color):
        # 清除背景图片
        self.canvas.delete("bg_image")
        self.current_bg_path = None
        self.bg_image = None

        # 设置新颜色
        self.canvas.config(bg=color)
        self.text.config(bg=color)

    def set_text_color(self):
        color_tuple = colorchooser.askcolor(title="选择文字颜色")
        if color_tuple and color_tuple:  # 正确提取十六进制颜色值
            self.text.config(fg=color_tuple)

    # 文件操作方法
    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.current_file = None

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("文本文档", "*.txt"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    self.text.delete(1.0, tk.END)
                    self.text.insert(tk.INSERT, file.read())
                self.current_file = file_path
            except Exception as e:
                messagebox.showerror("错误", f"打开文件失败：{e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding='utf-8') as file:
                    file.write(self.text.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("错误", f"保存文件失败：{e}")
        else:
            self.save_as()

    def save_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("文本文档", "*.txt"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding='utf-8') as file:
                    file.write(self.text.get(1.0, tk.END))
                self.current_file = file_path
            except Exception as e:
                messagebox.showerror("错误", f"另存为失败：{e}")

    def on_exit(self):
        if messagebox.askokcancel("退出", "确定要退出吗？"):
            self.root.destroy()


if __name__ == "__main__":
    Notepad()
# pyinstaller -F -w --icon="D:\素材\pai.jpeg" 记事本.py
