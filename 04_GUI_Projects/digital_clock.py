"""import the tkinter library.
 Tkinter is used to create graphical user interfaces (GUI)."""

import tkinter as tk #enable GUI 
from time import strftime

root= tk.Tk() #makking a root windows where the time shows, Tk() creates the root window of the application.
root.title("Digital Clock")

def time():
    """Get the current time and date in the required format.
    %H = Hour in 24-hour format (00-23).
     %M = Minutes (00-59).
     %S = Seconds (00-59).
     %p = AM or PM.
     \n = Move the date to the next line.
     %D = Date in MM/DD/YY format."""

    
    string= strftime('%H:%M:%S %p \n %D')

    # Update the text displayed on the label with the current time and date.
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()

root.mainloop()

    