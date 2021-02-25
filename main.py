# coding: utf-8

__author__ = 'Eric-Nicolas'


def main() -> None:
    films = ["Voyage au centre du html", "Les 9 jsons cachés", "Algobox, le Film"]

    print("Welcome to the cinema, here are the movies on the bill")
    for i in range(len(films)):
        print("Film {0}. {1} - Room {0}".format(i+1, films[i]))


if __name__ == '__main__':
    main()
