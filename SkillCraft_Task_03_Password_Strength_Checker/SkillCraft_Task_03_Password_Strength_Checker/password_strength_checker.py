import re
import tkinter as tk
from tkinter import ttk, messagebox

COMMON_PASSWORDS = {
    "password", "password123", "123456", "123456789", "qwerty",
    "admin", "letmein", "welcome", "iloveyou", "abc123"
}

def assess_password(password: str):
    """Return a score, strength label, checklist, and improvement tips."""
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters (recommended)": len(password) >= 12,
        "Contains an uppercase letter (A–Z)": bool(re.search(r"[A-Z]", password)),
        "Contains a lowercase letter (a–z)": bool(re.search(r"[a-z]", password)),
        "Contains a number (0–9)": bool(re.search(r"\d", password)),
        "Contains a special character": bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    if not password:
        return 0, "Enter a password", checks, ["Type a password to see the assessment."]

    score = 0
    score += 1 if len(password) >= 8 else 0
    score += 1 if len(password) >= 12 else 0
    score += 1 if re.search(r"[A-Z]", password) else 0
    score += 1 if re.search(r"[a-z]", password) else 0
    score += 1 if re.search(r"\d", password) else 0
    score += 1 if re.search(r"[^A-Za-z0-9]", password) else 0

    tips = []
    if len(password) < 12:
        tips.append("Use 12 or more characters.")
    if not re.search(r"[A-Z]", password):
        tips.append("Add an uppercase letter.")
    if not re.search(r"[a-z]", password):
        tips.append("Add a lowercase letter.")
    if not re.search(r"\d", password):
        tips.append("Add a number.")
    if not re.search(r"[^A-Za-z0-9]", password):
        tips.append("Add a special character, such as !, @, or #.")
    if password.lower() in COMMON_PASSWORDS:
        score = min(score, 1)
        tips.insert(0, "Avoid common passwords that are easy to guess.")
    if re.search(r"(.)\1{3,}", password):
        tips.append("Avoid repeating the same character many times.")
    if re.search(r"1234|abcd|qwerty", password.lower()):
        tips.append("Avoid predictable sequences or keyboard patterns.")

    if password.lower() in COMMON_PASSWORDS:
        label = "Very Weak"
    elif score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    else:
        label = "Strong"

    if label == "Strong" and (re.search(r"(.)\1{3,}", password) or
                              re.search(r"1234|abcd|qwerty", password.lower())):
        label = "Moderate"

    return score, label, checks, tips

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        root.title("Password Strength Checker")
        root.geometry("650x610")
        root.minsize(600, 570)
        root.configure(bg="#f4f6fb")

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("TButton", padding=7)
        style.configure("TCheckbutton", background="#ffffff", font=("Segoe UI", 10))

        outer = tk.Frame(root, bg="#f4f6fb", padx=26, pady=22)
        outer.pack(fill="both", expand=True)

        tk.Label(outer, text="PASSWORD STRENGTH CHECKER",
                 font=("Segoe UI", 19, "bold"), bg="#f4f6fb", fg="#202744").pack(anchor="w")
        tk.Label(outer, text="Check password characteristics locally on your device.",
                 font=("Segoe UI", 10), bg="#f4f6fb", fg="#596174").pack(anchor="w", pady=(4, 18))

        card = tk.Frame(outer, bg="white", padx=20, pady=18,
                        highlightbackground="#dfe4ef", highlightthickness=1)
        card.pack(fill="x")

        tk.Label(card, text="Enter a password", font=("Segoe UI", 11, "bold"),
                 bg="white", fg="#202744").pack(anchor="w")
        row = tk.Frame(card, bg="white")
        row.pack(fill="x", pady=(8, 12))
        self.password_var = tk.StringVar()
        self.entry = tk.Entry(row, textvariable=self.password_var, show="•",
                              font=("Consolas", 13), relief="solid", bd=1)
        self.entry.pack(side="left", fill="x", expand=True, ipady=8)
        self.show_var = tk.BooleanVar(value=False)
        tk.Checkbutton(row, text="Show", variable=self.show_var, command=self.toggle_show,
                       bg="white", activebackground="white").pack(side="left", padx=(10, 0))

        self.strength_label = tk.Label(card, text="Enter a password", font=("Segoe UI", 14, "bold"),
                                       bg="white", fg="#596174")
        self.strength_label.pack(anchor="w")
        self.progress = ttk.Progressbar(card, maximum=6, mode="determinate")
        self.progress.pack(fill="x", pady=(8, 4))
        self.score_label = tk.Label(card, text="Score: 0 / 6", font=("Segoe UI", 9),
                                    bg="white", fg="#596174")
        self.score_label.pack(anchor="w")

        checks_card = tk.Frame(outer, bg="white", padx=20, pady=16,
                               highlightbackground="#dfe4ef", highlightthickness=1)
        checks_card.pack(fill="x", pady=(16, 0))
        tk.Label(checks_card, text="Security checklist", font=("Segoe UI", 12, "bold"),
                 bg="white", fg="#202744").pack(anchor="w", pady=(0, 8))
        self.check_vars = {}
        for name in [
            "At least 8 characters",
            "At least 12 characters (recommended)",
            "Contains an uppercase letter (A–Z)",
            "Contains a lowercase letter (a–z)",
            "Contains a number (0–9)",
            "Contains a special character",
        ]:
            var = tk.BooleanVar(value=False)
            self.check_vars[name] = var
            tk.Checkbutton(checks_card, text=name, variable=var, state="disabled",
                           disabledforeground="#27324b", bg="white",
                           activebackground="white", font=("Segoe UI", 10)).pack(anchor="w", pady=1)

        tips_card = tk.Frame(outer, bg="#fffaf0", padx=18, pady=13,
                             highlightbackground="#f0dfb8", highlightthickness=1)
        tips_card.pack(fill="x", pady=(16, 0))
        tk.Label(tips_card, text="Suggestions", font=("Segoe UI", 11, "bold"),
                 bg="#fffaf0", fg="#674d12").pack(anchor="w")
        self.tips_text = tk.Label(tips_card, text="Type a password to receive suggestions.",
                                  justify="left", anchor="w", wraplength=560,
                                  font=("Segoe UI", 9), bg="#fffaf0", fg="#674d12")
        self.tips_text.pack(fill="x", pady=(5, 0))

        tk.Label(outer, text="Privacy: the password is assessed in this app and is not saved or sent anywhere.",
                 font=("Segoe UI", 8), bg="#f4f6fb", fg="#596174",
                 wraplength=590, justify="left").pack(anchor="w", pady=(13, 0))

        self.password_var.trace_add("write", self.update_assessment)
        self.entry.focus_set()

    def toggle_show(self):
        self.entry.configure(show="" if self.show_var.get() else "•")

    def update_assessment(self, *_):
        password = self.password_var.get()
        score, label, checks, tips = assess_password(password)
        colors = {
            "Enter a password": "#596174",
            "Very Weak": "#b42318",
            "Weak": "#d04a36",
            "Moderate": "#b7791f",
            "Strong": "#16803c",
        }
        self.strength_label.configure(text=label, fg=colors.get(label, "#596174"))
        self.progress["value"] = score
        self.score_label.configure(text=f"Score: {score} / 6")
        for name, value in checks.items():
            self.check_vars[name].set(value)
        if tips:
            self.tips_text.configure(text="\n".join("• " + tip for tip in tips))
        else:
            self.tips_text.configure(text="• Good result! Avoid reusing this password on other accounts.")

def main():
    root = tk.Tk()
    PasswordCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
