from tkinter import *
app = Tk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.title(".")
app.geometry("30x30+200+600")
app.wm_attributes("-alpha",0.5)
app.overrideredirect(True)
app.resizable(False, False)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    app.geometry("30x30+{}+{}".format(x,y))

app.bind('<Motion>', motion)

app.mainloop()
