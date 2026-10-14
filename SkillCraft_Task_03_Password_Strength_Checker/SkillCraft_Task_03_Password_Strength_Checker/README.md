# SkillCraft Task 03 — Password Strength Checker

A beginner-friendly Python desktop application that assesses password strength using length and character-type criteria.

## Features
- Checks minimum length and recommended 12+ character length
- Checks uppercase letters, lowercase letters, numbers, and special characters
- Gives a simple score out of 6 and a strength label
- Provides improvement suggestions for common weak patterns
- Show/hide password option
- Runs locally; it does not save or transmit the password

## Requirements
- Python 3.10 or newer
- Tkinter (included with most standard Windows Python installations)
- No third-party packages required

## Run on Windows
1. Install Python from https://www.python.org/downloads/ if it is not installed.
2. Download or clone this repository.
3. Open Command Prompt in the project folder.
4. Run:

```bash
py password_strength_checker.py
```

If `py` does not work, try `python password_strength_checker.py`.

## How it works
The application checks length and character categories using Python regular expressions. It adds one point for each of six criteria, then assigns a strength label and displays suggestions. This is a basic educational checker, not a guarantee against every password attack.

## Important security note
Do not enter a real password you use for any account into a demo or screenshot. Use a sample password instead. This application does not store or send entered passwords.
