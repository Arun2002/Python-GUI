from tkinter import *
from tkinter import messagebox
from tkinter import ttk


if __name__ != "__main__":

    class Main(Tk):
        #Functions 0f main ---------------------------------
        def __init__(self , root_main):
            # main buttons:
            self.button1_main = Button(root_main, text="Sign up")
            self.button2_main = Button(root_main, text="Login in", )
            self.button3_main = Button(root_main, text="Quit", command=self.quit_main)

            # main label :

            self.label1_main = Label(root_main, text="Face pack")
            self.label1_main.grid(row=1, padx=30, pady=10)

            self.button1_main.grid(row=0, column=4, padx=20, pady=10)
            self.button2_main.grid(row=0, column=5, padx=20, pady=10)
            self.button3_main.grid(row=5, column=3, pady=100, padx=10)

        def quit_main(self):
            self.m = messagebox.askquestion("Alert!" , "Are you Sure you want to exit" ,icon = "warning")
            if self.m == "yes":
                quit()

    r_main = Main()
    Main.mainloop(r_main)

