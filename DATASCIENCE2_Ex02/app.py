import numpy as np
import sys
import os
import tkinter as tk
sys.path.append(os.path.join(f"{os.path.dirname(__file__)}", "utils"))

from utils.random_number import generate_random_number
from utils.make_array import array_generator
from utils.identify import win_fail


# function for check button
def check_num():
    n = int(entry.get())
    array = array_generator(n)
    label_result2.config(text=f"{array}")
    label_result4.config(text=f"{max(array)}")

    if win_fail(array)=="Win":
        label_result.config(text= win_fail(array), fg="green2", font=44)
    else:
        label_result.config(text= win_fail(array), fg="red2", font=44)




# window
window = tk.Tk()
window.title("تمرین 2")
window.geometry("500x500")

# title
title_label = tk.Label(master=window, text="(numpy) تمرین دوم پایتون", font="calibri 24 bold")
title_label.pack(pady=15)

# input field
note = tk.Label(master=window, text=":لطفا یک عدد بین 0 تا 100 وارد کنید", font="calibri 14", justify="right")
note.pack(anchor='e',pady=15)


frame = tk.Frame(master=window)
frame.pack()

# Create an entry
entry = tk.Entry(frame)
entry.pack(side="left", padx=10)

# Create a button to submit the guess
button_guess = tk.Button(frame, text="Check", bg="lightskyblue1", command=check_num)
button_guess.pack()


# Create a label for results
label_result = tk.Label(window)
label_result.pack(pady=20)

label_result1 = tk.Label(window, text=":لیست اعداد", font="calibri")
label_result1.pack(pady=5)

label_result2 = tk.Label(window)
label_result2.pack(pady=5)

label_result3 = tk.Label(window, text=":بزرگترین عدد", font="calibri")
label_result3.pack(pady=5)

label_result4 = tk.Label(window)
label_result4.pack(pady=5)

# Button for exit 
exit_button = tk.Button(window, text="خروج", bg="tomato", command=window.destroy) 
exit_button.pack(pady=10) 

window.mainloop()


