known_users = ["hrusi","ronil","kumar","banshi","Anuradha"]

while True:
    print("Hi My name is Travis!!")

    name = input("What is your name?: ").strip().lower()

    if name in known_users:
        print("Hello {} !".format(name))
        remove = input("DO you want to be removed from the list?: ").strip()
        if remove =="y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        else:
            print("Nevre mind")
        
    else:
        print("I dont think i know you {} !!".format(name))
        add_me = input("do you want to add name to list?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print(known_users)
        else:
            print("No worries!!")
    
