import tkinter
import HangmanTurtle
import random
import sys
import os

word_bank = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure',
             'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle',
             'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing',
             'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri',
             'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage',
             'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby',
             'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo',
             'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku',
             'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice',
             'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey',
             'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole',
             'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths',
             'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz',
             'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph',
             'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia',
             'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz',
             'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv',
             'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold',
             'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript',
             'transgress', 'transplant', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown',
             'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy',
             'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy' 'witchcraft',
             'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful',
             'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie', 'zyzzyvas']

guessed_letters = []
correct_guesses = []
incorrect_guesses = 0

# Selecting word
word_index = random.randrange(0, len(word_bank) - 1)
word = word_bank[word_index]
word_progress = "_" * len(word)


def get_guessed_letters(letter_list):
    letter_string = ''
    for letter in letter_list:
        letter_string += str.upper(letter) + '  '
    return letter_string


def on_validate(event, button_submit):
    guess = event.widget.get()
    if len(guess) == 1 and (guess.isalpha()) and guess.upper() not in (guessed_letters + correct_guesses):
        button_submit.config(state=tkinter.NORMAL)
    else:
        button_submit.config(state=tkinter.DISABLED)


def on_enter(event, submit_button):
    submit_button.invoke()


def disable_button(submit_button):
    submit_button.config(state=tkinter.DISABLED)


def freeze(window):
    window.grab_set()


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def win(window, label_guess_word):
    label_guess_word.config(text=f"You Win! The word was {word}.")
    freeze(window)
    answer = tkinter.messagebox.askyesno("Hangman", "Play Again?")
    if answer:
        restart_program()
    else:
        window.quit()


def loose(window, label_guess_word):
    label_guess_word.config(text=f"You Lost! The word was {word}.")
    freeze(window)
    answer = tkinter.messagebox.askyesno("Hangman", "Play Again?")
    if answer:
        restart_program()
    else:
        window.quit()


def clicked(guess, entry_guess, pen, label_guess_letters, label_guess_word, word_progress_display, window):
    global word_progress, incorrect_guesses
    if guess not in word:
        incorrect_guesses += 1
        guessed_letters.append(guess.upper())
        label_guess_letters.config(text=f'Guessed Letters:\n{get_guessed_letters(guessed_letters)}')
        pen.draw_man(incorrect_guesses)
    else:
        correct_guesses.append(guess.upper())

    entry_guess.delete(0, tkinter.END)
    correct_indexes = []

    for i in range(len(word)):
        if guess.casefold() == word[i].casefold():
            correct_indexes.append(i)

    if len(correct_indexes) > 0:
        word_char_list = []
        for char in word_progress:
            word_char_list.append(char)

        for i in correct_indexes:
            word_char_list[i] = guess

        word_progress = ''
        for char in word_char_list:
            word_progress += char.upper()

    word_progress_display = ''
    for letter in word_progress:
        word_progress_display += letter + ' '
    label_guess_word.config(text=word_progress_display)

    if word_progress.casefold() == word.casefold():
        win(window, label_guess_word)
    if incorrect_guesses == 6:
        loose(window, label_guess_word)


def main():
    # Main window
    window = tkinter.Tk()
    window.title("Hangman")
    window.maxsize(900, 700)
    window.minsize(900, 700)

    # Frame for text & entry
    frame_text = tkinter.Frame(master=window, pady=10)

    # Labels & entry for the text frame
    word_progress_display = ''
    for letter in word_progress:
        word_progress_display += letter + ' '

    label_guess_letters = tkinter.Label(master=frame_text,
                                        text=f'Guessed Letters:\n{get_guessed_letters(guessed_letters)}')
    label_guess_word = tkinter.Label(master=frame_text, pady=25, text=word_progress_display)
    entry_guess = tkinter.Entry(master=frame_text, font=144)

    entry_guess.bind("<KeyRelease>" or "<<ComboboxSelected>>", lambda event: on_validate(event, button_submit))
    entry_guess.bind("<Return>", lambda event: on_enter(event, button_submit))

    # Packing text
    label_guess_letters.pack()
    label_guess_word.pack()
    entry_guess.pack()
    frame_text.pack()

    # Button for submission
    button_submit = tkinter.Button(text="Submit",
                                   command=lambda: (
                                       clicked(entry_guess.get(), entry_guess, pen, label_guess_letters,
                                               label_guess_word, word_progress_display, window),
                                       disable_button),
                                   state=tkinter.DISABLED)

    # Packing button
    button_submit.pack()
    button_submit.place(x=570, y=118)

    # Frame for turtle
    frame_turtle = tkinter.Frame(master=window, pady=25)
    turtle_canvas = tkinter.Canvas(master=frame_turtle, width=500, height=500, background='#181818')

    # Packing canvas
    turtle_canvas.pack()
    frame_turtle.pack()

    pen = HangmanTurtle.HangmanTurtle(turtle_canvas)
    pen.draw_gallows()

    window.mainloop()


if __name__ == "__main__":
    main()
