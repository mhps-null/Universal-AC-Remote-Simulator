# Simulasi Remote AC dengan pendekatan Computational Thinking

Diperuntukkan untuk tugas besar projek II mata kuliah WI1102 Computational Thinking Semester 1


[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **universal air conditioner remote simulator** with a GUI, capable of controlling temperature, modes, fan speed, timer, sleep, swing, and simulating room temperature and humidity.  
This project allows testing and visualizing how an AC remote interacts with different AC models via IR codes.

---

## 📌 Table of Contents

- [Features](#-features)  
- [Prerequisites](#-prerequisites)  
- [Installation](#-installation)  
- [File Structure](#-file-structure)  
- [Screenshots](#-screenshots)  
- [License](#-license)  

---

## Features

- Automatic synchronization of IR codes with different AC models  
- Adjustable temperature (+/- 1°C)  
- Multiple modes: Auto, Cool, Dry, Fan, Eco  
- Fan speed control: Turbo, Quiet, Normal  
- Timer functionality & Clock display  
- Swing mode for fan  
- Sleep mode with gradual temperature adjustment  
- Simulated room temperature & humidity sensors  

---

## Prerequisites

Before running the program, ensure:

1. **Python 3.x** is installed on your computer.  
   - Check with:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```

2. **Tkinter** module is available (usually bundled with Python).  
   - For Linux, if not installed:
     ```bash
     sudo apt install python3-tk
     ```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   ```

## Run The Program

1. Clone this repository:
   ```bash
   python remote-AC.py
    ```
    or
    ```bash
   python3 remote-AC.py
    ```

2. Input current temperature (in Celcius)
```bash
Masukkan suhu ruang saat ini: [input here]
```
```markdown
Note:
When you run the program, it will prompt you to enter the current room temperature:
```

3. Input current humidity (scale 1-100)
```bash
Masukkan % kelembaban relatif (Skala: 1-100): [input here]
```
```markdown
Note:
When you run the program, it will prompt you to enter the current room humidity:
```

## File Structure
repo/
│
├─ remote-AC.py             # Main AC remote program
├─ suhu_terakhir.txt    # Stores last set temperature
├─ README.md           # Project documentation
└─ LICENSE 

## Screenshots
![Sample Run](screenshot.png)