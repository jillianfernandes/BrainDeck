import tkinter as tk

def newDeckwindow(new_window):
    label = tk.Label(new_window, 
              text = "New Deck Name: ",
              font = ('Helvetica', 20, 'bold'), 
              fg=  '#e6eaeb', 
              bg = '#252d2e')
    
    label.place(x=20, y= 20)



def viewDeckwindow(new_window):
    label = tk.Label(new_window, 
              text = "Select a deck from below to study:",
              font = ('Helvetica', 20, 'bold'), 
              fg=  '#e6eaeb', 
              bg = '#252d2e')
    
    label.place(x=20, y= 20)

    