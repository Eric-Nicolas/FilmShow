# coding: utf-8
from app import App

__author__ = 'Eric-Nicolas'


def main() -> None:
    SEATS = (200, 80, 120)
    MOVIES = {
        1: ["Voyage au centre du html", '06:00 p.m', SEATS[0]],
        2: ["Les 9 jsons cachés", '07:30 p.m', SEATS[1]],
        3: ["Algobox, le Film", '09:00 p.m', SEATS[2]]
    }

    app = App(MOVIES, SEATS)
    app.run()


if __name__ == '__main__':
    main()
