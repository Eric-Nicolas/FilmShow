# coding: utf-8
import tkinter as tk


__author__ = 'Eric-Nicolas'


class App:
    def __init__(self, movies: dict, seats: tuple) -> None:
        self.RED = '#f33'
        self.WHITE = '#fff'
        self.movies = movies.copy()
        self.SEATS = seats

        self.window = tk.Tk()
        self.window.title("Film Show")
        self.window.geometry('850x360')
        self.window.minsize(850, 360)
        self.window.iconbitmap('app_icon.ico')
        self.window.config(background=self.RED)

        title_frame = tk.Frame(self.window, bg=self.RED, bd=1, relief=tk.SUNKEN)
        tk.Label(title_frame, text="Welcome to the cinema!", font=('Courrier', 40), bg=self.RED, fg=self.WHITE).pack()
        tk.Label(title_frame, text="Here are the movies on the bill:", font=('Courrier', 25), bg=self.RED, fg=self.WHITE).pack()
        title_frame.pack(expand=tk.YES)

        list_frame = tk.Frame(self.window, bg=self.RED, bd=1, relief=tk.SUNKEN)
        for key, value in movies.items():
            movie_text = "Movie n°{0} title: {1}, {2} session ({3} seats available)".format(key, value[0], value[1], value[2])
            tk.Label(list_frame, text=movie_text, font=('Courrier', 15), bg=self.RED, fg=self.WHITE).grid(row=key, column=0, sticky=tk.W)
            self.create_button(list_frame, key)
        list_frame.pack(expand=tk.YES)

    def create_button(self, frame: tk.Frame, key: int) -> None:
        if key == 1:
            cmd = self.book1
        elif key == 2:
            cmd = self.book2
        else:
            cmd = self.book3
        tk.Button(frame, text='BOOK', font=('Courrier', 15), bg=self.WHITE, fg=self.RED, command=cmd).grid(row=key, column=1, sticky=tk.W)

    def create_popup(self) -> None:
        popup = tk.Toplevel()
        popup.title("Book info")
        popup.geometry('300x100')
        tk.Label(popup, text="Full movie!", font=('Courrier', 10)).pack(expand=tk.YES)
        tk.Button(popup, text='OK', command=popup.destroy).pack(padx=10, pady=10)
        popup.transient()
        popup.grab_set()
        self.window.wait_window(popup)

    def run(self) -> None:
        self.window.mainloop()

    def book(self, key: int) -> None:
        if self.movies[key][2] - 1 > 0:
            self.movies[key][2] -= 1
        else:
            self.create_popup()
            self.movies[key][2] = self.SEATS[key - 1]

    def book1(self) -> None:
        self.book(1)

    def book2(self) -> None:
        self.book(2)

    def book3(self) -> None:
        self.book(3)
