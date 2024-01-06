import sys
import os
import tkinter as tk
import random

# Generate a random number between 1 and 100
LOWER = 1
UPPER = 100
computer_number = random.randint(LOWER, UPPER)

# Initialize the number of guesses
guess_limit = 5
guess_count = 0

# Define a function to check the user's guess
def check_guess():
    global guess_count
    guess_count += 1
    guess_left = guess_limit - guess_count

    # Get the user's guess from the entry widget
    try:
        user_guess = int(entry_guess.get())
        if user_guess > 100 or user_guess < 1:
            label_result.config(text="Please enter a NUMBER (1-100)!")
            entry_guess.delete(0, tk.END)
            
    except ValueError:
        label_result.config(text='Please enter a NUMBER (1-100)!')
        entry_guess.delete(0, tk.END)
        
    
    # Compare the guess to the secret number
    if user_guess == computer_number:
        label_result.config(text="hooooooorrraaa! You've guessed the number!", fg="maroon1")
        button_guess.config(text='تمام')
        button_guess.config(state=tk.DISABLED)
        entry_guess.config(state=tk.DISABLED)

    elif guess_count == guess_limit or guess_left<0:
        label_result.config(text=f"Sorry, no more guesses. The number was {computer_number}.", fg="red2", font="24")
        button_guess.config(text='تمام')
        button_guess.config(state=tk.DISABLED)
        entry_guess.config(state=tk.DISABLED)

    elif user_guess < computer_number:
        label_result.config(text=f"Your number is smaller! You have {guess_left} guesses left.")
    else:
        label_result.config(text=f"Your number is bigger! You have {guess_left} guesses left.")
    
    # Clear the entry for the next guess
    entry_guess.delete(0, tk.END)


# window
window = tk.Tk()
window.title("بازی بزرگ حدس اعداد")
window.geometry("500x300")

# title
title_label = tk.Label(master=window, text="بازی بزرگ حدس اعداد", font="calibri 24 bold")
title_label.pack(pady=10)

# input field
note = tk.Label(master=window, text=":لطفا یک عدد بین 1 تا 100 وارد کنید", font="calibri 14", justify="right")
note.pack(anchor='e')


frame = tk.Frame(master=window)
frame.pack()

# Create an entry
entry_guess = tk.Entry(frame)
entry_guess.pack(side="left", padx=10)

# Create a button to submit the guess
button_guess = tk.Button(frame, text="حدس بزن", bg="lightgreen", command=check_guess)
button_guess.pack()


# Create a label for results
label_result = tk.Label(window)
label_result.pack(pady=20)

# Button for exit 
exit_button = tk.Button(window, text="خروج", bg="tomato", command=window.destroy) 
exit_button.pack() 

window.mainloop()