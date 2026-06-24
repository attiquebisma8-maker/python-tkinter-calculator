import tkinter as tk

# window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# display
entry = tk.Entry(window, font=("Arial", 20))
entry.pack(pady=20)

# functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(window)
frame.pack()

row = 0
col = 0

for button in buttons:
    if button == "=":
        tk.Button(frame, text=button, width=8, height=3,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(frame, text=button, width=8, height=3,
                  command=lambda x=button: click(x)).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1

# clear button
tk.Button(window, text="Clear", width=20, height=2,
          command=clear).pack(pady=10)

window.mainloop()