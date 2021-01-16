
class Author:
    # init function to create instance variables for the Author class
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        # publish function to add titles to the book list
        if self.books.__contains__(title):
            # checks if the title is already in the list
            print('This book has already been added')
        else:
            # if it is not a duplicate, it will be added to the list
            self.books.append(title)

    def __str__(self):
        # str function to format output
        titles = ', '.join(self.books) or 'No published books yet.'
        return f'{self.name}. Books: {titles}'


def main():
    # test data
    thompson = Author('Hunter S. Thompson')
    thompson. publish('Fear and Loathing in Las Vegas')
    thompson. publish('Hell\'s Angels')
    thompson. publish('Fear and Loathing on the Campaign Trail')
    thompson.publish('Fear and Loathing in Las Vegas')
    print(thompson)
    # one day maybe
    jones = Author('Sven Jonis')
    print(jones)


main()
