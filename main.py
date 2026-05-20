import tkinter as tk
from tkinter import ttk, messagebox
import time

# =====================================================
# PERMUTATION ALGORITHMS
# =====================================================

# Backtracking Algorithm
def backtrack_permutations(chars, start, result):

    if start == len(chars):
        result.append(''.join(chars))
        return

    for i in range(start, len(chars)):

        # Swap
        chars[start], chars[i] = chars[i], chars[start]

        # Recursive Call
        backtrack_permutations(chars, start + 1, result)

        # Backtrack
        chars[start], chars[i] = chars[i], chars[start]


# Brute Force Recursive Algorithm
def brute_force_permutations(prefix, remaining, result):

    if len(remaining) == 0:
        result.append(prefix)
        return

    for i in range(len(remaining)):

        brute_force_permutations(
            prefix + remaining[i],
            remaining[:i] + remaining[i+1:],
            result
        )

# =====================================================
# GUI FUNCTIONS
# =====================================================

def generate_permutations():

    input_string = entry.get()

    # Validation
    if input_string == "":
        messagebox.showerror("Error", "Please enter characters")
        return

    if len(set(input_string)) != len(input_string):
        messagebox.showerror("Error", "Enter unique characters only")
        return

    if len(input_string) > 8:
        messagebox.showerror(
            "Error",
            "Input too large.\nUse maximum 8 characters."
        )
        return

    result = []

    algorithm = algo_var.get()

    start_time = time.time()

    # Algorithm Selection
    if algorithm == "Backtracking":

        backtrack_permutations(
            list(input_string),
            0,
            result
        )

    elif algorithm == "Brute Force":

        brute_force_permutations(
            "",
            input_string,
            result
        )

    end_time = time.time()

    execution_time = end_time - start_time

    # Clear Previous Output
    output_text.delete(1.0, tk.END)

    # Display Permutations
    for perm in result:
        output_text.insert(tk.END, perm + "\n")

    # Update Statistics
    count_label.config(
        text=f"Total Permutations: {len(result)}"
    )

    time_label.config(
        text=f"Execution Time: {execution_time:.6f} sec"
    )


def clear_all():

    entry.delete(0, tk.END)

    output_text.delete(1.0, tk.END)

    count_label.config(
        text="Total Permutations: 0"
    )

    time_label.config(
        text="Execution Time: 0 sec"
    )

# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()

root.title("Secure Password Generation System")

root.geometry("850x650")

root.configure(bg="#0f172a")

# =====================================================
# TITLE SECTION
# =====================================================

title = tk.Label(
    root,
    text="🔐 Secure Password Generation System",
    font=("Helvetica", 22, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Permutation Generation using Backtracking & Brute Force",
    font=("Arial", 11),
    bg="#0f172a",
    fg="white"
)

subtitle.pack()

# =====================================================
# INPUT FRAME
# =====================================================

input_frame = tk.Frame(
    root,
    bg="#1e293b",
    bd=2,
    relief=tk.RIDGE
)

input_frame.pack(
    pady=20,
    padx=20,
    fill="x"
)

input_label = tk.Label(
    input_frame,
    text="Enter Characters:",
    font=("Arial", 13, "bold"),
    bg="#1e293b",
    fg="white"
)

input_label.grid(
    row=0,
    column=0,
    padx=15,
    pady=15
)

entry = tk.Entry(
    input_frame,
    font=("Consolas", 14),
    width=30,
    bd=3,
    relief=tk.GROOVE
)

entry.grid(
    row=0,
    column=1,
    padx=10
)

# =====================================================
# ALGORITHM SELECTION
# =====================================================

algo_label = tk.Label(
    input_frame,
    text="Select Algorithm:",
    font=("Arial", 13, "bold"),
    bg="#1e293b",
    fg="white"
)

algo_label.grid(
    row=1,
    column=0,
    padx=15,
    pady=10
)

algo_var = tk.StringVar()

algo_dropdown = ttk.Combobox(
    input_frame,
    textvariable=algo_var,
    values=["Backtracking", "Brute Force"],
    state="readonly",
    font=("Arial", 11),
    width=27
)

algo_dropdown.grid(
    row=1,
    column=1,
    pady=10
)

algo_dropdown.current(0)

# =====================================================
# BUTTONS
# =====================================================

button_frame = tk.Frame(
    root,
    bg="#0f172a"
)

button_frame.pack(pady=15)

generate_btn = tk.Button(
    button_frame,
    text="Generate Passwords",
    font=("Arial", 12, "bold"),
    bg="#22c55e",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=generate_permutations
)

generate_btn.grid(
    row=0,
    column=0,
    padx=15
)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#ef4444",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=clear_all
)

clear_btn.grid(
    row=0,
    column=1,
    padx=15
)

# =====================================================
# STATISTICS SECTION
# =====================================================

stats_frame = tk.Frame(
    root,
    bg="#1e293b",
    bd=2,
    relief=tk.RIDGE
)

stats_frame.pack(
    pady=15,
    padx=20,
    fill="x"
)

count_label = tk.Label(
    stats_frame,
    text="Total Permutations: 0",
    font=("Arial", 13, "bold"),
    bg="#1e293b",
    fg="#facc15"
)

count_label.pack(pady=8)

time_label = tk.Label(
    stats_frame,
    text="Execution Time: 0 sec",
    font=("Arial", 13, "bold"),
    bg="#1e293b",
    fg="#facc15"
)

time_label.pack(pady=8)

# =====================================================
# OUTPUT SECTION
# =====================================================

output_frame = tk.Frame(
    root,
    bg="#1e293b",
    bd=2,
    relief=tk.RIDGE
)

output_frame.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

output_label = tk.Label(
    output_frame,
    text="Generated Password Permutations",
    font=("Arial", 14, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
)

output_label.pack(pady=10)

# =====================================================
# TEXT AREA + SCROLLBAR
# =====================================================

text_frame = tk.Frame(output_frame)

text_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

scrollbar = tk.Scrollbar(text_frame)

output_text = tk.Text(
    text_frame,
    font=("Consolas", 12),
    bg="#020617",
    fg="#22c55e",
    insertbackground="white",
    yscrollcommand=scrollbar.set,
    wrap="word"
)

scrollbar.config(command=output_text.yview)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)

output_text.pack(
    side=tk.LEFT,
    fill="both",
    expand=True
)

# =====================================================
# FOOTER
# =====================================================

footer = tk.Label(
    root,
    text="Developed for Experiential Learning Project | MCA",
    font=("Arial", 10),
    bg="#0f172a",
    fg="gray"
)

footer.pack(pady=10)

# =====================================================
# RUN APPLICATION
# =====================================================

root.mainloop()