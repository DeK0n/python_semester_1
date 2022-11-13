class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print("Name: ", self.name, "/ Author: ",
              self.author, "/ Pages: ", self.pages)


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        print("Name: ", self.name, "/ Editor: ", self.editor)


book_1 = Book("Campartment No. 6", "Rosa Liksom", 192)
magazine_1 = Magazine("Donald Duck", "Aki Hyppa")

book_1.print_information()
magazine_1.print_information()
