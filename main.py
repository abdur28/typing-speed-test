from tkinter import *
from tkinter import messagebox
import random

import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time


with open("word.txt") as words:
    list_of_words = words.readlines()
    position = random.randint(0, 99)
    my_word0 = list_of_words[position].replace("\n", "").lower()

my_word = my_word0
number_of_word = 1
total = 0

def next_word():
    new_position = random.randint(0, 99)
    new_word = list_of_words[new_position].replace("\n", "").lower()
    global my_word
    global number_of_word
    my_word = new_word
    number_of_word += 1
    word.config(text=my_word)
    text.delete(0, END)
    text.focus()
    if time0._start_time is not None:
        time0.stop()
        time0.start()
    else:
        time0.start()


def done():
    if time0._start_time is not None:
        if text.get() == my_word:
            time0.stop()
            elapsed_time = time.perf_counter() - time0._start_time
            time0._start_time = None
            my_speed = f"{elapsed_time:0.4f} seconds"
            global total
            total += elapsed_time
            speed.config(text=my_speed)
        else:
            messagebox.showinfo(title="Oops", message="INCORRECT SPELLING!!!")

    else:
        pass


def again():
    text.delete(0, END)
    if time0._start_time is not None:
        time0.stop()
        time0.start()
    else:
        time0.start()

def finish():
    if time0._start_time is not None:
        time0.stop()
        messagebox.showinfo(title="Summary",
                            message=f"Your average speed is {(total / number_of_word):0.4f} for {number_of_word} words ")

    else:
        messagebox.showinfo(title="Summary",
                            message=f"Your average speed is {(total / number_of_word):0.4f} for {number_of_word} words ")

def enter(e):
    if time0._start_time is not None:
        if text.get() == my_word:
            time0.stop()
            elapsed_time = time.perf_counter() - time0._start_time
            time0._start_time = None
            my_speed = f"{elapsed_time:0.4f} seconds"
            global total
            total += elapsed_time
            speed.config(text=my_speed)
        else:
            messagebox.showinfo(title="Oops", message="INCORRECT SPELLING!!!")

    else:
        pass
def next0(e):
    new_position = random.randint(0, 99)
    new_word = list_of_words[new_position].replace("\n", "").lower()
    global my_word
    global number_of_word
    my_word = new_word
    number_of_word += 1
    word.config(text=my_word)
    text.delete(0, END)
    text.focus()
    if time0._start_time is not None:
        time0.stop()
        time0.start()
    else:
        time0.start()

def start():
    new_position = random.randint(0, 99)
    new_word = list_of_words[new_position].replace("\n", "").lower()
    global total
    global number_of_word
    global my_word
    my_word = new_word
    number_of_word = 1
    total = 0
    word.config(text=my_word)
    speed.config(text="")
    text.delete(0, END)
    text.focus()
    if time0._start_time is not None:
        time0.stop()
        time0.start()
    else:
        time0.start()

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=600, height=200)
window.config(pady=50, padx=70)
time0 = Timer()
time0.start()
window.bind("<Return>", enter)
window.bind("<space>", next0)

word = Label()
word.config(text=my_word)
word.grid(column=2, row=0)

start_typing = Label()
start_typing.config(text="Start Typing ")
start_typing.grid(column=0, row=1)

speed = Label()
speed.config(text="")
speed.grid(column=1, row=3)

text = Entry()
text.config(width=50)
text.grid(row=1, column=1, columnspan=3)
text.focus()

done_button = Button()
done_button.config(text="Done", width=15, command=done)
done_button.grid(row=2, column=1)

try_again = Button()
try_again.config(text="Try Again", width=15, command=again)
try_again.grid(row=2, column=2)

next_button = Button()
next_button.config(text="Next Word", width=15, command=next_word)
next_button.grid(row=2, column=3)

finish_button = Button()
finish_button.config(text="Finish", width=15, command=finish)
finish_button.grid(row=3, column=3)

start_button = Button()
start_button.config(text="Start", width=15, command=start)
start_button.grid(row=3, column=2)

window.mainloop()
