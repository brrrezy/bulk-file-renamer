# 📁 Bulk File Renamer

A Python tool for renaming multiple files at once.  
Includes **two versions**:  

1. **CMD Panel Version** (`rename.py`) – Clean terminal interface  
2. **GUI Version** (`rename_gui.py`) – Simple Tkinter window with browse and rename buttons  

---

## 🚀 Features

- Rename multiple files with a custom prefix
- Automatic numbering (001, 002, 003…)
- CMD version shows progress line-by-line
- GUI version provides folder picker and success messages
- Renames only files (ignores folders)
- Lightweight, no extra libraries needed besides Tkinter for GUI

---

## 🖥️ CMD Panel Preview

```
==================================================
                BULK FILE RENAMER
==================================================

📁 Paste folder path: D:\Photos

✅ Found 15 files

🔤 Enter prefix: trip

Renaming files...

✔ image1.jpg  →  trip_001.jpg  
✔ image2.jpg  →  trip_002.jpg  

==================================================
🎉 15 files successfully renamed!
==================================================
```

---

## 🖼 GUI Version Screenshot (Tkinter)

- Select folder using **Browse**
- Enter desired **prefix**
- Click **Rename Files**
- Success message displayed in popup

---

## 📦 Requirements

- Python 3.x  
- Windows / macOS / Linux  
- Tkinter is required for the GUI version (comes with most Python installations)

Check Python version:

```bash
python --version
```

---

## ⚙️ Installation

1. Clone the repository or download files:

```bash
git clone https://github.com/yourusername/bulk-file-renamer.git
```

2. Navigate to the project directory:

```bash
cd bulk-file-renamer
```

---

## ▶️ Usage

### CMD Version

```bash
python rename.py
```

- Paste folder path  
- Enter prefix  
- Watch files get renamed in terminal

### GUI Version

```bash
python rename_gui.py
```

- Browse folder  
- Enter prefix  
- Click **Rename Files**  

---

## 🧠 How It Works

- Lists all items in folder  
- Filters **only files**  
- Creates new names with prefix + zero-padded numbers  
- Uses `os.rename()` to rename files  

Example:

```
trip_001.jpg
trip_002.jpg
trip_003.jpg
```

---

## ⚠️ Important Notes

- Action **cannot be undone**  
- Ensure folder path is correct  
- Existing files with target names **will be overwritten**

---

## 💡 Future Improvements

- File type filter (e.g., only `.jpg`)  
- Dry-run preview mode  
- Undo functionality  
- Colored terminal output (CMD version)  

---

## 🛠 Built With

- Python  
- `os`, `sys` modules  
- Tkinter (GUI version)

---

## 📜 License

Open-source, free to use.  

---

## 👨‍💻 Author

brrrezy  

Star the repository ⭐ if you find it useful!
