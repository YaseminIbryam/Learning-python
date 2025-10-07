import tkinter as tk
from tkinter import messagebox, simpledialog
import random


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.categories = {
            "Animals": ["cat"],  # "dog", "elephant", "giraffe", "monkey"
            "Countries": ["india", "japan", "brazil", "australia", "canada"],
            "Fruits": ["apple", "banana", "orange", "grape", "kiwi"]
        }
        self.current_category = None
        self.secret_word = None
        self.guesses_left = 6
        self.guesses = set()

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.category_label = tk.Label(master, text="Category: ")
        self.category_label.pack()

        self.word_display = tk.Label(master, text="", font=("Helvetica", 20))
        self.word_display.pack()

        self.label = tk.Label(master, text="Guess a letter:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.guess_button.pack()

        self.new_word_button = tk.Button(master, text="New Word", command=self.choose_new_word)
        self.new_word_button.pack()

        self.choose_category()

    from tkinter import simpledialog

    def choose_category(self):
        category_names = list(self.categories.keys())
        chosen_category = simpledialog.askstring("Choose Category",
                                                 "Please enter a category name:\n" + "\n".join(category_names))
        if chosen_category and chosen_category in self.categories:
            self.current_category = chosen_category.capitalize()
        else:
            messagebox.showinfo("Hangman Game", "Invalid category name. Please choose from the available categories.")
            self.choose_category()

    def choose_new_word(self):
        if not self.current_category:
            messagebox.showinfo("Hangman Game", "Please choose a category first.")
            return

        messagebox.showinfo("Hangman Game", f"Choose a new word from the {self.current_category} category:")
        chosen_word = simpledialog.askstring("Choose Word",
                                             f"Please enter a word from the {self.current_category} category:")
        if chosen_word and chosen_word.lower() in self.categories[self.current_category]:
            self.secret_word = chosen_word.lower()
            print("Chosen word:", self.secret_word)  # Add this line for debugging
            self.update_word_display()
        else:
            messagebox.showinfo("Hangman Game",
                                "Invalid word. Please choose from the available words in the selected category.")
            self.choose_new_word()

    def draw_hangman(self):
        self.canvas.delete("all")  # Clear the canvas before drawing
        # Define the parts of the hangman's body as a list
        hangman_parts = [
            # Head
            lambda: self.canvas.create_oval(150, 100, 250, 200),
            # Body
            lambda: self.canvas.create_line(200, 200, 200, 350),
            # Left arm
            lambda: self.canvas.create_line(200, 250, 150, 300),
            # Right arm
            lambda: self.canvas.create_line(200, 250, 250, 300),
            # Left leg
            lambda: self.canvas.create_line(200, 350, 150, 400),
            # Right leg
            lambda: self.canvas.create_line(200, 350, 250, 400)
        ]

        # Draw the hangman's body parts based on the number of incorrect guesses
        for i in range(6 - self.guesses_left):
            hangman_parts[i]()

    def guess_letter(self):
        letter = self.entry.get().lower()
        if letter.isalpha():  # Check if the input is a valid letter
            if letter not in self.guesses:
                self.guesses.add(letter)
                self.update_word_display()  # Update the displayed word with the guessed letters
                if letter not in self.secret_word:
                    self.guesses_left -= 1
                    self.draw_hangman()
                    messagebox.showinfo("Hangman Game", f"The letter '{letter}' is not in the word.")
                else:
                    messagebox.showinfo("Hangman Game", f"The letter '{letter}' is in the word.")
            else:
                messagebox.showinfo("Hangman Game", "You've already guessed this letter.")
        else:
            messagebox.showinfo("Hangman Game", "Please enter a valid letter.")

    def update_word_display(self):
        word_display_text = ""
        for char in self.secret_word:
            if char in self.guesses:
                word_display_text += char + " "
            else:
                word_display_text += "_ "
        self.word_display.config(text=word_display_text.strip())  # Remove trailing space


def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
