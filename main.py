import tkinter as tk
import subprocess
import settings

def run_program():
    subprocess.run(["python", "hand_tracking.py"])

root = tk.Tk()
root.title('PACMAIN CS')

#creation of a canva
canva = tk.Canvas(root, width=settings.sw, height=settings.sh, bg='blue')
canva.pack()

#add the name of the game
canva.create_text(settings.sw / 2, 50, text="PACMAIN", fill='yellow', font=("Calibri", 50))


#creation of buttons
startbttn = tk.Button(root, text='Start Game', command=run_program, width=15, height=2)

#center coords
x_startbttn = settings.sw / 2
y_startbttn = settings.sh / 2

#place the buttons
canva.create_window(x_startbttn, y_startbttn, window=startbttn)


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Run Program", command=run_program)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()