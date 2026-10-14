# 🔐 Password Strength Checker

## 📌 About the Project
The Password Strength Checker is a Python application developed as **Task 03 of the SkillCraft Technology internship**. It assesses password strength based on length and the presence of uppercase letters, lowercase letters, numbers, and special characters.

The application displays a strength score, identifies the password strength category, and provides suggestions to improve password security.

## ✨ Features
- Password length validation
- Uppercase and lowercase letter detection
- Number and special character detection
- Password strength score out of 6
- Strength classification: Very Weak, Weak, Moderate, and Strong
- Suggestions for improving password strength
- Show/hide password functionality
- Simple graphical user interface

## 🛠️ Technologies Used
- **Language:** Python
- **GUI:** Tkinter
- **Pattern Matching:** Regular Expressions (`re`)

## 📂 Project Structure
```text
SkillCraft-Task-03-Password-Strength-Checker/
├── password_strength_checker.py
├── README.md
├── requirements.txt
└── screenshots/
    └── sample_result.png
```

## ⚙️ Requirements
- Python 3.10 or newer
- Tkinter (usually included with Python on Windows)
- No additional third-party packages required

## 🚀 Installation and Execution

**Step 1:** Download or clone this repository.

**Step 2:** Open the project folder in Command Prompt or a terminal.

**Step 3:** Run the application:

```bash
py password_strength_checker.py
```

Alternatively, use:

```bash
python password_strength_checker.py
```

**Step 4:** Enter a sample password to view its strength score, classification, and improvement suggestions.

## 🧠 Password Evaluation Criteria
The application checks the following six criteria:

1. At least 8 characters
2. At least 12 characters (recommended)
3. Contains an uppercase letter (A–Z)
4. Contains a lowercase letter (a–z)
5. Contains a number (0–9)
6. Contains a special character

Each satisfied criterion contributes to the score. Common passwords and predictable patterns may also affect the assessment.

## 📸 Sample Output
An illustrative sample result is available in [`screenshots/sample_result.png`](screenshots/sample_result.png).

## 🔒 Security Note
This project is intended for educational purposes. The score is a basic indication of password strength and does not guarantee protection against all attacks. Avoid reusing passwords, and never upload real passwords or sensitive information to public repositories.

## 🎯 Learning Outcomes
- Practiced Python programming
- Learned basic GUI development using Tkinter
- Applied regular expressions for input validation
- Understood basic password security concepts


