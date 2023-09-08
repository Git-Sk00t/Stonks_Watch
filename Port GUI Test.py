from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ticker1 = "AAPL"
ticker2 = "GOGL"
ticker3 = "NIO"
ticker4 = ""
ticker5 = ""
ticker6 = ""
ticker7 = ""
ticker8 = ""
ticker9 = ""
ticker10 = ""

t1p = int("15")
t2p = int("70")
t3p = int("32")

t1s = int("10")
t2s = int("42")
t3s = int("91")

t1value= t1p * t1s
t2value= t2p * t2s
t3value= t3p * t3s


class Top3Frame(ctk.CTkFrame):
    def __init__(self,*args,header_name="top3frame",**kwargs):
        super().__init__(*args,**kwargs)
        
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)

        self.toplabel = ctk.CTkLabel(self,text="Top 3 Movers",font=ctk.CTkFont(size=85,weight="bold"))
        self.toplabel.grid(row=0,column=1,padx=1,pady=0,sticky="N")

        self.ticker1lable = ctk.CTkLabel(self, text=f"{ticker1}",font=ctk.CTkFont(size=50,weight="bold"))
        self.ticker1lable.grid(row=1,column=0,padx=1,pady=1,sticky="EW")
        self.ticker1percent = ctk.CTkLabel(self, text=f" {t1p}%",font=ctk.CTkFont(size=35))
        self.ticker1percent.grid(row=2,column=0,padx=1,pady=1)
        self.ticker1shareprice = ctk.CTkLabel(self, text=f"Share price is ${t1p}",font=ctk.CTkFont(size=35))
        self.ticker1shareprice.grid(row=3,column=0,padx=1,pady=1)
        self.ticker1value = ctk.CTkLabel(self,text=f"Current value is ${t1value}",font=ctk.CTkFont(size=35))
        self.ticker1value.grid(row=4,column=0,padx=1,pady=1)

        self.ticker2lable = ctk.CTkLabel(self,text=f"{ticker2}",font=ctk.CTkFont(size=50,weight="bold"))
        self.ticker2lable.grid(row=1,column=1,padx=1,pady=1,sticky="EW") 
        self.ticker2percent = ctk.CTkLabel(self, text=f" {t2p}%",font=ctk.CTkFont(size=35))
        self.ticker2percent.grid(row=2,column=1,padx=1,pady=1)
        self.ticker2shareprice = ctk.CTkLabel(self,text=f"Share price is ${t2p}",font=ctk.CTkFont(size=35))
        self.ticker2shareprice.grid(row=3,column=1,padx=1,pady=1)
        self.ticker2value = ctk.CTkLabel(self,text=f"Current value is ${t2value}",font=ctk.CTkFont(size=35))
        self.ticker2value.grid(row=4,column=1,padx=1,pady=1)

        self.ticker3lable = ctk.CTkLabel(self,text=f"{ticker3}",font=ctk.CTkFont(size=50,weight="bold"))
        self.ticker3lable.grid(row=1,column=2,padx=1,pady=1,sticky="EW")
        self.ticker3percent = ctk.CTkLabel(self, text=f" {t3p}%",font=ctk.CTkFont(size=35))
        self.ticker3percent.grid(row=2,column=2,padx=1,pady=1)
        self.ticker3shareprice = ctk.CTkLabel(self,text=f"Share price is ${t3p}",font=ctk.CTkFont(size=35))
        self.ticker3shareprice.grid(row=3,column=2,padx=1,pady=1)
        self.ticker3value = ctk.CTkLabel(self,text=f"Current value is ${t3value}",font=ctk.CTkFont(size=35))
        self.ticker3value.grid(row=4,column=2,padx=1,pady=1)


#Actual app itself
class App(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)
        self.grid_rowconfigure(6,weight=1)
        self.grid_rowconfigure(7,weight=1)
        self.grid_rowconfigure(8,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        self.grid_columnconfigure(5,weight=1)
        self.grid_columnconfigure(6,weight=1)
        self.grid_columnconfigure(7,weight=1)
        self.grid_columnconfigure(8,weight=1)

        self.top3frame = Top3Frame(self)
        self.top3frame.grid(row=0,column=0,padx=0,pady=0)
        




#Runs the program
if __name__ == "__main__":
    app = App()
    app.mainloop()


