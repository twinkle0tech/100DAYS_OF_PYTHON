# 🎮 Hangman Game (Python)

This is a simple **Hangman game** made using Python.  
The program randomly selects a word and you have to guess it letter by letter before you lose all lives.

---

## ✅ Features
- Random word selection
- 6 lives system
- Shows guessed letters
- Hangman stages graphics
- Win & Lose message

---

## 📂 Files Used
This project uses 3 files:

- `main.py` → main game code  
- `hangman_words.py` → contains the word list   
- `hangman_art.py` → contains logo + stages   

---

## 🧠 Functions / Modules Used
Some important things used in this project:

- `random.choice()` → to randomly pick a word from the list
- `input()` → to take user guess
- `.lower()` → to convert input into lowercase
- `len()` → to get word length
- `for loop` → to check letters and build the display
- `if / else` conditions → to check correct/wrong guesses
- `while loop` → to keep game running until win/lose
- `print()` → to display game progress

---

## ▶️ How to Run
1. Open the folder in VS Code / PyCharm
2. Run the file:

```bash
python main.py

```
---

## 🕹️ How to Play

- The game will show blanks like _ _ _ _

- Type one letter and press Enter

- If the letter is wrong, you lose a life

- Guess the full word before lives become 0

---

## ✅ Output

- Lives left will be shown like: 6/6 LIVES LEFT

- After every guess, the word progress and hangman stage will display

---

## Demo Image
<img src="demo_image.png" title="UI"></img>

---

### 👤 Author

Muskan Tamang
Student | Learning Python
Part of 100 Days of Python