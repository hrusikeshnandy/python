movies = {
    "war":{"age":18,"seats":10},
    "chochore":{"age":18,"seats":5},
    "bala":{"age":10,"seats":7},
    "dream girl":{"age":18,"seats":8}
    }

while True:
    choice = input("Which movie you want to watch?: ").strip().lower()
    if choice in movies:
        age = int(input("what is your age?: ").strip())
        if age >= movies[choice]["age"]:
            seat_num = movies[choice]["seats"]
            if seat_num > 0:
                print("Enjoy the film")
                movies[choice]["seats"] = movies[choice]["seats"]-1
            else:
                print("We are sold out .....")
        else:
            print("You are too young for the movie!!")
        print();
    else:
        print("Sorry we do not have this movie")
        add_me = input("Want to add the movie to collection?: ").strip().lower()
        if add_me == "y":
            print("adding the {} to the collection..".format(choice))
            age = input("Set the age bar: ").strip()
            num_seat = input("Enterthe max capacity of seat: ").strip()
            movies[choice]={"age":age,"seats":num_seat}
            print(movies.keys())
        else:
            print("No worries")
