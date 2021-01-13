def hello_birthday():

    # asks user for their name
    name = input("Hello, what is your name? ")
    # asks for birthday month
    month = input("Nice to meet you " + name + " what month were you born in? ")
    # determines length of the name
    nameLength = len(name)
    # finally reveals to the user (after all this time) how many letters are in their name
    print("your name has " + str(nameLength) + " letters " + " in it")
    # if their birthday is in august, they get a special message
    if month.lower() == "august":
        print("Happy Birthday Month!")

hello_birthday()




