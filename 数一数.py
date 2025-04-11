import tkinter as tk

root = tk.Tk()
root.title('简易计算器')
root.geometry('295x280+100+100')

root.attributes("-alpha", 0.8)  # 设置透明度
root["background"] = "#ffffff"  # 背景颜色
font_20 = ('宋体', 16)
result_num = tk.StringVar()
result_num.set('')

tk.Label(root,
         textvariable=result_num, font=font_20, height=2,
         width=20, justify=tk.LEFT, anchor=tk.SE
         ).grid(row=1, column=1, columnspan=4)
# 第一行
button_clear = tk.Button(root, text='C', width=5, font=font_20, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text='←', width=5, font=font_20, relief=tk.FLAT, bg='#b1b2b2')
button_division = tk.Button(root, text='/', width=5, font=font_20, relief=tk.FLAT, bg='#b1b2b2')
button_multiplication = tk.Button(root, text='x', width=5, font=font_20, relief=tk.FLAT, bg='#b1b2b2')
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_division.grid(row=2, column=3, padx=4, pady=2)
button_multiplication.grid(row=2, column=4, padx=4, pady=2)

# 第二行
button_seven = tk.Button(root, text='7', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_eight = tk.Button(root, text='8', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_nine = tk.Button(root, text='9', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_subtraction = tk.Button(root, text='-', width=5, font=font_20, relief=tk.FLAT, bg='#b1b2b2')
button_seven.grid(row=3, column=1, padx=4, pady=2)
button_eight.grid(row=3, column=2, padx=4, pady=2)
button_nine.grid(row=3, column=3, padx=4, pady=2)
button_subtraction.grid(row=3, column=4, padx=4, pady=2)
# 第三行
button_four = tk.Button(root, text='4', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_five = tk.Button(root, text='5', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_six = tk.Button(root, text='6', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_addition = tk.Button(root, text='+', width=5, font=font_20, relief=tk.FLAT, bg='#b1b2b2')
button_four.grid(row=4, column=1, padx=4, pady=2)
button_five.grid(row=4, column=2, padx=4, pady=2)
button_six.grid(row=4, column=3, padx=4, pady=2)
button_addition.grid(row=4, column=4, padx=4, pady=2)

# 第四行
button_one = tk.Button(root, text='1', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_two = tk.Button(root, text='2', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_there = tk.Button(root, text='3', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_equal = tk.Button(root, text='=', width=5, height=3, font=font_20, relief=tk.FLAT, bg='#b1b2b2')
button_one.grid(row=5, column=1, padx=4, pady=2)
button_two.grid(row=5, column=2, padx=4, pady=2)
button_there.grid(row=5, column=3, padx=4, pady=2)
button_equal.grid(row=5, column=4, padx=4, pady=2, rowspan=2)

# 第五行
button_zero = tk.Button(root, text='0', width=12, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_dot = tk.Button(root, text='.', width=5, font=font_20, relief=tk.FLAT, bg='#eacda1')
button_zero.grid(row=6, column=1, padx=4, pady=2, columnspan=2)
button_dot.grid(row=6, column=3, padx=4, pady=2)


# 事件行动
def click_button(x):
    result_num.set(result_num.get() + x)


def clear():
    result_num.set('')


def back():
    current_text = result_num.get()
    if current_text:
        result_num.set(current_text[:-1])


def calculation():
    opt_str = result_num.get()
    try:
        result = eval(opt_str)
        result_num.set(str(result))
    except Exception as e:
        result_num.set("Error")


button_one.config(command=lambda: click_button('1'))
button_two.config(command=lambda: click_button('2'))
button_there.config(command=lambda: click_button('3'))
button_four.config(command=lambda: click_button('4'))
button_five.config(command=lambda: click_button('5'))
button_six.config(command=lambda: click_button('6'))
button_seven.config(command=lambda: click_button('7'))
button_eight.config(command=lambda: click_button('8'))
button_nine.config(command=lambda: click_button('9'))
button_zero.config(command=lambda: click_button('0'))
button_addition.config(command=lambda: click_button('+'))
button_subtraction.config(command=lambda: click_button('-'))
button_multiplication.config(command=lambda: click_button('*'))
button_division.config(command=lambda: click_button('/'))
button_dot.config(command=lambda: click_button('.'))
button_clear.config(command=clear)
button_back.config(command=back)
button_equal.config(command=calculation)

root.mainloop()
#pyinstaller - F - w - -icon = "D:\素材\R.jpg"数一数.py