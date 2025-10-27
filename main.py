import tkinter as tk

last_x = None
last_y = None
current_color = "white"
current_width = 4

def start_drawing(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y,
                            fill=current_color,
                            width=current_width,
                            capstyle=tk.ROUND,
                            smooth=True)
        last_x = event.x
        last_y = event.y

def stop_drawing(event):
    global last_x, last_y
    last_x = None
    last_y = None

def erase(event):
    global current_color, current_width
    current_width = 20
    current_color = "white"
    root.title("Pim (Erase Mode)")


def pen(event):
    global current_color, current_width
    current_color = "black"
    current_width = 4
    root.title("Pim (Pen Mode)")

def add(event):
    global current_width
    current_width += 1
    update_width()

def minus(event):
    global current_width
    if current_width > 1:
        current_width -= 1
    update_width()

def update_width():
    width_label.config(text=f"Width: {current_width}")

root = tk.Tk()
root.title("Pim")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(fill="both", expand=True)

width_label = tk.Label(root, text=f"Width: {current_width}", font=("Arial", 12), bg="lightgrey", padx=5, pady=2)
width_label.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor='se')

root.iconbitmap('C:/source/repos/MS-Paint-clone/paintbrush.ico')

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.bind("<e>", erase, update_width())
root.bind("<p>", pen, update_width())
root.bind("<plus>", add)
root.bind("<minus>", minus)

root.mainloop()