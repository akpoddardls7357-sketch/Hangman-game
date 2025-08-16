import tkinter as tk
import random

# Predefined words
words = ["python", "hangman", "game", "random", "loop"]

# Pick a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = []
max_attempts = 6

# Hangman drawing steps
def draw_hangman(stage):
    canvas.delete("all")  # clear previous drawing
    # Base
    canvas.create_line(20, 180, 120, 180, width=3)  # base
    canvas.create_line(70, 180, 70, 20, width=3)    # pole
    canvas.create_line(70, 20, 150, 20, width=3)    # top
    canvas.create_line(150, 20, 150, 40, width=3)   # rope

    if stage >= 1:  # head
        canvas.create_oval(130, 40, 170, 80, width=2)
    if stage >= 2:  # body
        canvas.create_line(150, 80, 150, 130, width=2)
    if stage >= 3:  # left arm
        canvas.create_line(150, 90, 120, 110, width=2)
    if stage >= 4:  # right arm
        canvas.create_line(150, 90, 180, 110, width=2)
    if stage >= 5:  # left leg
        canvas.create_line(150, 130, 130, 160, width=2)
    if stage >= 6:  # right leg
        canvas.create_line(150, 130, 170, 160, width=2)

# Update the displayed word and status
def update_display():
    display_word = ""
    for letter in word:
        display_word += letter + " " if letter in guessed_letters else "_ "
    word_label.config(text=display_word.strip())
    wrong_label.config(text=f"Wrong guesses: {', '.join(wrong_guesses)}")
    attempts_label.config(text=f"Attempts left: {max_attempts - len(wrong_guesses)}")
    draw_hangman(len(wrong_guesses))

# Handle a guessed letter
def guess_letter():
    letter = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        message_label.config(text="Enter a single letter!")
        return

    if letter in guessed_letters or letter in wrong_guesses:
        message_label.config(text="You already guessed that!")
        return

    if letter in word:
        guessed_letters.append(letter)
        message_label.config(text="Good guess! 🎉")
    else:
        wrong_guesses.append(letter)
        message_label.config(text="Wrong guess! ❌")

    update_display()

    # Win condition
    if all(l in guessed_letters for l in word):
        message_label.config(text=f"You win! The word was '{word}' 🎯")
        guess_button.config(state=tk.DISABLED)
    # Lose condition
    elif len(wrong_guesses) == max_attempts:
        message_label.config(text=f"Game over! The word was '{word}' 💀")
        guess_button.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x400")

# Canvas for stickman
canvas = tk.Canvas(root, width=250, height=200)
canvas.pack()

# Labels and input
word_label = tk.Label(root, text="", font=("Arial", 20))
word_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 14))
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 14))
guess_button.pack(pady=5)

wrong_label = tk.Label(root, text="", font=("Arial", 12))
wrong_label.pack()

attempts_label = tk.Label(root, text="", font=("Arial", 12))
attempts_label.pack()

message_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
message_label.pack(pady=5)

# Initialize display
update_display()

root.mainloop()
