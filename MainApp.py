import tkinter as tk                
from tkinter import font as tkfont  
from PIL import ImageTk,Image
from Pages import StartPage,PageOne,WrongPasswordPage,PageTwo,PageThree,PageFour


class MainMemoApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, WrongPasswordPage,PageTwo,PageThree,PageFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("StartPage")

    def showFrame(self, page_name):
        if page_name == "PageFour":
            self.geometry("740x400")
        elif page_name == "PageTwo" or page_name == "PageOne":
            self.geometry("328x200")
        else:
            self.geometry("328x250")
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainMemoApp()
    app.title("MemoIt Application")
    
    app.mainloop()


