import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password():
    password = password_entry.get()
    errors = []

    if len(password) < 8:
        errors.append("• At least 8 characters required.")
    if not re.search(r'[A-Z]', password):
        errors.append("• Include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        errors.append("• Include at least one lowercase letter.")
    if not re.search(r'\d', password):
        errors.append("• Include at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("• Include at least one special character (!@#$%^&*).")

    # Clear previous result
    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)

    # Show result
    if errors:
        result_text.insert(tk.END, "❌ Weak Password:\n\n")
        for err in errors:
            result_text.insert(tk.END, err + "\n")
        result_text.config(fg="red")
    else:
        result_text.insert(tk.END, "✅ Strong Password!\nWell done!")
        result_text.config(fg="green")

    result_text.config(state='disabled')

# Main Window
root = tk.Tk()
root.title("🔐 PassGuard")
root.geometry("400x300")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="Enter your password:", font=("Arial", 12))
heading.pack(pady=10)

# Password Entry
password_entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

# Check Button
check_btn = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 11), bg="#4CAF50", fg="white")
check_btn.pack(pady=10)

# Result Box
result_text = tk.Text(root, height=8, width=40, font=("Arial", 10), wrap="word", borderwidth=2, relief="groove")
result_text.pack(pady=10)
result_text.config(state='disabled')

# Run the app
root.mainloop()


