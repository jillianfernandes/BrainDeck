import tkinter as tk
from welcome import newDeckwindow 
from welcome import viewDeckwindow

# creates new window when new deck button is pushed
def new_deck(window):
    new_window = tk.Toplevel()
    new_window.title("New Deck")
    new_window.geometry("600x300")
    new_window.config(background = "#252d2e")
    newDeckwindow(new_window)
    
    new_window.mainloop()
    window.destroy()
    
#creates new window when view decks button is pushed 
def view_decks(window):
    new_window = tk.Toplevel()
    new_window.title("View Decks")
    new_window.geometry("600x300")
    new_window.config(background = "#252d2e")
    viewDeckwindow(new_window)

    new_window.mainloop()

#instantiate instance of a window
window = tk.Tk()
window.geometry("600x300")
window.title("BrainDeck")

#setting icon image
icon = tk.PhotoImage(file ='bulb.png')
window.iconphoto(True, icon)

window.config(background = "#252d2e")

#Creating label 
label = tk.Label(window, 
              text = "Welcome to BrainDeck!",
              font = ('Helvetica', 30, 'bold'), 
              fg=  '#e6eaeb', 
              bg = '#252d2e')
label.place(x=120, y= 20)

#Adding New Deck Button 
newDeck = tk.Button(window, text = 'Create New Deck')
newDeck.config(command= lambda: new_deck(window))
newDeck.config(font = ('Helvetica', 50, 'bold'))
newDeck.config(bg = '#e6eaeb')
newDeck.config(fg = '#252d2e')
newDeck.config(activebackground = '#cff4ff')
newDeck.config(activeforeground= '#252d2e')

newDeck.place(x = 80, y = 80)

# Adding View Deck Button 
viewDeck = tk.Button(window, text = ' View Old Decks ')
viewDeck.config(command= lambda: view_decks(window))
viewDeck.config(font = ('Helvetica', 50, 'bold'))
viewDeck.config(bg = '#e6eaeb')
viewDeck.config(fg = '#252d2e')
viewDeck.config(activebackground = '#cff4ff')
viewDeck.config(activeforeground= '#252d2e')

viewDeck.place(x = 82, y = 200)

#place window on coputer screen, listen for events 
window.mainloop() 