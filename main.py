# coding: utf-8

__author__ = 'Eric-Nicolas'


def launch_intro(movies: dict) -> None:
    print("Welcome to the cinema, here are the movies on the bill:")
    for key, value in movies.items():
        print("Movie n°{0} title: {1}, {2} session ({3} seats available)".format(key, value[0], value[1], value[2]))
    print()


def get_user_choice(movies: dict) -> int:
    user_choice = 0
    while user_choice == 0:
        user_choice = input("Which movie do want to watch ? Write the number id: ")

        try:
            user_choice = int(user_choice)
            if user_choice not in movies.keys():
                raise ValueError
        except ValueError:
            print("Please enter a number included in " + str(movies.keys()) + '\n')
            user_choice = 0
    return user_choice


def main() -> None:
    SEATS = (200, 80, 120)
    movies = {
        1: ["Voyage au centre du html", '06:00 p.m', SEATS[0]],
        2: ["Les 9 jsons cachés", '07:30 p.m', SEATS[1]],
        3: ["Algobox, le Film", '09:00 p.m', SEATS[2]]
    }

    launch_intro(movies)

    while True:
        user_choice = get_user_choice(movies)

        if movies[user_choice][2] - 1 > 0:
            movies[user_choice][2] -= 1
            print("There are " + str(movies[user_choice][2]) + " seats available.\n")
        else:
            print("Full movie!\n")
            movies[user_choice][2] = SEATS[user_choice]
            launch_intro(movies)


if __name__ == '__main__':
    main()
