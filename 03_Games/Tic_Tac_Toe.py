import tkinter as tk
from tkinter import messagebox  # messagebox is Tkinter module used to display dialog popups.

def check_winner():
    winning_combinations = [

         [0,1,2],   #first row
         [3,4,5],  #second row
         [6,7,8],  #third row
         [0,3,6],  #first column
         [1,4,7],  #second column
         [2,5,8],  #third column
         [0,4,8],  #main diagonal
         [2,4,6]  #another diagonal

    ]
    for combo in winning_combinations :
            # check combo 0, combo 1, combo 2 text are same or not and not considering space 
    
            if buttons[combo[0]]["text"]== buttons[combo[1]]["text"]== buttons[combo[2]]["text"]!="":
               # Change the background color of the three winning buttons to green. 
    
                buttons[combo[0]].config(bg='green')
                buttons[combo[1]].config(bg='green')
                buttons[combo[2]].config(bg='green')

                #.showinfo creates an informational popup with an "OK" button.
                # print Tic_Tac_Toe at the begining of the table 

                messagebox.showinfo("Tic_Tac_Toe", f"player{buttons[combo[0]]['text']} wins!")

                root.quit()

     

def button_cllick(index):

    if buttons[index]["text"] == ""and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()
def toggle_player():
    global current_player
    current_player = "x" if current_player == "o" else "o"
    label.config(text=f"player{current_player}'s turn")

root = tk.Tk()
root.title("Tic_Tac_Toe")
buttons = [tk.Button(root, text="", font=("normal", 50),width=6, height=2, command=lambda i=i: button_cllick(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i %3)
current_player = "x"
winner = False
label = tk.Label(root, text=f"player{current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()