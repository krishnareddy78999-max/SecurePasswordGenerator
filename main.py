import tkinter as tk
from tkinter import messagebox
import itertools
import time
import re

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Secure Password Generation System")
root.geometry("900x650")
root.config(bg="#0f172a")

# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="Secure Password Generation System",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="cyan"
)

title.pack(pady=20)

# ---------------- INPUT FRAME ---------------- #

input_frame = tk.Frame(root, bg="#0f172a")
input_frame.pack(pady=10)

input_label = tk.Label(
    input_frame,
    text="Enter Characters:",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="white"
)

input_label.grid(row=0, column=0, padx=10)

entry = tk.Entry(
    input_frame,
    font=("Arial", 14),
    width=30,
    bd=3
)

entry.grid(row=0, column=1, padx=10)

# ---------------- OUTPUT AREA ---------------- #

output_text = tk.Text(
    root,
    height=18,
    width=80,
    font=("Consolas", 11),
    bg="#1e293b",
    fg="white",
    insertbackground="white"
)

output_text.pack(pady=20)

# ---------------- PASSWORD STRENGTH LABEL ---------------- #

strength_label = tk.Label(
    root,
    text="Strength: ",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="yellow"
)

strength_label.pack(pady=5)

# ---------------- TIME LABEL ---------------- #

time_label = tk.Label(
    root,
    text="Execution Time: ",
    font=("Arial", 12, "bold"),
    bg="#0f172a",
    fg="lightgreen"
)

time_label.pack(pady=5)

# ---------------- FUNCTIONS ---------------- #

# BACKTRACKING FUNCTION
def backtrack(chars, path, used, result):

    if len(path) == len(chars):
        result.append("".join(path))
        return

    for i in range(len(chars)):

        if used[i]:
            continue

        used[i] = True
        path.append(chars[i])

        backtrack(chars, path, used, result)

        path.pop()
        used[i] = False


# GENERATE USING BACKTRACKING
def generate_backtracking():

    chars = entry.get()

    if chars == "":
        messagebox.showerror("Error", "Please enter characters")
        return

    output_text.delete(1.0, tk.END)

    result = []

    start = time.time()

    used = [False] * len(chars)

    backtrack(list(chars), [], used, result)

    end = time.time()

    for item in result:
        output_text.insert(tk.END, item + "\n")

    output_text.insert(
        tk.END,
        f"\nTotal Permutations: {len(result)}"
    )

    execution_time = end - start

    time_label.config(
        text=f"Execution Time: {execution_time:.6f} seconds"
    )


# GENERATE USING BRUTE FORCE
def generate_bruteforce():

    chars = entry.get()

    if chars == "":
        messagebox.showerror("Error", "Please enter characters")
        return

    output_text.delete(1.0, tk.END)

    start = time.time()

    perms = itertools.permutations(chars)

    count = 0

    for p in perms:
        password = "".join(p)
        output_text.insert(tk.END, password + "\n")
        count += 1

    end = time.time()

    output_text.insert(
        tk.END,
        f"\nTotal Permutations: {count}"
    )

    execution_time = end - start

    time_label.config(
        text=f"Execution Time: {execution_time:.6f} seconds"
    )


# PASSWORD STRENGTH CHECKER
def check_password_strength():

    password = entry.get()

    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1

    # Digit Check
    if re.search(r"[0-9]", password):
        score += 1

    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=<>?/]", password):
        score += 1

    # RESULT
    if score <= 2:
        result = "Weak Password"
        color = "red"

    elif score == 3 or score == 4:
        result = "Medium Password"
        color = "orange"

    else:
        result = "Strong Password"
        color = "lightgreen"

    strength_label.config(
        text=f"Strength: {result}",
        fg=color
    )


# SAVE PASSWORDS TO FILE
def save_to_file():

    data = output_text.get(1.0, tk.END)

    if data.strip() == "":
        messagebox.showwarning(
            "Warning",
            "No passwords generated"
        )
        return

    with open("passwords.txt", "w") as file:
        file.write(data)

    messagebox.showinfo(
        "Saved",
        "Passwords saved to passwords.txt"
    )


# CLEAR OUTPUT
def clear_output():

    output_text.delete(1.0, tk.END)

    strength_label.config(
        text="Strength: ",
        fg="yellow"
    )

    time_label.config(
        text="Execution Time: "
    )


# ---------------- BUTTON FRAME ---------------- #

button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(pady=20)

# BACKTRACK BUTTON
backtrack_btn = tk.Button(
    button_frame,
    text="Backtracking",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=generate_backtracking
)

backtrack_btn.grid(row=0, column=0, padx=10)

# BRUTE FORCE BUTTON
bruteforce_btn = tk.Button(
    button_frame,
    text="Brute Force",
    font=("Arial", 12, "bold"),
    bg="#16a34a",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=generate_bruteforce
)

bruteforce_btn.grid(row=0, column=1, padx=10)

# CHECK STRENGTH BUTTON
strength_btn = tk.Button(
    button_frame,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="#9333ea",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=check_password_strength
)

strength_btn.grid(row=0, column=2, padx=10)

# SAVE BUTTON
save_btn = tk.Button(
    button_frame,
    text="Save to File",
    font=("Arial", 12, "bold"),
    bg="#ea580c",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=save_to_file
)

save_btn.grid(row=0, column=3, padx=10)

# CLEAR BUTTON
clear_btn = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#dc2626",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=clear_output
)

clear_btn.grid(row=0, column=4, padx=10)

# ---------------- RUN APPLICATION ---------------- #

root.mainloop()