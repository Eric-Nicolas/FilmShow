# coding: utf-8

__author__ = 'Eric-Nicolas'


def main() -> None:
    movies = {
        0: ("Voyage au centre du html", '06:00 p.m', 200),
        1: ("Les 9 jsons cachés", '07:30 p.m', 80),
        2: ("Algobox, le Film", '09:00 p.m', 120)
    }

    print("Welcome to the cinema, here are the movies on the bill")

    for key, value in movies.items():
        print("Movie n°{0} title: {1}, {2} session ({3} places available)".format(key+1, value[0], value[1], value[2]))


if __name__ == '__main__':
    main()
