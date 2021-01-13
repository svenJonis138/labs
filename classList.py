def classList():

    # list to hold the class names
    nameList =[]
    # asks user for number of classes
    numberClasses = input("How many classes are you taking? ")
    # loop to get class names based on number of classes
    for i in range(0, int(numberClasses)):
        # user inputs class name here
        newClass = input("Please enter class ")
        # added to the list
        nameList.append(newClass)
        # prints out list of classes
    print(nameList)
classList()