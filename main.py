from cProfile import label
import tkinter as tk
from tkinter import ttk
from tkinter import font

from numpy import pad
import matplotlib.pyplot as plt
import numpy as np

from res.res_manager import AppStrings, FontManager
from tkinter import messagebox

class MainScreen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title(AppStrings.APP_NAME)
        self.iconbitmap("res/logo.ico")
        
            
        self.window_width = 600
        self.window_height = 350

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - self.window_width / 2)
        center_y = int(screen_height/2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        FONT = FontManager.FONT
        largeFont = (FONT, FontManager.FONT_SIZE_20)
        mediumFont = (FONT, FontManager.FONT_SIZE_16)
        smallFont = (FONT, FontManager.FONT_SIZE_14)
        

        welcomeLabel = ttk.Label(self, text=AppStrings.WELCOME_MESSAGE, font=largeFont)
        functionLabel = ttk.Label(self, text=AppStrings.FUNCTION_LABEL, font=mediumFont)
        minXLabel = ttk.Label(self, text=AppStrings.MIN_X_LABEL, font=mediumFont)
        maxXLabel = ttk.Label(self, text=AppStrings.MAX_X_LABEL, font=mediumFont)

        functionEntry = ttk.Entry(self, width=30,font = smallFont)
        minXEntry = ttk.Entry(self, width=30,font = smallFont)
        maxXEntry = ttk.Entry(self, width=30,font = smallFont)



        button = ttk.Button(self, text ="Plot Function",
        command = lambda : self.plot_function(functionEntry.get(), minXEntry.get(), maxXEntry.get()))
          
        # welcomeLabel.pack()
        welcomeLabel.grid(row = 0, column = 3, padx = 10, pady = 10)
        functionLabel.grid(row = 3, column = 2, padx = 10, pady = 10)
        functionEntry.grid(row = 3, column = 3, padx = 10, pady = 10)

        minXLabel.grid(row = 4, column = 2, padx = 10, pady = 10)
        maxXLabel.grid(row = 5, column = 2, padx = 10, pady = 10)

        minXEntry.grid(row = 4, column = 3, padx = 10, pady = 10)
        maxXEntry.grid(row = 5, column = 3, padx = 10, pady = 10)


        button.grid(row = 6, column = 3, padx = 10, pady = 10)

    def plot_function(self, function_str , min_x_str, max_x_str):

        
        try:
            min_x = int(min_x_str.replace(" ",""))
            max_x = int(max_x_str.replace(" ",""))

            function = self.replace_operations_from_string(function_str.strip())
            x = np.linspace(min_x, max_x)
        
            fx  = []

           
            f = lambda x: eval(function)
            for i in x:
                fx.append(f(i))

            plt.figure()
            plt.plot(x , fx) 

            plt.title("F(x) = " + function_str)
            plt.xlabel("X")
            plt.ylabel("Y")

            plt.show()            

        except Exception as e:
            
            messagebox.showerror("Error", "Wront Input")
        
          

    def replace_operations_from_string(self,func):

        func = func.replace(" ","").lower()
        
        op = {
            'sin':'np.sin',
            'cos':'np.cos',
            'tan':'np.tan',
            'log':'np.log',
            'exp':'np.exp',
            'sqrt':'np.sqrt',
            '^':'**',
            'ln':'np.log',
            'pi':'np.pi',
            }
        for i in op:
            func = func.replace(i,op[i])

        return func

 
if __name__ == "__main__":
    MainScreen().mainloop()