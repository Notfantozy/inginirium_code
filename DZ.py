import tkinter as tk
win = tk.Tk()
label = tk.Label(win, text='DAMASHKA')
label.pack()
canvas = tk.Canvas(win, bg='#fff', width=400, height=400)
for i in range(50,400,50):
    i = canvas.create_line((0, i), (400, i), fill='blue')
for i in range(50,400,50):
    i = canvas.create_line((i, 0), (i, 400), fill='blue')
canvas.pack()
win.mainloop()