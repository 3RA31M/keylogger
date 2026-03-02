# Python Keylogger (Educational Project)

⚠️ **Disclaimer**
This project is created strictly for **educational and ethical purposes**.
Do **NOT** use this software on devices you do not own or without explicit permission.
Unauthorized keylogging is illegal and unethical.

---

## 📌 Overview

This project demonstrates how keyboard events can be captured in Python using
low-level input hooks. It is intended to help learners understand:

- How keyboard listeners work
- Event-driven programming in Python
- Secure coding awareness
- Malware detection & prevention concepts

---

## 🛠 Features

- Records key press events
- Saves logs locally with timestamps
- Runs in the background (headless mode)
- Lightweight and simple implementation

---

## 🧰 Technologies Used

- Python 3.x
- `keyboard` module
- `datetime` module

---

## 📂 Project Structure

```
keylogger/
├── main.py           # Main program
├── keystrokes.log    # Output log file
├── .gitignore        # Git ignore rules
└── README.md         # Project documentation
```

## ▶️ How It Works (High-Level)

1. A keyboard hook listens for key press events.
2. Each key press is timestamped.
3. Data is written to a local log file.
4. The program runs continuously until stopped.

> No network communication is used in this project.

---

## 🚫 What This Project Does NOT Do

- ❌ No remote access
- ❌ No data exfiltration
- ❌ No persistence mechanisms
- ❌ No hidden installation

---

## 🔐 Ethical Usage

This project should only be used for:
- Learning cybersecurity concepts
- Testing detection software
- Personal experimentation on owned systems

Misuse may violate local and international laws.

---

## 📄 License

This project is licensed for **educational use only**.
You are responsible for how you use this code.