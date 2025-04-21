import tkinter as tk
from tkinter import ttk
import numpy as np

# Logistic regression coefficients (from your model)
b0 = -0.0457
b_ldl = -0.0131
b_estat = 0.0433
b_interact = -0.0067

def calculate_probability(ldl, estatinas):
    interaction = ldl * estatinas
    logit_p = b0 + b_ldl * ldl + b_estat * estatinas + b_interact * interaction
    probability = 1 / (1 + np.exp(-logit_p))
    return probability

def on_calculate():
    ldl = float(ldl_entry.get())
    estatinas = estatinas_var.get()
    prob = calculate_probability(ldl, estatinas)
    result_label.config(text=f"Predicted Probability: {prob*100:.1f}%")

# GUI setup
root = tk.Tk()
root.title("LDL < 55 Risk Calculator")

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

ttk.Label(frame, text="LDL (mg/dL):").grid(column=0, row=0, sticky=tk.W)
ldl_entry = ttk.Entry(frame)
ldl_entry.insert(0, "100")
ldl_entry.grid(column=1, row=0)

estatinas_var = tk.IntVar()
ttk.Label(frame, text="Statins in use:").grid(column=0, row=1, sticky=tk.W)
statin_check = ttk.Checkbutton(frame, text="Yes", variable=estatinas_var)
statin_check.grid(column=1, row=1, sticky=tk.W)

ttk.Button(frame, text="Calculate", command=on_calculate).grid(column=0, row=2, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=3, columnspan=2)

root.mainloop()
